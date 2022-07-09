
from django.shortcuts import render,redirect,reverse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import *
from .views import *
from core.model import CuentaUsuario
from .urls import *
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_emailNewEmpleado(mail,idcuentausuario):
   
    cuentaUsuario= CuentaUsuario.objects.get(idcuentausuario=idcuentausuario)
    context={'mail':cuentaUsuario.email,'nombre': cuentaUsuario.nmbusuario,'apellido':cuentaUsuario.apellidousuario,'idusuario':cuentaUsuario.idcuentausuario,'pass':cuentaUsuario.password}
    template = get_template('core/correo/correoNuevoEmpleado.html')
    content= template.render(context)

    email= EmailMultiAlternatives(
        'Nuevo Registro de Empleado',
        'SOPORTE AL MAYOREO 10',
        settings.EMAIL_HOST_USER,
        [mail],

    )
    

    email.attach_alternative(content,'text/html')
    email.fail_silently= False
    email.send()


def send_email(mail,idcuentausuario):
   
    cuentaUsuario= CuentaUsuario.objects.get(rutusuario=idcuentausuario)
    context={'mail':cuentaUsuario.email,'nombre': cuentaUsuario.nmbusuario,'apellido':cuentaUsuario.apellidousuario,'idusuario':cuentaUsuario.rutusuario,'pass':cuentaUsuario.password}
    template = get_template('core/correo/correoNuevoEmpleado.html')
    content= template.render(context)

    email= EmailMultiAlternatives(
        'PRUEBA PDF',
        'SOPORTE AL MAYOREO 10',
        settings.EMAIL_HOST_USER,
        [mail],

    )

    email.attach_alternative(content,'text/html')
    email.attach_file('core/static/doc/pp.pdf')
    email.fail_silently= False
    email.send()


