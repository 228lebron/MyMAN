# Generated by Django 4.1.3 on 2023-02-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0020_remove_part_package_type_part_case_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'verbose_name': 'Микросхема', 'verbose_name_plural': 'Микросхемы'},
        ),
        migrations.AlterField(
            model_name='part',
            name='brand',
            field=models.CharField(max_length=100, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='part',
            name='case_type',
            field=models.CharField(default='Корпус не указан!', max_length=50, null=True, verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='part',
            name='number',
            field=models.CharField(max_length=100, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='part',
            name='series',
            field=models.CharField(max_length=100, verbose_name='Серия'),
        ),
    ]
