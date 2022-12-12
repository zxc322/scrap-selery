from celery import Celery

from src.telegram_msg import TelegramNotificator
from src.config import TELEGRAM_BROKER_URL


app = Celery(
    "tasks", 
    broker=TELEGRAM_BROKER_URL
    )

telegram = TelegramNotificator()

@app.task
def tg_task_wrapper():
    return telegram.send_message()


app.conf.beat_schedule = {
    "777": {
        "task": "src.tasks.telegram_task.tg_task_wrapper",
        "schedule": 60.0
        }
}