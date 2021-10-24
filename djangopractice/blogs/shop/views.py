from django.shortcuts import render
from .models import myblogs

from django.http import  HttpResponse


def index(request):
    blogs = myblogs.objects.all()
    print(blogs)
    slides = len(blogs)
    params = {'blogs': blogs, 'range': range(slides), 'slides':slides}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
