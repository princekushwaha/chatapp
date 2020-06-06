
from django.urls import path, include, re_path
from .views import index, room

urlpatterns = [

    path('', index, name = 'index'),
    path('<str:room_name>/', room, name = 'room')

]