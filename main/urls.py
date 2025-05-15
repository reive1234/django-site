from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sale/', views.sale, name='sale'),
    path('new/', views.new, name='new'),
    path('login/', views.login, name='login'),
]
