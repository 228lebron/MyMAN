# Generated by Django 4.1.3 on 2023-02-10 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_request_allow_analogues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='allow_analogues',
        ),
    ]
