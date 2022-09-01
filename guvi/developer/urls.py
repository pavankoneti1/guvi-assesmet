from django.urls import path
from .views import *
urlpatterns =[
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('edit/', edit, name='edit'),
    path('task/', TaskList, name='task'),
    path('profile/<int:pk>/>',profile, name='profile'),
    # path('signup/addrecord/', addrecord, name='addrecord'),
    # path('add/', addrecord, name='add'),
    # path('edit/<int:pk>/', edit.as_view(), name='edit')
]