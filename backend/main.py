from fastapi import FastAPI
from backlogic import random_card_number, send_money1, login_card

app = FastAPI()

@app.post("/creating/account")
def card_creating(PIN: str, USER: str):
    rand = random_card_number(USER, PIN)
    return rand

@app.get("/transit")
def send_money(number: int, money: float, number_to: int, cvv: int, date: str, pin: int):
    login_card(number, money, pin, cvv, date, number_to)
    return "works"

@app.get("/account")
def account_checking(number: int, cvv: int, date: str, pin: int):
    login_card(number, None, pin, cvv, date, None, account(number))