from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement

        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                            'id': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg',
                                                 'id': 'description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg',
                                              'id': 'price'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input',
                                                  'id': 'auction'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg',
                                            'id': 'image'})
        }
