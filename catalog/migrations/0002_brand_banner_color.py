# Generated by Django 4.2.7 on 2024-06-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='banner_color',
            field=models.CharField(default='#005d9c', max_length=32, verbose_name='Цвет баннера бренда'),
        ),
    ]
