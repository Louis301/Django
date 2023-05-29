from django.db import models

class NoteFilm(models.Model):

    title        = models.CharField('title', max_length=100) 
    director     = models.CharField('director', max_length=100) 
    genre        = models.CharField('genre', max_length=100) 
    feedback     = models.CharField('feedback', max_length=1000) 
    promo        = models.CharField('promo', max_length=1000) 

    def __str__(self):
        return f"{self.title} ({self.director})"
    


