# Generated by Django 4.1.3 on 2023-02-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0006_remove_request_allow_analogues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quota',
            name='part_number',
            field=models.CharField(max_length=100),
        ),
    ]
