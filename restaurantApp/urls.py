from django.contrib import admin
from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('home/', views.sayHello, name='sayHello'),
    path('restaurant/', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
]