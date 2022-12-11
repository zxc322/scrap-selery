import os
from typing import Dict
from celery import Celery

from src.send_mail import MailSender


mail_task = MailSender()
BACKEND_URL = os.environ.get('BACKEND_URL')
BROKER_URL = os.environ.get('BROKER_URL')

app = Celery('mail_task', 
        backend=BACKEND_URL, 
        broker=BROKER_URL
)

@app.task
def task_wrapper(car: Dict, page: str):
    return mail_task.send_email(car, page)