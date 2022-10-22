from django.conf import settings
from django.core.mail import EmailMessage

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import onde_ficar

# Create your views here.

def home(request):
    if request.method == 'GET':
        #administração User:admin Senha:admin
        onde = onde_ficar.objects.all()
        context ={
            'onde':onde,
        }
        return render(request, 'home/index.html', context)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        inst = request.POST.get('instagram')
        mensagem = request.POST.get('mensagem')

        #eviar o email
        email = EmailMessage(
            'Nova mensagem',
            f'nome:{name}\n \n email:{email}\n \n teçefone:{tel}\n \n instagram:{inst}\n \n Mensagem: {mensagem}',
            settings.EMAIL_HOST_USER,
            ['klebersonfialhobaleeiro@gmail.com']
        )
        email.fail_silently = True
        email.send()

        messages.add_message(request, messages.SUCCESS, 'Mensagem enviada')
        return redirect(reverse('home'))