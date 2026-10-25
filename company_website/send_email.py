"""Send a plain-text email through Gmail's SMTP server.

Credentials are read from environment variables (never hardcode them):

    EMAIL_USERNAME   Gmail address used to log in and send
    EMAIL_PASSWORD   Gmail *app password* (not your normal password)
    EMAIL_RECEIVER   Address that receives the message (defaults to EMAIL_USERNAME)

For local development put them in a ``.env`` file (see ``.env.example``);
``python-dotenv`` loads it automatically.
"""

import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv

# Load variables from a local .env file if one exists; a no-op otherwise.
load_dotenv()

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465  # SSL


def _require_env(name):
    """Return the value of an environment variable or fail with a clear message."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"Environment variable {name} is not set. "
            "Copy .env.example to .env and fill it in."
        )
    return value


def send_email(subject, body, reply_to=None):
    """Send an email.

    Args:
        subject: Subject line.
        body: Plain-text message body (UTF-8 is supported).
        reply_to: Optional address to put in the Reply-To header, e.g. the
            visitor's address when used from a contact form.
    """
    username = _require_env("EMAIL_USERNAME")
    password = _require_env("EMAIL_PASSWORD")
    receiver = os.environ.get("EMAIL_RECEIVER") or username

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = username
    message["To"] = receiver
    if reply_to:
        message["Reply-To"] = reply_to
    message.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(username, password)
        server.send_message(message)
