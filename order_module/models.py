from django.db import models
from account_module.models import User
from django_jalali.db import models as jalali_models
from product_module.models import Product
from about_us_module.models import ManyInfo


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده')
    is_close = models.BooleanField(default=False, verbose_name='بسته شده')
    date_paid = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    post_paid = models.IntegerField(null=True, blank=True, verbose_name='هزینه پستی', default=50000)

    def post_price(self):
        post_price = 0
        post_price += self.post_paid
        return post_price

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
        if total_amount > 0:
            total_amount += self.post_paid

        return total_amount

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبد های خرید'

    def __str__(self):
        return str(self.order)
