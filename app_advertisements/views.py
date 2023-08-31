from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Advertisement
from .forms import AdvertisementForm


# Функция для отправки html по запросу пользователя
def index(requests):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'user': requests.user.is_authenticated}
    return render(requests, 'app_adv/index.html', context)


def top_sellers(requests):
    return render(requests, 'app_adv/top-sellers.html', {'user': requests.user.is_authenticated})


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
            # переброска user на главную страничку, где он сможет увидеть своё объявление
            return redirect(reverse('index'))

    else:
        form = AdvertisementForm()
    errors = (i.strip() for i in form.errors.as_text().split('*') if i.strip())
    res_errors = []
    for i in errors:
        if 'Заголовок не может начинаться' in i:
            res_errors.append("- Заголовок не может начинаться c вопросительного знака\n")

    context = {'form': form, "user": requests.user.is_authenticated, 'error': res_errors}
    return render(requests, 'app_adv/advertisement-post.html', context)
