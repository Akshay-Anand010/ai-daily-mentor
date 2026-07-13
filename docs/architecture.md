# Architecture

```text
RSS feeds ──> ingestion/ranking ──> lesson generator ──> PostgreSQL
                                      │                  │
                                      └──> PDF/email     └──> FastAPI ──> Next.js
```

The scheduler invokes the job daily at 07:00 UTC. Production deployments should configure a timezone-aware external scheduler or a per-user job queue once delivery preferences are enabled. The generator uses OpenAI Responses when configured and a curriculum lesson fallback otherwise. Feed ingestion only uses public RSS endpoints; no prohibited scraping is performed.

The first production extension points are `services/ingest.py` (approved sources and ranking), `services/lesson.py` (prompt/evaluations), and a `services/email.py` provider adapter for Resend, SMTP, or SendGrid.
