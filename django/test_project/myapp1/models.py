from django.db import models


# 1. Создаём таблицу Worker 
class Worker(models.Model):
    # 2. Добавляем поля
    name = models.CharField(max_length=28, blank=False)  # Строковый атрибут, не может быть пустым (2-ой параметр)
    second_name = models.CharField(max_length=35, blank=False) 
    salary = models.IntegerField(default=0)  # Числовой атрибут, по умолчанию равен нулю
    
    # 3. Добавляем методы
    def __str__(self):
        return f"{self.second_name} {self.name}"