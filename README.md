# AI Daily Mentor

AI Daily Mentor turns trusted AI news and a structured curriculum into a daily, 15–20 minute lesson, a downloadable PDF, and a searchable learning archive.

## What is included

- FastAPI API with OpenAPI docs, PostgreSQL persistence, JWT-ready configuration, a daily scheduler, source ingestion, lesson generation, PDF production, and pluggable email delivery.
- Responsive Next.js dashboard with today, archive, progress, settings, dark mode, and a public subscription form.
- Docker Compose, CI, deployment manifests, tests, and configuration templates.

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Open `http://localhost:3000`; API documentation is at `http://localhost:8000/docs`.

The system runs in a safe demo mode until `OPENAI_API_KEY` and an email provider are configured. In demo mode it creates a curriculum-based lesson without contacting third parties. Configure `RESEND_API_KEY` and `EMAIL_FROM` to deliver the generated PDF to subscribers.

## Deployment and subscriptions

GitHub Pages can host the static dashboard, but it cannot securely store email addresses or run scheduled jobs. Deploy `backend` to Render or Railway and set `NEXT_PUBLIC_API_URL` to its HTTPS URL; the dashboard's subscription form then writes to your backend. Full instructions are in [docs/deployment.md](docs/deployment.md).

## Project layout

```
backend/     FastAPI service and worker
frontend/    Next.js dashboard
docs/        architecture, setup, deployment notes
.github/     CI workflow
```

## Safety

Do not commit `.env`. Use a freshly-created GitHub token only through your local Git credential manager or the GitHub CLI—not in source code, issue comments, or chat.
