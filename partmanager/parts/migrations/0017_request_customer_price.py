# Generated by Django 4.1.3 on 2023-02-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0016_delete_responsequota'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='customer_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]