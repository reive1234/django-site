from django.shortcuts import render
from decimal import Decimal, InvalidOperation
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # Отримання параметрів з GET
    selected_categories = request.GET.getlist('category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    # Перевірка та обробка числових значень
    try:
        price_min = float(price_min) if price_min is not None and price_min != '' else None
        if price_min is not None and price_min < 0:
            price_min = 0
    except ValueError:
        price_min = None

    try:
        price_max = float(price_max) if price_max is not None and price_max != '' else None
        if price_max is not None and price_min is not None and price_max < price_min:
            price_max = price_min
    except ValueError:
        price_max = None

    # Фільтрація по категоріям
    if selected_categories:
        products = products.filter(category__id__in=selected_categories)

    # Фільтрація по ціні
    if price_min is not None:
        products = products.filter(price__gte=price_min)
    if price_max is not None:
        products = products.filter(price__lte=price_max)

    context = {
        'categories': categories,
        'products': products,
        'selected_categories': list(map(int, selected_categories)) if selected_categories else [],
        'price_min': price_min if price_min is not None else '',
        'price_max': price_max if price_max is not None else '',
    }

    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')

def sale(request):
    products = Product.objects.exclude(discount__isnull=True)
    valid_products = []
    for product in products:
        try:
            # Перевіряємо, що discount можна конвертувати в Decimal і він більше 0
            discount_value = Decimal(product.discount)
            if discount_value > 0:
                valid_products.append(product)
        except (InvalidOperation, TypeError):
            # Ігноруємо продукти з некоректним discount (порожнім рядком або іншим)
            continue

    return render(request, 'main/sale.html', {'products': valid_products})

def new(request):
    products = Product.objects.order_by('-id')[:10]  # Останні 10 товарів
    return render(request, 'main/new.html', {'products': products})

def login(request):
    return render(request, 'main/login.html')
