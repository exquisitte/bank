import datetime

import random
from pymongo import MongoClient

from random import randint

cluster = "mongodb+srv://timofy:22052009t@cluster0.0jebmyp.mongodb.net/users?retryWrites=true&w=majority"

client = MongoClient(cluster)

db = client.users

bank_users = db.bank_users


def random_card_number(c_user, c_pin):
    random_card = random.randint(1000000000000000, 9999999999999999)
    users_result = bank_users.insert_one({
        "card_number": random_card,
        "card_user": c_user,
        "card_cvv": random.randint(100, 999),
        "card_pin": c_pin,
        "card_date": datetime.datetime.combine(datetime.date.today(), datetime.time.min),
        "card_balance": 0,
    })
    return users_result


def login_card(card_number, money, pin, cvv, date, send_to):
    BU = bank_users.find_one({"card_number": card_number, "card_cvv": cvv, "card_pin": pin, "card_date": date})
    print(BU)
    if BU is not None:
        send_money1(card_number, money, send_to)
    else:

        print("something went wrong")


def send_money1(card_number_sender, send_money, card_to):
    bank = Bank()
    bank.minus_money(card_number_sender, send_money)
    bank.plus_money(send_money, card_to)


class Bank:

    def __init__(self):
        self.collection = db.bank_users


    def minus_money(self, card_number_sender, send_money):
        person = self.collection.find_one({"card_number": card_number_sender})
        bal = person["card_balance"]
        new_money = bal - send_money

        old_values = {"card_number": card_number_sender}
        new_values = {"$set": {"card_balance": new_money}}

        if new_money >= 0:
            self.collection.update_one(old_values, new_values)
        else:
            raise Exception("you don`t have enough money to send")


    def plus_money(self, money, card):
        person = self.collection.find_one({"card_number": card})
        bal = person["card_balance"]
        new_money = bal + money

        old_values = {"card_number": card}
        new_values = {"$set": {"card_balance": new_money}}

        self.collection.update_one(old_values, new_values)
