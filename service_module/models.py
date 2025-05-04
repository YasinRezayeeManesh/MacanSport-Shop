from django.db import models

# Create your models here.


class Service(models.Model):
    home_img = models.ImageField(upload_to='images/service', verbose_name='تصویر صفحه اصلی', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="نام")
    short_description = models.CharField(max_length=200, verbose_name="توضیحات کوتاه")
    main_image = models.ImageField(upload_to='images/service', verbose_name="تصویر اصلی")
    title_1 = models.CharField(max_length=100, verbose_name="عنوان اول")
    title_2 = models.CharField(max_length=100, verbose_name="عنوان دوم")
    title_3 = models.CharField(max_length=100, verbose_name="عنوان سوم")
    title_4 = models.CharField(max_length=100, verbose_name="عنوان چهارم")
    description_1 = models.TextField(verbose_name="توضیحات اول")
    description_2 = models.TextField(verbose_name="توضیحات دوم")
    description_3 = models.TextField(verbose_name="توضیحات سوم")
    description_4 = models.TextField(verbose_name="توضیحات چهارم")
    image = models.ImageField(upload_to='images/service', verbose_name="تصویر")
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url', db_index=True, default='')

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.name
