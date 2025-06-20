# Generated by Django 5.1.5 on 2025-03-11 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0014_product_prc_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoriesMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url_title', models.SlugField(max_length=100, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی مادر',
            },
        ),
        migrations.AddField(
            model_name='productcategories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_categories_main', to='product_module.productcategoriesmain', verbose_name='دسته بندی مادر'),
        ),
    ]
