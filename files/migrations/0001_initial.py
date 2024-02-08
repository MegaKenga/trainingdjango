# Generated by Django 4.2.7 on 2024-02-05 19:20

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
            ],
            options={
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='ModelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to=files.models.get_upload_path)),
            ],
            options={
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
