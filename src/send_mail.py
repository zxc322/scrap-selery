import smtplib
from typing import Dict
from email.mime.text import MIMEText

from src.config import MAIL_SENDER, MAIL_PASSWORD, MAIL_RECIEVER


class MailSender:
        
    def send_email(self, car: Dict, page: str) -> str:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            message = self.create_message(car=car, page=page)
            message = MIMEText(message)
            server.login(MAIL_SENDER, MAIL_PASSWORD)
            message['Subject'] = 'New car was found'
            server.sendmail(MAIL_SENDER, MAIL_RECIEVER, message.as_string())
            return 'Mail was successfully sent'
        except Exception as ex:
            return f'Mail was not sent because of [ERROR]: {ex}'
    

    def create_message(self, car: Dict, page: str) -> str:
        message = f'The most expensive car on page №{page}\n\
                Title: {car.get("title")}\n\
                Year: {car.get("year")}\n\
                Price: {car.get("price")}\n\
                Miliage: {car.get("miliage")}\n\
                State number: {car.get("state_number")}\n\
                href: {car.get("href")}\n\
                was found at {car.get("created_at")}'

        return message



