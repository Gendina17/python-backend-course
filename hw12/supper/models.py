from django.db import models


class FunnyWord(models.Model):
    word = models.CharField(null=False, max_length=50, verbose_name='Забавное слово')

    def __str__(self):
        return f'Забавное слово №{self.id}'

    class Meta:
        verbose_name_plural = "Забавные слова"
        verbose_name = 'Забавное слово'
