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

## Local setup video

[![Watch the AI Daily Mentor local setup video](https://img.youtube.com/vi/U7eqcbZJGfs/maxresdefault.jpg)](https://youtu.be/U7eqcbZJGfs)

▶ Click the image to watch the step-by-step local setup walkthrough.

## Free local AI mode (recommended for development)

The default provider is [Ollama](https://ollama.com/download/mac), which runs models locally and needs no API key. Install it, then run:

```bash
ollama pull llama3.2
ollama run llama3.2
```

Keep Ollama running and start the app with Docker. The included `.env.example` points Docker on macOS to `host.docker.internal:11434`. For a non-Docker backend, set `OLLAMA_BASE_URL=http://localhost:11434`. Set `LLM_PROVIDER=demo` for a no-model fallback, or `LLM_PROVIDER=openai` and add `OPENAI_API_KEY` to use OpenAI.

Configure `RESEND_API_KEY` and `EMAIL_FROM` to deliver generated PDFs to subscribers. Local models make lesson generation free, but email delivery to public subscribers still requires an email provider and a deployed backend.

For fully local email testing, Docker Compose starts Mailpit automatically. It catches outgoing messages locally (nothing is delivered to the public internet); view them at `http://localhost:8025`.

## Local Setup Demo


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
