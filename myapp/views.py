from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Chat, Message
from django.urls import reverse
import requests
from urllib.parse import urljoin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('myapp:login'))  # Redirect to the login page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect(reverse('myapp:login'))
    else:
        return redirect(reverse('myapp:index'))

@login_required
def index(request):
    user = request.user  # Retrieve the logged-in user
    chats = Chat.objects.all()
    context = {'chats': chats, 'user': user}  # Add 'user' to the context
    return render(request, 'index.html', context)


@login_required
def chat_view(request, chat_id):
    chats = Chat.objects.all()
    chat = Chat.objects.get(pk=chat_id)
    messages = Message.objects.filter(chat=chat)
    context = {'chats': chats, 'chat': chat, 'messages': messages}
    return render(request, 'chat_detail.html', context)


@login_required
def create_chat(request):
    if request.method == 'POST':
        user = request.user  # Retrieve the logged-in user
        chat = Chat.objects.create(user = user)
        return redirect(reverse('myapp:chat_view', kwargs={'chat_id': chat.pk}))
    else:
        return render(request, 'create_chat.html')


@login_required
def create_msg(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        chat_input = request.POST.get('chat_input')
        sender = 'user'
        typeofMessage = 'text'

        # Retrieve the chat object based on chat_id
        chat = Chat.objects.get(pk=chat_id)

        # Create the message object with the provided data
        Message.objects.create(chat=chat, content=chat_input, sender=sender, typeofMessage=typeofMessage)

        # Fetch the JSON data from the URL
        response = requests.get('https://cataas.com/cat/gif?json=true')
        json_data = response.json()

        # Extract the image URL from the JSON data
        base_url = 'https://cataas.com'
        image_url = json_data['url']

        Message.objects.create(chat=chat, content=urljoin(base_url, image_url), sender="system", typeofMessage='img_url')
        Message.objects.create(chat=chat, content="Meow Meow Moew", sender="system", typeofMessage=typeofMessage)

        return redirect(reverse('myapp:chat_view', kwargs={'chat_id': chat.pk}))
    else:
        return render(request, 'create_msg.html')


@login_required
def clear_chat(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        # Retrieve the chat object based on chat_id
        chat = Chat.objects.get(pk=chat_id)
        # Delete the messages with the matching chat_id
        Message.objects.filter(chat_id=chat.pk).delete()

        return redirect(reverse('myapp:chat_view', kwargs={'chat_id': chat.pk}))
    else:
        return render(request, 'create_chat.html')


@login_required
def delete_chat(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        # Retrieve the chat object based on chat_id
        chat = Chat.objects.get(pk=chat_id)
        # Delete the messages with the matching chat_id
        chat.delete()

        return redirect(reverse('myapp:index'))
    else:
        return render(request, 'create_chat.html')
