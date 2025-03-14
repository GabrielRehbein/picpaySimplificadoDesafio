from django.db import models
from django.core.validators import RegexValidator
from utils.validators import valid_if_value_is_positive
class UserPicPay(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(
        decimal_places=2,
        max_digits=11,
        default=0,
        validators=[valid_if_value_is_positive]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


def help_text_message():
    return 'Use only numbers'


class ShopKeeper(UserPicPay):
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        validators=[RegexValidator(
            regex='^[0-9]{8}0001[0-9]{2}$',
            message='CNPJ invalid. Use the format: 99999999000100'
        )],
        help_text=help_text_message()
    )

    def __str__(self):
        return f'{self.fullname} | {self.cnpj}'


class Customer(UserPicPay):
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(
            regex='^[0-9]{11}$',
            message='CPF invalid. Use the format: 12345678901'
        )],
        help_text=help_text_message()
    )

    def __str__(self):
        return f'{self.fullname} | {self.cpf}'
