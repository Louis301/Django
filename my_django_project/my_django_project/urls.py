from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book', views.add_book, name='add_book'),
    path('book_list', views.show_book_list, name='book_list'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
]



