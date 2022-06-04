
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import *

def send_email(mail):
    context={'mail':mail}

    template = get_template('core/correo/correo.html')
    content= template.render(context)

    email= EmailMultiAlternatives(
        'Un correo de prueba',
        'Mensaje Correo',
        settings.EMAIL_HOST_USER,
        [mail],

    )

    email.attach_alternative(content,'text/html')
    email.fail_silently= False
    email.send()

def correoP(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)
    return render(request,'core/correo/correoPrueba.html',{})