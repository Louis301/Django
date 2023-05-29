from django.shortcuts import render
from .models import Users

def index(request):
    if request.POST.get('send') == 'Отправить':
        Users.objects.create(
            name=request.POST.get('user_name'),
            phone=request.POST.get('user_phone'),
            mail=request.POST.get('user_mail'),
        )
    return render(request, 'savvinova_app/index.html')


def about(request):
    return render(request, 'savvinova_app/about.html')


def program(request):
    return render(request, 'savvinova_app/program.html')


