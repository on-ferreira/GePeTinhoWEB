from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('chat/<int:chat_id>/', views.chat_view, name='chat_view'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('create_msg/', views.create_msg, name='create_msg'),
    path('', views.index, name='index'),
]
