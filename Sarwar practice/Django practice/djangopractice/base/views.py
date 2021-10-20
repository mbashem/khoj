from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

dic = [

    {'id':'first Id'},
    {'id':'second Id'}

]

var = 5

def home(request):
    return render(request,'base/home.html')

def room(request,y):
     return render(request,'base/room.html',{'dict':dic, 'x' : y})