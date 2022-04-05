from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.

@login_required(login_url='login')
def home_view(request:HttpRequest)->render:
    return render(request, 'index.html')

def log_view(request:HttpRequest)->render:
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect("login")

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('')
    # else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(home_view)
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)
