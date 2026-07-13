# Setup

1. Install Docker Desktop or Python 3.12/PostgreSQL and Node 22.
2. Copy `.env.example` to `.env` and replace `SECRET_KEY`.
3. Add `OPENAI_API_KEY` to enable generated lessons. Without it, demo curriculum lessons work offline.
4. Run `docker compose up --build`.
5. Visit the web app at port 3000 and API docs at port 8000/docs.

For local Python testing: `cd backend && pip install -r requirements.txt && pytest`.
