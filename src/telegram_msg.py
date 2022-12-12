import httpx

from src.database import Database
from src.config import TOKEN, CHAT_ID



class TelegramNotificator:

    def __init__(self) -> None:
        self.token = TOKEN
        self.chat_id = CHAT_ID
        self.database = Database()

    
    def create_message(self) -> str:
        message = str()
        cars = self.database.get_top_expensives_cars(limit=3)
        top = 1
        for car in cars.cars:
            message += f"Car-{top}\n"
            message += f"title: {car.title}\n"
            message += f"year: {car.year}\n"
            message += f"price: {car.price} $\n"
            message += f"mileage: {car.miliage} km\n"
            message += f"state-number: {car.state_number}\n"
            # message += f"href: {car.href}\n"
            message += f"created: {car.created_at}\n\n"
            top += 1

        return message

    
    def send_message(self) -> None:
        message = self.create_message()

        print('message', type(message), '\n',  message)
        url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}".format(
            self.token, self.chat_id, message
        )
        return httpx.get(url=url).json()


