from django.db import models
from users.models import User
from packages.models import Package
from django.db.models.signals import post_save
from django.dispatch import receiver
from application.views import send_notification


class Order(models.Model):
    STATES = [
        ('booked', 'Забронирован'), ('paid', 'Оплачен'), ('confirmed', 'Подтвержден'),
        ('deposit', 'Депосит'), ('trip', 'Отдыхает'), ('cancelled', 'Отменен'),
        ('completed', 'Завершен')
    ]

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name='Клиент')
    package = models.ForeignKey(Package, null=False, on_delete=models.CASCADE, verbose_name='Туристичесуий пакет')
    date_travel = models.DateField(null=False, verbose_name='Дата поездки')
    number_of_tourists = models.IntegerField(null=False, verbose_name='Количество туристов')
    state = models.CharField(null=False, max_length=10, choices=STATES, verbose_name='Статус')
    number_rest_days = models.IntegerField(null=False, verbose_name='Количество дней отпуска')
    price = models.IntegerField(null=True, verbose_name='Цена')

    def __str__(self):
        return f'Заказ № {self.id}'

    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = 'Заказ'


@receiver(post_save, sender=Order)
def update_stock(sender, instance, created, **kwargs):
    if created:
        send_notification.delay(f"В базе данных был создан объект:\n\tКласс модели: {sender} \n\tИмя объекта: {instance}")
