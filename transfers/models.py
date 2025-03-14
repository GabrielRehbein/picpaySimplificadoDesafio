from django.db import models
from utils.validators import is_greater_than_zero
from users_picpay.models import Customer, ShopKeeper


class Transfer(models.Model):
    value = models.DecimalField(
        decimal_places=2,
        max_digits=11,
        validators=[is_greater_than_zero]
    )
    payer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    payee = models.ForeignKey(ShopKeeper, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.payer.fullname} transferiu R${self.value} para {self.payee.fullname}'