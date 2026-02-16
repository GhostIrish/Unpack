from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    return render(request, 'core/login.html')