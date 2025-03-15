from django.db import models
from utils.validators import is_greater_than_zero
from users_picpay.models import PicPayUser, UserType
from django.core.exceptions import ValidationError

class Transfer(models.Model):
    value = models.DecimalField(
        decimal_places=2,
        max_digits=11,
        validators=[is_greater_than_zero],
    )
    payer = models.ForeignKey(
        PicPayUser,
        on_delete=models.PROTECT,
        related_name='transfers_made',
    )
    payee = models.ForeignKey(
        PicPayUser,
        on_delete=models.PROTECT,
        related_name='transfers_received',
    )
    reversed_transfer = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        if self.payer.user_type == UserType.SHOPKEEPER:
            raise ValidationError("Usuários lojistas não podem fazer pagamentos.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.payer.fullname} transferiu R${self.value} para {self.payee.fullname}'
