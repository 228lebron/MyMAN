# Generated by Django 4.1.3 on 2023-02-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0021_alter_part_options_alter_part_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quota',
            name='lead_time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quota',
            name='ruble_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='U/P RUB'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='U/P USD'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
    ]
