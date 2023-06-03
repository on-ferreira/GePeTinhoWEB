from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('chat/<int:chat_id>/', views.chat_view, name='chat_view'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('create_msg/', views.create_msg, name='create_msg'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),
    path('delete_chat/', views.delete_chat, name='delete_chat'),
    path('', views.index, name='index'),
]
