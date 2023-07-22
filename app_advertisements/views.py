from django.shortcuts import render
from django.http import HttpResponse
# Функция для отправки html по запросу пользователя
# Create your views here.


def index(requests):
    return render(requests, 'index.html')


def top_sellers(requests):
    return render(requests, 'top-sellers.html')


def advertisement_post(requests):
    return render(requests, 'advertisement-post.html')


def register(requests):
    return render(requests, 'register.html')


def login(requests):
    return render(requests, 'login.html')


def profile(requests):
    return render(requests, 'profile.html')


def exit_(requests):
    return render(requests, 'index.html')


def test(requests):
    return render(requests, 'test.html')


def test2(requests):
    return render(requests, 'test2.html')
