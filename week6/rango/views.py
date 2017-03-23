'''
Created on Mar 23, 2017

@author: jackwang
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there world!")
