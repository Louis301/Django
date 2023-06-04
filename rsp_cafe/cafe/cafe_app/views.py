from django.shortcuts import render
from .models import Dish

# Create your views here.

def home(request):

    first_courses = Dish.objects.filter(category='Первые блюда')
    salads = Dish.objects.filter(category='Салаты')
    drinks = Dish.objects.filter(category='Напитки')


    context = {
        'first_courses' : first_courses,
        'salads' : salads,
        'drinks' : drinks
    }

    return render(request, 'home.html', context)



