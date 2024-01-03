# Generated by Django 4.2.7 on 2024-01-02 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_brand_description_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='catalog.category', verbose_name='Категории, к которым принадлежит группа товаров'),
        ),
    ]