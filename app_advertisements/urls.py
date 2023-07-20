from django.urls import path
from .views import index, test, test2

urlpatterns = [
    path('test2/', test2, name='test2'),
    path('', test, name='test'),
    #path('', index),
]
