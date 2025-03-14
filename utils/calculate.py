from users_picpay.models import Customer, ShopKeeper
from decimal import Decimal


def calculate_balance(customer: Customer, shopkeeper: ShopKeeper, value: Decimal):
    customer.balance -= value
    shopkeeper.balance += value
