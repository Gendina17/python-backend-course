from django.shortcuts import render
from application import settings
from django.core import mail
from application.celery import app


def index(request):
    return render(request, 'index.html')


def send_email_to_admin(body):
    email = mail.EmailMessage(
        'Notification of the creation of a new object',
        body,
        settings.EMAIL_HOST_USER,
        settings.ADMIN,
    )
    email.send()


@app.task()
def send_notification(body):
    send_email_to_admin(body)
    return 'Email send'