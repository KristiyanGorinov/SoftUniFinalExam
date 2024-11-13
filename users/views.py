from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, View

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.models import *


class HomeView(ListView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'public/public-page.html'


class DescriptionView(ListView):
    model = User
    template_name = 'public/description.html'


class AboutView(ListView):
    model = User
    template_name = 'public/about-me.html'


@login_required(login_url='login')
def UserHomeView(request):
    return render(request, 'user/user-page.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('user-home')
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('login')

    context = {'form': form}

    return render(request, 'user/register-user.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('user-home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user-home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'user/login-user.html')


def logout_user(request):
    logout(request)
    return redirect('home')
