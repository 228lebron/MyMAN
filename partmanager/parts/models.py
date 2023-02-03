from django.db import models

class Part(models.Model):
    number = models.CharField(max_length=50, unique=True)
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    digikey_link = models.URLField()
    manufacturer_link = models.URLField()

    def __str__(self):
        return self.number

class Request(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    final_ruble_price = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.part} {self.quantity} {self.created_at}"

class Quote(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    datecode = models.PositiveIntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=255)
    lead_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.part} {self.price} {self.datecode} {self.quantity} {self.created_at}"

class Order(models.Model):
    quotes = models.ManyToManyField(Quote)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        parts_in_quotes = {}
        for part in self.quotes.all():
            parts_in_quotes['part'] = part.part.number
            parts_in_quotes['price'] = part.price
            return f"{parts_in_quotes}"