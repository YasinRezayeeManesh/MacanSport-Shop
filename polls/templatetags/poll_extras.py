from django import template


register = template.Library()


@register.filter('three_digits_currency')
def three_digits_currency(value):
    return ' {: ,} '.format(value) + ' تومان '


@register.filter('four_digits_currency')
def four_digits_currency(value):
    value = str(value)
    return '-'.join([value[i:i+4] for i in range(0, len(value), 4)])
