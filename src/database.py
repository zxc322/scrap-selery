import os
from typing import List
from pymongo import MongoClient
from dotenv import load_dotenv

from src.schemas import Cars

load_dotenv()
MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_PORT = os.environ.get('MONGO_PORT')


class Database:

    def __init__(self) -> None:
        self.client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@mongo:{MONGO_PORT}/')
        self.db = self.client.auto_ria
        self.collection = self.db.autos

    
    def insert_cars(self, cars: List):
        for car in cars:
            if not self.get_car_by_href(href=car.get('href')):
                self.collection.insert_one(car).inserted_id


    def get_top_expensives_cars(self, limit: int):
        top_cars = self.collection.find().sort("price", -1).limit(limit)
        return Cars(cars=[dict(s) for s in top_cars])

        

    def get_car_by_href(self, href: str) -> List:
        car = self.collection.find({"href": href})
        return list(car)


