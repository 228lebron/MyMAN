from django.contrib import admin
from .models import Part, Request, Quote, Order

# Register your models here.
admin.site.register(Part)
admin.site.register(Request)
admin.site.register(Quote)
admin.site.register(Order)
