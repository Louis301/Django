from django.shortcuts import render
from gigachat import GigaChat

authorize_key = 'N2Q5MGI4NTMtZjllMS00OGEwLWExNWItMWJjNDA0N2NkMTQ3OjMxZGYyMjlhLTYwZDItNGE5My04NWRlLWZkNzY1ZDQwOWJlNw=='

def start(request):

    post_data = request.POST
    page_discription = ''
    gigachat_response = ''

    if post_data.get('generate_code') == 'generate code':
        page_discription = post_data.get('page_discription')

        if page_discription:
            with GigaChat(credentials=authorize_key, verify_ssl_certs=False) as giga:
                response = giga.chat('Сгенерируй HTML-код следующей страницы:' + page_discription)
                gigachat_response = response.choices[0].message.content

            with open('./static/page.html', 'w', encoding='utf-8') as fout:
                fout.write(gigachat_response)

    context = {
        'page_discription' : page_discription, 
        'gigachat_response' : gigachat_response,
    }

    return render(request, 'main_app/start.html', context)
