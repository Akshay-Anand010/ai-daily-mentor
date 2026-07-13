"""Provider boundary for transactional lesson delivery.

Resend is used when configured; absence of credentials deliberately results in
an unsent status so local/demo deployments never accidentally email users.
"""
import base64
import smtplib
from email.message import EmailMessage
import httpx
from app.core.config import settings

def send_lesson(recipient: str, title: str, pdf: bytes) -> tuple[str, str | None]:
    if settings.resend_api_key and settings.email_from:
        payload = {
            "from": settings.email_from, "to": [recipient], "subject": title,
            "html": "<p>Your AI Daily Mentor lesson is attached.</p>",
            "attachments": [{"filename": "ai-daily-mentor.pdf", "content": base64.b64encode(pdf).decode()}],
        }
        response = httpx.post("https://api.resend.com/emails", json=payload, headers={"Authorization": f"Bearer {settings.resend_api_key}"}, timeout=20)
        response.raise_for_status()
        return "sent", response.json().get("id")
    if settings.smtp_host and settings.smtp_from:
        message = EmailMessage()
        message["From"] = settings.smtp_from; message["To"] = recipient; message["Subject"] = title
        message.set_content("Your AI Daily Mentor lesson is attached.")
        message.add_attachment(pdf, maintype="application", subtype="pdf", filename="ai-daily-mentor.pdf")
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=20) as server:
            if settings.smtp_user and settings.smtp_password:
                server.starttls(); server.login(settings.smtp_user, settings.smtp_password)
            server.send_message(message)
        return "sent", None
    return "skipped_no_provider", None
