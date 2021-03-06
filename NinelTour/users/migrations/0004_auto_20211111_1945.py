# Generated by Django 3.2.8 on 2021-11-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211111_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='2001-01-01', verbose_name='Дата рождения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужчина'), ('w', 'Женщина')], default='w', max_length=1, verbose_name='Пол'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='passport_number',
            field=models.CharField(default='111111', max_length=6, verbose_name='Номер паспорта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, null=True, verbose_name='Телефонный номер'),
        ),
    ]
