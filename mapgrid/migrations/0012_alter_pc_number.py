# Generated by Django 4.0.4 on 2022-06-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapgrid', '0011_alter_pc_id_pc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='Number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Номер ПК'),
        ),
    ]
