from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterUser


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})


def register_view(request):
    # if request.method == 'POST':
    #     redirect_url = reverse('profile')
    #     form = RegisterUser(request.POST)
    #     if form.is_valid():
    #
    #         username = form.cleaned_data.get('username')
    #         name = form.cleaned_data.get('name')
    #         surname = form.cleaned_data.get('surname')
    #         password = form.cleaned_data.get('password')
    #         password_confirmation = form.cleaned_data.get('password_confirmation')
    #         if password_confirmation == password:
    #
    #     username = request.POST['username']
    #     name = request.POST['name']
    #     surname = request.POST['surname']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect(redirect_url)
    #     return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})
    #
    # if requests.method == 'POST':
    #     form = AdvertisementForm(requests.POST, requests.FILES)
    #     # Если все поля заполнены
    #     if form.is_valid():
    #         # Передаём очищенные данные в форму
    #         advertisement = Advertisement(**form.cleaned_data)
    #         advertisement.user = requests.user
    #         advertisement.save()
    #         # URL-адрес главной странички
    #         url = reverse('index')
    #         # переброска user на главную страничку, где он сможет увидеть своё объявление
    #         return redirect(url)
    # else:
    #     form = AdvertisementForm()
    # context = {'form': form}
    # return render(requests, 'app_adv/advertisement-post.html', context)
    ...


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
