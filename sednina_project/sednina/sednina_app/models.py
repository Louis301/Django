from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.category})"
    

class Order(models.Model):
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.category})"