# Generated by Django 5.0.7 on 2024-07-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyze',
            name='description_docs',
            field=models.TextField(default=0, verbose_name='Описание докторам'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analyze',
            name='name_docs',
            field=models.CharField(default=1, max_length=150, verbose_name='Название докторам'),
            preserve_default=False,
        ),
    ]
