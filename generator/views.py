from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.
def hello(request):
    return HttpResponse('Hello is there!!!')


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    length = int(request.GET.get("length"))

    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
