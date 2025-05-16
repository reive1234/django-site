from django.contrib import admin
from .models import Category, Product, Size, User

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(User)
