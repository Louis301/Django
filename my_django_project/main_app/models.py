from django.db import models


# all_book_titles = set()


class Book(models.Model):
    title =           models.CharField(max_length=100)
    author =          models.CharField(max_length=100)
    discription =     models.CharField(max_length=400)
    style =           models.CharField(max_length=200)
    age_restriction = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}\n({self.author})\n{self.discription}\n{self.style}\n{self.age_restriction}"

    