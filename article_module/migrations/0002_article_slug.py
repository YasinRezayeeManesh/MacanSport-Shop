# Generated by Django 5.1.5 on 2025-02-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='عنوان در url'),
        ),
    ]
