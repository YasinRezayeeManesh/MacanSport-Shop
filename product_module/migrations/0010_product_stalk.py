# Generated by Django 5.1.5 on 2025-03-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_productvisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stalk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='پایه'),
        ),
    ]
