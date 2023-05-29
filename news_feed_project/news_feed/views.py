from django.shortcuts import render
from news_feed.models import News

section_list = [
    'Экономика',
    'Общество',
    'Армия',
    'Политика',
    'Наука',
    'Спорт',
    'Культура'
]

def index(request, section_item=section_list[0], news_id=None):  

    news_list = News.objects.filter(section=section_item)

    if news_list:
        if news_id == None:
            news_id = news_list[0].id
        select_news = News.objects.get(id=news_id)
    else:
        select_news = []
    
    return render(request, 'index.html', context={ 'news_list' : news_list, 'section_list' : section_list, 'select_section' : section_item, 'select_news' : select_news })

