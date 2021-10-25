from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


# Create your views here.

dic = [

    {'id':'first Id'},
    {'id':'second Id'}

]

var = 5

def home(request):

    p = Person.objects.all()[0]
    
    
    return render(request,'base/home.html',{'var' : p})

def room(request,y):
     return render(request,'base/room.html',{'dict':dic, 'x' : y})