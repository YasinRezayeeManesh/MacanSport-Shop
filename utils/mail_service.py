from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


def send_email(subject, to, context, template_name):
    try:
        html_massage = render_to_string(template_name, context)
        plain_massage = strip_tags(html_massage)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_massage, from_email, [to], html_message=html_massage)

    except:
        pass
