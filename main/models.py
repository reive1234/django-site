from django.db import models

# Таблиця категорій
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Таблиця розмірів (для зв'язку багато-до-багатьох)
class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Таблиця товарів
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sizes = models.ManyToManyField(Size)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

# Таблиця користувачів (проста, кастомна)
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

