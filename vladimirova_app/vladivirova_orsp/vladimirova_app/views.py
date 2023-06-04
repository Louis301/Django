from django.shortcuts import render
from .models import Question, epoch_titles, Choice


class Epoch_Questions:
    epoch_title = ''
    questions_list: any

    def __init__(self, epoch_title, questions_list):
        self.epoch_title = epoch_title
        self.questions_list = questions_list


def home(request):
    epoch_titles_local = []

    for i in epoch_titles:
        epoch_titles_local.append(i[1])

    all_questions = []

    for epoch in epoch_titles_local:
        all_questions.append(Epoch_Questions(epoch_title=epoch, questions_list=Question.objects.filter(epoch_title=epoch)))


    Choice.objects.all().update(radiobox_class='answer-inactive')

    verified_questions_category = ''


    for epoch in epoch_titles_local:
        if (request.POST.get(f'send_{epoch}') == 'Проверить'):    

            for i in all_questions:
                if i.epoch_title == epoch:
                    epoch_questions = i
                    break

            for question in epoch_questions.questions_list:
                for choice in question.choice_set.all():
                    if choice.answer_status and request.POST.get(f'{epoch_questions.epoch_title}_{question.id}') != None:
                        Choice.objects.filter(choice_text=choice.choice_text).update(radiobox_class='answer-right')
                    else:
                        if choice.choice_text == request.POST.get(f'{epoch_questions.epoch_title}_{question.id}'):
                            Choice.objects.filter(choice_text=choice.choice_text).update(radiobox_class='answer-wrong')

            verified_questions_category = epoch

    context = {
        'all_questions' : all_questions,
        'epoch_titles' : epoch_titles_local,
        'verified_questions_category' : verified_questions_category,
    }

    return render(request, 'vladimirova_app/home.html/', context)


