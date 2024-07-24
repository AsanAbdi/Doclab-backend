from django.db import models

# Create your models here.
class Vacancy(models.Model):
    role = models.CharField(
        max_length=50,
        verbose_name='Роль'
    )
    salary = models.CharField(
        max_length=20,
        default='Договорная',
        verbose_name='Зарплата'
    )
    requirements = models.TextField(
        verbose_name='Требования',
    )
    is_actual = models.BooleanField(
        default=True,
        verbose_name='Актульано'
    )

    def __str__(self):
        return str(self.role)