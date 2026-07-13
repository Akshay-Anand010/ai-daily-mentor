import json
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler
from app.core.config import settings
from app.models.database import Base, EmailLog, Lesson, SessionLocal, User, UserSettings, engine
from app.services.ingest import collect_articles
from app.services.lesson import CURRICULUM, generate_lesson
from app.services.pdf import render_pdf
from app.services.email import send_lesson

app = FastAPI(title="AI Daily Mentor", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=[settings.frontend_origin], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
def db():
    session = SessionLocal()
    try: yield session
    finally: session.close()

class Subscribe(BaseModel): email: EmailStr
class SettingsInput(BaseModel): timezone: str = "UTC"; delivery_time: str = "07:00"; difficulty: str = "intermediate"; language: str = "python"; mode: str = "hybrid"

@app.on_event("startup")
def startup():
    Base.metadata.create_all(engine)
    scheduler = BackgroundScheduler(timezone="UTC")
    scheduler.add_job(create_daily_lesson, "cron", hour=7, id="daily-lesson", replace_existing=True)
    scheduler.start(); app.state.scheduler = scheduler

def create_daily_lesson():
    with SessionLocal() as session:
        index = session.query(Lesson).count() % len(CURRICULUM); topic = CURRICULUM[index]
        title, content = generate_lesson(topic, collect_articles())
        lesson = Lesson(title=title, topic=topic, difficulty="intermediate", content=content)
        session.add(lesson); session.flush()
        attachment = render_pdf(title, content)
        for user in session.scalars(select(User)).all():
            try:
                status, message_id = send_lesson(user.email, title, attachment)
            except Exception:
                status, message_id = "failed", None
            session.add(EmailLog(user_id=user.id, lesson_id=lesson.id, status=status, provider_message_id=message_id))
        session.commit()

@app.get("/health")
def health(): return {"status": "ok", "time": datetime.utcnow()}
@app.get("/api/lessons")
def lessons(q: str | None = None, session: Session = Depends(db)):
    stmt = select(Lesson).order_by(Lesson.created_at.desc())
    if q: stmt = stmt.where(Lesson.content.ilike(f"%{q}%") | Lesson.title.ilike(f"%{q}%"))
    return [{"id": x.id, "title": x.title, "topic": x.topic, "difficulty": x.difficulty, "created_at": x.created_at} for x in session.scalars(stmt).all()]
@app.get("/api/lessons/today")
def today(session: Session = Depends(db)):
    lesson = session.scalars(select(Lesson).order_by(Lesson.created_at.desc())).first()
    if not lesson:
        create_daily_lesson(); lesson = session.scalars(select(Lesson).order_by(Lesson.created_at.desc())).first()
    return {"id": lesson.id, "title": lesson.title, "topic": lesson.topic, "content": lesson.content, "created_at": lesson.created_at}
@app.get("/api/lessons/{lesson_id}/pdf")
def pdf(lesson_id: int, session: Session = Depends(db)):
    lesson = session.get(Lesson, lesson_id)
    if not lesson: raise HTTPException(404, "Lesson not found")
    return Response(render_pdf(lesson.title, lesson.content), media_type="application/pdf", headers={"Content-Disposition": f'attachment; filename="lesson-{lesson_id}.pdf"'})
@app.post("/api/subscribe", status_code=201)
def subscribe(body: Subscribe, session: Session = Depends(db)):
    user = session.scalar(select(User).where(User.email == body.email))
    is_new = user is None
    if not user:
        user = User(email=body.email); session.add(user); session.flush(); session.add(UserSettings(user_id=user.id))
    session.commit()
    # A first lesson gives a new subscriber immediate confirmation; scheduled
    # delivery continues daily thereafter.
    if is_new:
        lesson = session.scalars(select(Lesson).order_by(Lesson.created_at.desc())).first()
        if lesson:
            try:
                status, message_id = send_lesson(user.email, lesson.title, render_pdf(lesson.title, lesson.content))
            except Exception:
                status, message_id = "failed", None
            session.add(EmailLog(user_id=user.id, lesson_id=lesson.id, status=status, provider_message_id=message_id))
            session.commit()
    return {"message": "You are subscribed."}
