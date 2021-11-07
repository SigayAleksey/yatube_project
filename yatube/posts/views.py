# posts/views.py
from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


#Страницы сообществ
def group_posts(request, slug):
    return HttpResponse(f'Страницы сообществ {slug}')
