from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=50,
        unique=True
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=2000
    )
    date = models.DateField(
        auto_now=True,
        verbose_name='Дата создания'
    )