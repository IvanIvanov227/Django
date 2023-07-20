from django.shortcuts import render
from django.http import HttpResponse
# Функция для отправки html по запросу пользователя
# Create your views here.


def index(requests):
    return render(requests, 'index.html')


def test(requests):
    return render(requests, 'test.html')


def test2(requests):
    return render(requests, 'test2.html')
