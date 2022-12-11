from fastapi import APIRouter

from src.database import Database
from src.scraper import Scraper
from src.tasks.mail_task import task_wrapper
from src.schemas import Car, Cars

router = APIRouter()

@router.get('/page/', response_model=Car)
def get_cars_from_page(page: str = None) -> Car:
    url="https://auto.ria.com/uk/car/used/"
    if page:
        url += f"?page={page}"
    scraper = Scraper(url=url)
    cars_list = scraper.scrap_all_cars_on_page()
    most_expensive_car = scraper.find_most_expensive_car(cars=cars_list)
    task_wrapper.delay(car=most_expensive_car, page=page)
    Database().insert_cars(cars=cars_list) 
    return Car(**most_expensive_car)


@router.get('/top', response_model=Cars)
def get_top_cars(limit: int = 3) -> Cars:
    return Database().get_top_expensives_cars(limit=limit)





    
    