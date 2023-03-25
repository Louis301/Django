from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):

	all_workers = Worker.objects.all()  # Получение всех записей модели Worker

	# for i in all_workers:
	# 	print(i.id, i.name, i.second_name, i.salary)

	return render(request, 'index.html', context={'data' : all_workers})