# -*- coding: utf-8 -*- 
from django.http import HttpResponse

def admin(request):
    return HttpResponse("Hello world")
    
def WebHome(request):
    return HttpResponse("Hello world")
    
def rest(request):
    return HttpResponse("Hello world")