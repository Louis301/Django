from django.db import models


class Dish(models.Model):
    category = models.CharField('Категория', max_length=600)
    title = models.CharField('Наименование', max_length=600)
    price = models.FloatField('Цена')

    def __str__(self):
        return f"{self.title} ({self.category})"
    


    