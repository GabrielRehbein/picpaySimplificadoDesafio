from decimal import Decimal
from users_picpay.models import PicPayUser


def check_balance(payer: PicPayUser, value: Decimal) -> bool:
    if payer.balance < value:
        return False
    return True
