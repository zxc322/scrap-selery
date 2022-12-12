from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel

class Car(BaseModel):
    title: str
    year: int
    price: int
    miliage: Optional[int]
    state_number: Optional[str]
    href: str
    created_at: Optional[datetime]


class Cars(BaseModel):
    cars: List[Car]

