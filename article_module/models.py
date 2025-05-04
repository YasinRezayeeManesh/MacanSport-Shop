from django.db import models
from django_jalali.db import models as jalali_models

from account_module.models import User


# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    main_title = models.CharField(max_length=200, verbose_name="عنوان اصلی")
    shamsi_date = jalali_models.jDateField(auto_now_add=True, verbose_name="تاریخ شمسی")
    sub_title1 = models.CharField(max_length=200, verbose_name="عنوان اول")
    sub_title2 = models.CharField(max_length=200, verbose_name="عنوان دوم")
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    description1 = models.TextField(verbose_name="توضیحات 1")
    description2 = models.TextField(verbose_name="توضیحات 2")
    description3 = models.TextField(verbose_name="توضیحات 3")
    description4 = models.TextField(verbose_name="توضیحات 4")
    main_image = models.ImageField(upload_to="images/articles", verbose_name="تصویر اصلی")
    image1 = models.ImageField(upload_to="images/articles", verbose_name="تصویر 1")
    image2 = models.ImageField(upload_to="images/articles", verbose_name="تصویر 2")
    image3 = models.ImageField(upload_to="images/articles", verbose_name="تصویر 3")
    quote = models.TextField(verbose_name="نقل قول")
    quote_from = models.CharField(max_length=100, verbose_name="گوینده نقل قول")
    slug = models.SlugField(verbose_name='عنوان در url', unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.name


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    shamsi_date = jalali_models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')
    comment = models.TextField(verbose_name='متن کامنت')
    success = models.BooleanField(default=False, verbose_name="تایید شده")

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return str(self.user)
