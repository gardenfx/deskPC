# Generated by Django 4.0.4 on 2022-06-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='Photo',
            field=models.ImageField(blank=True, upload_to='../main/static/main/img', verbose_name='Фото'),
        ),
    ]
