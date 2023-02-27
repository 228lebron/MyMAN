from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone, timedelta

USD_rate = 75
air_shipping_cost = 5
sea_shipping_cost = 1

PACKAGE_WEIGHTS = {
    'SOIC-8': 0.32,
    'SOIC-14': 0.55,
    'TO-92': 0.16,
    'SOD-523': 0.3
}

CURRENCY_CHOICES = (
        ('USD', 'Доллар'),
        ('EUR', 'Евро'),
        ('RUB', 'Рубль'),
        # add more currency options here
    )

class Part(models.Model):
    series = models.CharField(max_length=100, verbose_name='Серия')
    number = models.CharField(max_length=100, verbose_name='Номер')
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    case_type = models.CharField(max_length=50, null=True, default='Корпус не указан!', verbose_name='Корпус')

    def __str__(self):
        return f'{self.number} ({self.brand}) ({self.series}) ({self.case_type})'
    def package_weight(self):
        return PACKAGE_WEIGHTS.get(self.case_type, 0)

    class Meta:
        verbose_name = "Микросхема"
        verbose_name_plural = "Микросхемы"


class Quota(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='U/P USD')
    ruble_price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='U/P RUB', default=0)
    datecode = models.PositiveIntegerField(verbose_name='DC')
    lead_time = models.CharField(max_length=100, verbose_name='Срок')
    supplier = models.CharField(max_length=100, verbose_name='Поставщик')
    date = models.DateField(verbose_name='Дата квоты')

    def __str__(self):
        return f'{self.part.number} ({self.part.brand}) ({self.quantity} шт.) ({self.price}$) ({self.supplier}) ({self.date})'
    def save(self, *args, **kwargs):
        self.ruble_price = self.price * USD_rate
        super(Quota, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Квота"
        verbose_name_plural = "Квоты"
class Request(models.Model):

    STATUS_CHOICES = (
        ('QUOTA', 'Есть квота'),
        ('NO_QUOTA', 'Нет квоты'),
        ('PAID', 'Оплачен'),
        ('ORDERED', 'Заказан')
    )

    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во')
    customer = models.CharField(max_length=100, verbose_name='Клиент')
    date = models.DateField(verbose_name='Дата запроса')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', verbose_name='Менеджер')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='NO_QUOTA', verbose_name='Статус')

    selected_quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, null=True, blank=True, related_name='selected_quotas')
    customer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null=True, default='RUB')
    def __str__(self):
        return f'{self.part.number} - {self.quantity} - {self.customer}'

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class RequestQuotaResult(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    quota = models.ForeignKey(Quota, on_delete=models.SET_NULL, null=True)

    ruble_air_price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Авиа', default=0)
    ruble_sea_price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Морем', default=0)

    def save(self, *args, **kwargs):
       if self.quota:
           self.ruble_air_price = (self.quota.part.package_weight() * air_shipping_cost + float(self.quota.price)) * USD_rate
           self.ruble_sea_price = (self.quota.part.package_weight() * sea_shipping_cost + float(self.quota.price)) * USD_rate
       super(RequestQuotaResult, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Заявка с квотой"
        verbose_name_plural = "Заявки с квотами"



