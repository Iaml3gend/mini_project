from django.http import request
from django.http import HttpResponse
# from django import re
from .forms import UserRegisterForm
import re
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from mission.models import Mission
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')


def campus(request):
    return render(request, 'campus.html')


def news(request):
    return render(request, 'news.html')


def training(request):
    return render(request, 'training.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('signin')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(
                request, ("There was an error logging in try again "))
            return redirect('signin')

    else:
        return render(request, 'signin.html', {})


def signout(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('signin')

# registeration starts here
