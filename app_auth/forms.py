from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterUser(UserCreationForm):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                             'type': 'text',
                                                             'name': 'username',
                                                             'autocomplete': 'username',
                                                             'placeholder': 'Никнейм вашего аккаунта'}))
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                         'type': 'text',
                                                         'name': 'name',
                                                         'autocomplete': 'name',
                                                         'placeholder': 'Ваше имя'}))
    surname = forms.CharField(max_length=20,
                              widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                            'type': 'text',
                                                            'name': 'surname',
                                                            'autocomplete': 'surname',
                                                            'placeholder': 'Ваша фамилия'}))
    password1 = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                              'type': 'password',
                                                              'name': 'password',
                                                              'autocomplete': 'new-password',
                                                              'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                              'type': 'password',
                                                              'name': 'password2',
                                                              'autocomplete': 'new-password',
                                                              'placeholder': 'Повторно введите пароль'}))
