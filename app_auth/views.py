from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterUser


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    context = {'is_user': request.user.is_authenticated, 'user': request.user}
    return render(request, 'app_auth/profile.html', context)


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        else:
            context = {'user': request.user.is_authenticated}
            return render(request, 'app_auth/login.html', context)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    context = {'error': 'Пользователь не найден', 'user': request.user.is_authenticated}
    return render(request, 'app_auth/login.html', context)


def register_view(requests):
    if requests.method == 'POST':
        form = RegisterUser(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(requests, user)
            return redirect(reverse('profile'))
        else:
            errors = (i.strip() for i in form.errors.as_text().split('*') if i.strip())
            res_errors = []
            for i in errors:
                if i == 'A user with that username already exists.':
                    res_errors.append("- Пользователь с таким именем пользователя уже существует\n")
                elif i == 'This password is too short. It must contain at least 8 characters.':
                    res_errors.append('- Минимальная длина пароля - 8 символов\n')
                elif i == 'This password is too common.':
                    res_errors.append('- Этот пароль слишком распространен\n')
                elif i == 'This password is entirely numeric.':
                    res_errors.append('- Пароль не должен состоять только из цифр\n')
                elif i == "The two password fields didn’t match.":
                    res_errors.append('- Пароли не совпадают\n\n')
            context = {'error': res_errors, 'user': requests.user.is_authenticated,
                       'form': form}
            return render(requests, 'app_auth/register.html', context)
    else:
        form = RegisterUser()
    context = {"user": requests.user.is_authenticated, "form": form}
    return render(requests, 'app_auth/register.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
