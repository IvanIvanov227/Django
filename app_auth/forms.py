from django import forms


class RegisterUser(forms.Form):
    username = forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    name = forms.CharField(max_length=64,
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    surname = forms.CharField(max_length=64,
                              widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password_confirmation = forms.CharField(max_length=64,
                                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
