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
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




# Create your views here.

@login_required(login_url='login')
def homeView(request) -> HttpResponse:
    return render(request, "index.html")


def logoutUser(request):
    logout(request)
    return redirect("login")

def loginUser(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(homeView)
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def deniedUser(request) -> HttpResponse:
    return render(request, "denied(user).html")

def deniedManager(request) -> HttpResponse:
    return render(request, "denied(manager).html")

def deniedAdmin(request) -> HttpResponse:
    return render(request, "denied(admin).html")

def findUsers(request) -> HttpRequest:
    return render(request, "search.html")


def updatePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(homeView)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'updatepw.html', {
        'form': form
    })