
from celery import shared_task
from django.core.mail import send_mail
from send_message import settings

@shared_task
def send_welcome_email(email):
    subject = 'Добро пожаловать!'
    message = 'Спасибо за подписку на наши обновления!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    return send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )
