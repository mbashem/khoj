from django import http
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

rooms = [
    {'id':1, 'name':'learn django'},
    {'id':2, 'name':'learn python'},
    {'id':3, 'name':'learn git'},
]

def index(request, pk):
    return render(request, 'index.html', {'rooms':rooms})


def profile(request):
    return HttpResponse("This is task profile page")


def file(request):
    file = open("tasks/one.txt", 'r+')
    return HttpResponse(file.read())


def Check_Command(request):
    checked = request.GET.get("text", "default")

    removepunc = request.GET.get("removepunc", "off")

    capital = request.GET.get("capitalize", "off")

    removespace = request.GET.get("removespace", "off")

    if removepunc == "on":
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''

        final_ckecked = ""

        for char in checked:
            if char not in punctuations:
                final_ckecked = final_ckecked + char

        params = {'purpose': 'Remove Punctuation', 'checked_text': final_ckecked}

        return render(request, 'checktext.html', params)


    elif capital == "on":

        params = {'purpose': 'Capitalization', 'checked_text': checked.upper()}
        return render(request, 'checktext.html', params)

    elif removespace == "on":

        final_space_remove = ""
        for char in checked:
            if char != ' ':
                final_space_remove = final_space_remove + char

        params = {'purpose': 'Remove space', 'checked_text': final_space_remove}

        return render(request, 'checktext.html', params)

    else:
        return HttpResponse("Error!")
