import os
from typing import Dict
import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""
    sg = sendgrid.SendGridAPIClient(api_key = os.environ.get("SENDGRID_API_KEY"))
    from_email = Email(os.environ.get("FROM_EMAIL"))
    to_email = To(os.environ.get("TO_EMAIL"))
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    try:
        response = sg.client.mail.send.post(request_body = mail)
        print("Email response", response.status_code)
        if response.status_code == 202:
            return {"status": "success"}
        else:
            return {"status": "failed", "code": response.status_code, "body": response.body}
    except Exception as e:
        print("Email send exception:", e)
        return {"status": "error", "message": str(e)}

INSTRUCTIONS = """You have the ability to send a professionally formatted HTML email.
When provided with a detailed report, convert it into clean, well-structured, and visually appealing HTML.
Choose an appropriate subject line, then use your tool to send exactly one email containing the formatted report."""

mailer_agent = Agent(
    name = "MailerAgent",
    instructions = INSTRUCTIONS,
    tools = [send_email],
    model = "gpt-4o-mini",
)