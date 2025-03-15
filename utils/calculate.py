from users_picpay.models import PicPayUser
from decimal import Decimal


def calculate_balance(payer: PicPayUser, payee: PicPayUser, value: Decimal):
    payer.balance -= value
    payee.balance += value

def reverse_transfer(payer: PicPayUser, payee: PicPayUser, value: Decimal):
    payer.balance += value
    payee.balance -= value
