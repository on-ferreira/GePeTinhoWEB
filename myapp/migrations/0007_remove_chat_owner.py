# Generated by Django 4.2.1 on 2023-05-28 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_message_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='owner',
        ),
    ]
