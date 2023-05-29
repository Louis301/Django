from django.shortcuts import render
from .models import NoteFilm


def main(request):
    return render(request, 'main.html')


def adding(request):
    if request.POST.get('add_note') == 'Сохранить':

        NoteFilm.objects.create(
            title        = request.POST.get('film_title'),
            director     = request.POST.get('film_director'), 
            genre        = request.POST.get('film_genre'), 
            feedback     = request.POST.get('film_feedback'), 
            promo        = request.POST.get('film_promo')
        )

    return render(request, 'adding.html')


def notes(request):

    all_notes = NoteFilm.objects.all()

    context = {
        'all_notes' : all_notes
    }

    return render(request, 'notes.html', context)



