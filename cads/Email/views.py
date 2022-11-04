
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader
from . models import SendEmail
from django.urls import reverse
from . models import Register


def index(request):
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({}, request))



def email(request):
    
    send_mail("Testando", "Testando se funciona enviar email pelo Django", "santoseduardolourenco@gmail.com", ['cursopedrolou@gmail.com', 'ph352471@gmail.com'])
    
    return HttpResponse("Olá mundo")


def send(request):
    name = request.POST['name']
    
    subject = request.POST['subject']
    
    message = request.POST['message']

    sendEmail = SendEmail(name = name, subject = subject, message = message)
    
    sendEmail.save()

    message =  "Nome: " + name + " \n" + message

    send_mail(subject, message, "santoseduardolourenco@gmail.com", ['cursopedrolou@gmail.com', 'ph352471@gmail.com'])

    return HttpResponseRedirect(reverse('index'))


def register_users(request):
    
    template = loader.get_template('register.html')
    
    return HttpResponse(template.render({}, request))


def add_registration(request):

    name = request.POST['name']
    
    years = request.POST['years']
    
    state = request.POST['state']
    
    district = request.POST['district']
    
    email = request.POST['email']

    first_subject = "Pedidos de membro em analise"

    register = "Os nosso membros estão analisando seus dados e logo entraremos encontato."

    send_mail(first_subject, register, "santoseduardolourenco@gmail.com", [email])

    if(int(years) >= 18):

        registration = Register(name = name, years = years, state = state, district = district, email = email)
        
        registration.save()

        subject = "Analise de novo membro"

        message = "nome  "+name + " \n" + "Idade "+years + " \n" +"Estado " +state + " \n" + "Bairro "+district+ "\n "+ "Email " + email+" \n"

        for element in registration:
            
            send_mail(subject, message, "santoseduardolourenco@gmail.com", [element.email])
        
        return HttpResponseRedirect(reverse('index'))
    