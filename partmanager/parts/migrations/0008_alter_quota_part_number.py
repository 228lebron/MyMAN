# Generated by Django 4.1.3 on 2023-02-10 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_alter_quota_part_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quota',
            name='part_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.part'),
        ),
    ]
