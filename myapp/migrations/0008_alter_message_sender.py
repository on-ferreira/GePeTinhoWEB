# Generated by Django 4.2.1 on 2023-05-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_chat_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.TextField(max_length=10),
        ),
    ]