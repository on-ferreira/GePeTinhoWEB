from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'myapp'

urlpatterns = [
    path('chat/<int:chat_id>/', views.chat_view, name='chat_view'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('create_msg/', views.create_msg, name='create_msg'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),
    path('delete_chat/', views.delete_chat, name='delete_chat'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),
]
