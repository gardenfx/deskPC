# Generated by Django 4.0.4 on 2022-05-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('ID_PC', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.CharField(max_length=20, unique=True, verbose_name='Статус')),
                ('Stoim', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'ПК',
                'verbose_name_plural': 'ПК',
                'db_table': 'mapgrid',
            },
        ),
    ]
