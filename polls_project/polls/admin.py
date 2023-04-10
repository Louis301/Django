# from django.contrib import admin

# from .models import Question, Choice


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Формулировка', {'fields': ['question_text']}),  # элем1: имя группы полей для пользователя (None, если поле одно), элем2: набор полей
#         ('Информация по дате', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Question, QuestionAdmin)  
# admin.site.register(Choice)  

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):  # Базовый класс определяет режим отображения элементов Choice
    model = Choice
    extra = 3  # Количество элементов Choice на странице admin


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)