from typing import Dict
from celery import Celery

from src.send_mail import MailSender
from src.config import MAIL_BROKER_URL




app = Celery(
        'mail_task',  
        broker=MAIL_BROKER_URL
)

mail_task = MailSender()

@app.task
def task_wrapper(car: Dict, page: str):
    return mail_task.send_email(car, page)