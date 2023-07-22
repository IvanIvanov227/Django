from django.urls import path
from .views import *

urlpatterns = [
    #path('test2/', test2, name='test2'),
    #path('test/', test, name='test'),
    path('', index, name='index'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('exit_/', exit_, name='#'),
]
