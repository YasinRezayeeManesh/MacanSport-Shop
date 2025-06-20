# Generated by Django 5.1.5 on 2025-02-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('price', models.FloatField(verbose_name='قیمت')),
                ('inventory', models.BooleanField(verbose_name='موجودی')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
