# Generated by Django 4.2.7 on 2024-01-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='slug',
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=128, unique=True, verbose_name='url-адрес'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=128, unique=True, verbose_name='url-адрес'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='slug',
            field=models.SlugField(max_length=128, unique=True, verbose_name='url-адрес'),
        ),
    ]