from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeview(request) :
    return HttpResponse('homeview')

def deleteview(request) :
    return HttpResponse('delete view')

def loginview(request) :
    return render(request, 'login.html')

def signupview(request) :
    return HttpResponse('signup view')

def walletview(request) :
    return HttpResponse('wallet view')