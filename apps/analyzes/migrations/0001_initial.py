# Generated by Django 5.0.3 on 2024-04-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analyze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_actual', models.BooleanField(default=True, verbose_name='Актуально')),
            ],
        ),
    ]
