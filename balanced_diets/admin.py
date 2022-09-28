from django.contrib import admin

# Register your models here.

from .models import Dish, Product, Recipe, User, exclusion_product
admin.site.register(Dish)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(User)
admin.site.register(exclusion_product)

