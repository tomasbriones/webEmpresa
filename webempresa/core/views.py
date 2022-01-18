from urllib.request import Request
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/home.html")

def about(request):
    return HttpResponse('<h1>about</h1>')

def services(request):
    return HttpResponse('<h1>services</h1>')

def store(request):
    return HttpResponse('<h1>store</h1>')

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def blog(request):
    return HttpResponse('<h1>blog</h1>')

def sample(request):
    return HttpResponse('<h1>sample</h1>')
