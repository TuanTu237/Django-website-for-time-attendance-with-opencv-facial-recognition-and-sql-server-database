from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')


def login(request):
    return render(request,'core/login.html')

def signup(request):
    return render(request,'core/signup.html')

def slidebar(request):
    return render(request,'core/slidebar.html')

def slideNV(request):
    return render(request,'core/slideNV.html')

def loginNV(request):
    return render(request,'core/loginNV.html')

def loginQL(request):
    return render(request,'core/loginQL.html')