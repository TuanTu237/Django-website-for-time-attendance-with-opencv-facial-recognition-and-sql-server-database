from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')


def login(request):
    return render(request,'core/login.html')

def signup(request):
    return render(request,'core/signup.html')

def slidebar(request):
    return render(request,'core/slidebar.html')