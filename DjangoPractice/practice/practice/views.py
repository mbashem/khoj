# this file is created for some practice

# from django.http import HttpResponse
from django.http import HttpResponse


def link(request):
    return HttpResponse ("Hello everyone")


def git(request):
    return HttpResponse ('''<h2> Git Link : </h2> <a href="https://github.com/MaishaAmin"> here is the link! </a>''')
