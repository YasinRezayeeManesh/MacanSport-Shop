# Generated by Django 5.1.5 on 2025-02-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us_module', '0014_remove_manyinfo_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manyinfo',
            name='card_number',
            field=models.IntegerField(verbose_name='شماره کارت اول'),
        ),
        migrations.AlterField(
            model_name='manyinfo',
            name='card_number2',
            field=models.IntegerField(verbose_name='شماره کارت دوم'),
        ),
    ]
