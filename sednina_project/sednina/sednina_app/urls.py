from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
]