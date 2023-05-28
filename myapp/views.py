from django.shortcuts import render, redirect
from .models import Chat, Message
from django.urls import reverse
import requests
from urllib.parse import urljoin


def index(request):
    chats = Chat.objects.all()
    context = {'chats': chats}
    return render(request, 'index.html', context)


def chat_view(request, chat_id):
    chats = Chat.objects.all()
    chat = Chat.objects.get(pk=chat_id)
    messages = Message.objects.filter(chat=chat)
    context = {'chats': chats, 'chat': chat, 'messages': messages}
    return render(request, 'chat_detail.html', context)


def create_chat(request):
    if request.method == 'POST':
        chat = Chat.objects.create()
        return redirect(reverse('myapp:chat_view', kwargs={'chat_id': chat.pk}))
    else:
        return render(request, 'create_chat.html')


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

