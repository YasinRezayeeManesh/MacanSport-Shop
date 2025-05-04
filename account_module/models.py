from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name="تصویر پروفایل")
    mobile = models.CharField(max_length=11, verbose_name='شماره تماس', unique=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)
    about_user = models.TextField(verbose_name='درباره شخص', default='')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
