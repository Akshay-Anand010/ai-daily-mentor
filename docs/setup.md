# Setup

1. Install Docker Desktop or Python 3.12/PostgreSQL and Node 22.
2. Copy `.env.example` to `.env` and replace `SECRET_KEY`.
3. Install and run Ollama for free local lesson generation, or alternatively add `OPENAI_API_KEY` and set `LLM_PROVIDER=openai`.
4. Run `docker compose up --build`.
5. Visit the web app at port 3000 and API docs at port 8000/docs.

For local Python testing: `cd backend && pip install -r requirements.txt && pytest`.

## Local model (free)

Install [Ollama for macOS](https://ollama.com/download/mac), then run `ollama pull llama3.2`. The app defaults to `LLM_PROVIDER=ollama`; no OpenAI key is needed. Ollama exposes its local API at port 11434 and does not require authentication for local use. If the backend runs in Docker on macOS, leave `OLLAMA_BASE_URL=http://host.docker.internal:11434`; if it runs directly on your Mac, use `http://localhost:11434`.

Docker Compose also launches Mailpit. It safely captures all local test emails at `http://localhost:8025`; it does not send messages to real inboxes.
