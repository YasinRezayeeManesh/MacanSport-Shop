# Generated by Django 5.1.5 on 2025-02-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'درباره ما', 'verbose_name_plural': 'درباره ما'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='companies_image',
            field=models.ImageField(upload_to='images/about_us', verbose_name='تصویر نمایندگی ها'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='info_description',
            field=models.TextField(verbose_name='توضیحات اطلاعات'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='info_image',
            field=models.ImageField(upload_to='images/about_us', verbose_name='تصویر اطلاعات'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='info_title',
            field=models.CharField(max_length=200, verbose_name='عنوان اطلاعات'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='installation_and_repairs_perc',
            field=models.FloatField(verbose_name='درصد نصب و تعمیرات'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='main_title',
            field=models.CharField(max_length=200, verbose_name='عنوان اصلی'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='single_sales_perc',
            field=models.FloatField(verbose_name='درصد تک فروش'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='wholesale_sales_perc',
            field=models.FloatField(verbose_name='درصد فروش عمده'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='work_description',
            field=models.TextField(verbose_name='توضیحات کار ما'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='work_image',
            field=models.ImageField(upload_to='images/about_us', verbose_name='تصویر کار ما'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='work_title',
            field=models.CharField(max_length=200, verbose_name='عنوان کار ما'),
        ),
    ]
