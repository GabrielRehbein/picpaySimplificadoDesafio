from django.db import models
from django.core.validators import RegexValidator
from utils.validators import validate_if_value_is_positive

class UserType(models.TextChoices):
    NORMAL = 'N', 'Normal'
    SHOPKEEPER = 'S', 'Lojista'


class PicPayUser(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(
        max_length=100,
        choices=UserType,
        default=UserType.NORMAL
    )
    document = models.CharField(max_length=14, unique=True)
    balance = models.DecimalField(
        decimal_places=2,
        max_digits=11,
        default=0,
        validators=[validate_if_value_is_positive]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.user_type == UserType.NORMAL:
            validator = RegexValidator(
                regex='^[0-9]{11}$',
                message='CPF inválido. Deve conter 11 números.'
            )
            validator(self.document)

        elif self.user_type == UserType.SHOPKEEPER:
            validator = RegexValidator(
                regex='^[0-9]{8}0001[0-9]{2}$',
                message='CNPJ inválido. Deve conter 14 números e seguir o padrão.'
            )
            validator(self.document)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['fullname']
    
    def __str__(self):
        return f'{self.fullname} | {self.document}'

