"""Provider boundary for transactional lesson delivery.

Resend is used when configured; absence of credentials deliberately results in
an unsent status so local/demo deployments never accidentally email users.
"""
import base64
import httpx
from app.core.config import settings

def send_lesson(recipient: str, title: str, pdf: bytes) -> tuple[str, str | None]:
    if not settings.resend_api_key or not settings.email_from:
        return "skipped_no_provider", None
    payload = {
        "from": settings.email_from, "to": [recipient], "subject": title,
        "html": "<p>Your AI Daily Mentor lesson is attached.</p>",
        "attachments": [{"filename": "ai-daily-mentor.pdf", "content": base64.b64encode(pdf).decode()}],
    }
    response = httpx.post("https://api.resend.com/emails", json=payload, headers={"Authorization": f"Bearer {settings.resend_api_key}"}, timeout=20)
    response.raise_for_status()
    return "sent", response.json().get("id")
