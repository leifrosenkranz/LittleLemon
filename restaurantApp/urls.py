from django.contrib import admin
from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('sayhello/', views.sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('restaurant/', views.index, name='index'),
    path('restaurant/api/menu/', views.MenuItemView.as_view(), name='menu'),
    path('restaurant/api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    path('restaurant/api-token-auth/', obtain_auth_token)
]