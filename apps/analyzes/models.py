from django.db import models

# Create your models here.
class Analyze(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=150,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    is_actual = models.BooleanField(
        default=True,
        verbose_name='Актуально',
    )