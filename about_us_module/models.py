from django.db import models


# Create your models here.


class AboutUs(models.Model):
    home_service_img = models.ImageField(upload_to='images/about_us', verbose_name="تصویر خدمات صفحه خانه", null=True, blank=True)
    home_image = models.ImageField(upload_to="images/about_us", verbose_name="تصویر صفحه خانه", null=True, blank=True)
    home_title = models.CharField(max_length=100, verbose_name='عنوان صفحه خانه', default='')
    home_description = models.TextField(verbose_name='توضیحات صفحه خانه', default='')
    main_title = models.CharField(max_length=200, verbose_name='عنوان اصلی')
    info_title = models.CharField(max_length=200, verbose_name='عنوان اطلاعات')
    info_description = models.TextField(verbose_name='توضیحات اطلاعات')
    info_image = models.ImageField(upload_to='images/about_us', verbose_name='تصویر اطلاعات')
    work_title = models.CharField(max_length=200, verbose_name='عنوان کار ما')
    work_description = models.TextField(verbose_name='توضیحات کار ما')
    work_image = models.ImageField(upload_to='images/about_us', verbose_name='تصویر کار ما')
    wholesale_sales_perc = models.FloatField(verbose_name='درصد فروش عمده')
    single_sales_perc = models.FloatField(verbose_name='درصد تک فروش')
    installation_and_repairs_perc = models.FloatField(verbose_name='درصد نصب و تعمیرات')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return "درباره ما"


class Companies(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام نمایندگی')
    image = models.ImageField(upload_to='images/about_us', verbose_name='تصویر نمایندگی')

    class Meta:
        verbose_name = 'نمایندگی'
        verbose_name_plural = 'نمایندگی ها'

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    site_name = models.CharField(verbose_name='نام سایت', max_length=100, default='')
    site_logo = models.ImageField(upload_to='images/logo', verbose_name='لوگو سایت', null=True, blank=True)
    name = models.CharField(verbose_name='نام', max_length=100)
    telegram = models.CharField(verbose_name='آیدی تلگرام', max_length=100, null=True, blank=True)
    instagram = models.CharField(verbose_name='آیدی اینستاگرام', max_length=100, null=True, blank=True)
    whatsapp = models.CharField(verbose_name='شماره واتساپ', max_length=100, null=True, blank=True)
    mobile1 = models.CharField(max_length=100, verbose_name='شماره تماس اول')
    mobile2 = models.CharField(max_length=100, verbose_name='شماره تماس دوم', null=True, blank=True)
    mobile3 = models.CharField(max_length=100, verbose_name='شماره تماس سوم', null=True, blank=True)
    email = models.CharField(verbose_name='آدرس ایمیل', max_length=100, null=True, blank=True)
    address = models.CharField(verbose_name='آدرس مغازه', max_length=200)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.name


class FrequentlyQuestions(models.Model):
    question = models.CharField(verbose_name='سوال', max_length=200)
    answer = models.TextField(verbose_name='جواب')

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات متداول'

    def __str__(self):
        return self.question


class Team(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    job = models.CharField(max_length=200, verbose_name='وظیفه شغلی')
    image = models.ImageField(upload_to='images/team', verbose_name='تصویر پروفایل', null=True, blank=True)

    class Meta:
        verbose_name = 'عضو تیم'
        verbose_name_plural = 'اعضای تیم'

    def __str__(self):
        return 'تیم'


class ManyInfo(models.Model):
    site_logo = models.ImageField(upload_to='images/logo', verbose_name='لوگو سایت', null=True, blank=True)
    card_number = models.CharField(verbose_name='شماره کارت اول', default='', max_length=200)
    shaba_card_number = models.CharField(verbose_name='شماره شبا کارت اول', max_length=200)
    owner_card_number = models.CharField(verbose_name='صاحب شماره کارت اول', max_length=200)

    class Meta:
        verbose_name = 'اطلاعات'
        verbose_name_plural = "اطلاعات بانکی"

    def __str__(self):
        return 'اطلاعات بانکی'
