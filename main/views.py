from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def sale(request):
    return render(request, 'main/sale.html')

def new(request):
    return render(request, 'main/new.html')

def login(request):
    return render(request, 'main/login.html')
