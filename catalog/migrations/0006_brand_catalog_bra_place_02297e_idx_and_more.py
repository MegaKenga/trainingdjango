# Generated by Django 4.2.7 on 2024-04-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_categoryimage_category_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='brand',
            index=models.Index(fields=['place'], name='catalog_bra_place_02297e_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['place'], name='catalog_cat_place_bdac70_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['brand'], name='catalog_cat_brand_i_cc684c_idx'),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['place'], name='catalog_off_place_0c9311_idx'),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['category'], name='catalog_off_categor_a4ac70_idx'),
        ),
    ]
