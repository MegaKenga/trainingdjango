# Generated by Django 4.2.7 on 2024-01-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_remove_category_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='children', to='catalog.category', verbose_name='Родительские категории'),
        ),
    ]
