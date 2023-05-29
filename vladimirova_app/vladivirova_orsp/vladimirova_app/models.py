from django.db import models

epoch_titles = (
    ('Древняя Русь', 'Древняя Русь'),
    ('Русское государство', 'Русское государство'),
    ('Российская Империя', 'Российская Империя'),
)

class Question(models.Model):
    question_text = models.CharField('Вопрос', max_length=200) 
    epoch_title = models.CharField('Эпоха', max_length=200, choices=epoch_titles) 

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Варианты ответа', max_length=100)
    answer_status = models.BooleanField('Верный ответ', default=False)
    radiobox_class = models.CharField(max_length=100, default='answer-inactive')

    def __str__(self):
        return self.choice_text