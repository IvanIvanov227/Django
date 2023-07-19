from django.shortcuts import render
# Функция для отправки html по запросу пользователя
from django.http import HttpResponse
# Create your views here.


def index(requests):
    return HttpResponse('Успешно')
