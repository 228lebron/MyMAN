# Generated by Django 4.1.3 on 2023-02-10 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0004_request_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='allow_analogues',
            field=models.BooleanField(default=False),
        ),
    ]