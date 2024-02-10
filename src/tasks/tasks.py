import smtplib
from email.message import EmailMessage

from celery import Celery
from src.config import SMTP_USER, SMTP_PASSWORD, REDIS_HOST, REDIS_PORT

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery("tasks", broker=f'redis://{REDIS_HOST}:{REDIS_PORT}/0')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'TestLetter'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER
    
    with open('src/tasks/message_to_user.html', 'r', encoding='utf-8') as html_file:
        source_code = html_file.read()
        email.set_content(
            source_code,
            subtype='html'
            )
    return email
        

@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)