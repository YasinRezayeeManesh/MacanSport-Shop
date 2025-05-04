from django.db import models
from django_jalali.db import models as jalali_models
from account_module.models import User


# Create your models here.


class ProductCategories(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.SlugField(max_length=100, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    image = models.ImageField(upload_to='images/products', verbose_name='تصویر', null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class ProductCategoriesMain(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=100)
    url_title = models.SlugField(max_length=100, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    image = models.ImageField(upload_to='images/products', verbose_name='تصویر')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی مادر'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    stalk = models.CharField(max_length=100, verbose_name='پایه', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    inventory = models.BooleanField(verbose_name='موجودی')
    description = models.TextField(verbose_name='توضیحات')
    off = models.BooleanField(default=False, verbose_name='تخفیف خورده')
    off_price = models.IntegerField(verbose_name='قیمت تخفیف خورده', null=True, blank=True)
    prc_price = models.IntegerField(verbose_name='درصد تخفیف خورده', null=True, blank=True)
    warranty = models.BooleanField(default=False, verbose_name='گارانتی')
    warranty_time = models.IntegerField(verbose_name='مدت زمان گارانتی', null=True, blank=True)
    color = models.CharField(max_length=100, verbose_name='رنگ', null=True, blank=True)
    size = models.CharField(max_length=100, verbose_name='اندازه', null=True, blank=True)
    brand = models.CharField(max_length=100, verbose_name='شرکت', null=True, blank=True)
    image = models.ImageField(upload_to='images/products', verbose_name='تصویر')
    main_category = models.ForeignKey(ProductCategoriesMain, on_delete=models.CASCADE, verbose_name='دسته بندی مادر',
                                      related_name='product_categories_main', null=True, blank=True)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, verbose_name='دسته بندی',
                                 related_name='product_categories', null=True, blank=True)
    slug = models.SlugField(verbose_name='عنوان در url', db_index=True, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductComment(models.Model):
    product = models.ForeignKey(Product, verbose_name='محصول', on_delete=models.CASCADE)
    parent = models.ForeignKey('ProductComment', null=True, blank=True, verbose_name='والد', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='متن کامنت')
    success = models.BooleanField(verbose_name='تایید شده', default=False)
    shamsi_date = jalali_models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return str(self.user)


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'

    def __str__(self):
        return f'{self.product.title} / {self.ip}'
