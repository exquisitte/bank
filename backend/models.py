import datetime

from pydantic import BaseModel

class Users(BaseModel):
    card_number: int
    card_user: str
    card_cvv: int
    card_pin: int
    card_date: datetime.date
    card_balance: int