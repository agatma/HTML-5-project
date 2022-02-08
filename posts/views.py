from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text
    }
    return render(request, 'posts/index.html', context)


def group_posts(request):
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text
    }
    return render(request, 'posts/group_list.html', context)