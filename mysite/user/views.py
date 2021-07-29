from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required as _login_required
from .models import *
def login_page(request):
    if request.POST:
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_page")
    return render(request, "login.html")

def login_required(funf):
    return _login_required(function=funf, login_url="login-page")

def register_page(request):
    if request.POST:
        email = request.POST.get("email")
        full_name = request.POST.get("full-name")
        password = request.POST.get("password")
        user = User.objects.create_user(email=email, password=password, full_name=full_name)

        if user is not None:
            login(request, user)
            return HttpResponse("home page")

    return render(request, "register.html")

@login_required
def home_page(request):
    return render(request, 'index.html')