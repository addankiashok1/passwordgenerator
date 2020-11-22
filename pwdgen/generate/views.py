from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generate/home.html')

def about(request):
    return render(request, 'generate/about.html')

def password(request):
    charcters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        charcters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charcters.extend(list('!@#$%^&*()-+/?'))
    if request.GET.get('numbers'):
        charcters.extend(list('0123456789'))

    thepassword = ''
    for i in range(length):
        thepassword+=random.choice(charcters)

    return render(request, 'generate/password.html',{'password':thepassword})