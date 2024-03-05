from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from project_django.settings import base

def create_mail(subject, template_name, context):
    template = get_template(template_name)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=base.EMAIL_HOST_USER,
        to=[
            base.EMAIL_HOST_USER
        ],
        cc=[]
    )

    message.attach_alternative(content, 'text/html')
    return message