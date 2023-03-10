# Generated by Django 4.1.3 on 2023-02-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0023_alter_quota_options_alter_request_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestquotaresult',
            options={'verbose_name': 'Заявка с квотой', 'verbose_name_plural': 'Заявки с квотами'},
        ),
        migrations.AddField(
            model_name='requestquotaresult',
            name='ruble_air_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='Авиа RUB'),
        ),
        migrations.AddField(
            model_name='requestquotaresult',
            name='ruble_sea_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='Морем RUB'),
        ),
    ]
