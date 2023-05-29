from django.db import models


class Users(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    mail = models.CharField('Почта', max_length=40)

    def __str__(self):
        return f"{self.name};{self.phone};{self.mail};"


