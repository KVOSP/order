from django.contrib import admin
from order.db.models import food, restaurant

admin.site.register(food)
admin.site.register(restaurant)