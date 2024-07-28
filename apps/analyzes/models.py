from django.db import models

# Create your models here.
class Analyze(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=150,
    )
    name_docs = models.CharField(
        verbose_name='Название докторам',
        max_length=150,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    description_docs = models.TextField(
        verbose_name='Описание докторам'
    )
    is_actual = models.BooleanField(
        default=True,
        verbose_name='Актуально',
    )

    def __str__(self):
        return str(self.name)