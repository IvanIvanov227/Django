from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Advertisement
from .forms import AdvertisementForm


# Функция для отправки html по запросу пользователя
def index(requests):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(requests, 'app_adv/index.html', context)


def top_sellers(requests):
    return render(requests, 'app_adv/top-sellers.html')


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(requests):
    if requests.method == 'POST':
        form = AdvertisementForm(requests.POST, requests.FILES)
        # Если все поля заполнены
        if form.is_valid():
            # Передаём очищенные данные в форму
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = requests.user
            advertisement.save()
            # URL-адрес главной странички
            url = reverse('index')
            # переброска user на главную страничку, где он сможет увидеть своё объявление
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(requests, 'app_adv/advertisement-post.html', context)


def register(requests):
    return render(requests, 'app_auth/register.html')


def login(requests):
    return render(requests, 'app_auth/login.html')


def profile(requests):
    return render(requests, 'app_auth/profile.html')


def exit_(requests):
    return render(requests, 'app_adv/index.html')
