from django.shortcuts import render
from django.http import HttpResponse
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework import generics,viewsets

def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
    