from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transfer
from services.notify import NotifyService


@receiver(post_save, sender=Transfer)
def send_payment_received_email(sender, instance: Transfer, created, **kwargs):
    try:
        notify_client = NotifyService()
        value = instance.value
        payee= instance.payee
        email_to = payee.email
        payload = {
        "from": {"email": "noreply@picpay.com", "name": "PicPay"},
        "to": [{"email": f"{email_to}"}],
        "subject": "Transferência",
        "text": f"Você recebeu R${value}!",
        }
        response_status_code = notify_client.notify_by_email(payload)
        if response_status_code != 204:
            print('Algo deu errado ao envio do email.')
        elif response_status_code == 204:
            print('Email enviado.')
    except:
        pass
