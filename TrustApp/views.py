from fileinput import filename
from hashlib import new
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .models import *
from .forms import *

from django.contrib.auth import get_user_model





# Create your views here.

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists() or u.groups.filter(name='Employee') or u.groups.filter(name='Admin'), login_url='userAccessDenied')
def homeView(request) -> HttpResponse:
    if check_password('OneTwoThree', request.user.password):
        return redirect('password')
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
    logout(request)
    return render(request, "denied(user).html")

def deniedManager(request) -> HttpResponse:
    return render(request, "denied(manager).html")

def deniedAdmin(request) -> HttpResponse:
    return render(request, "denied(admin).html")


def findUsers(request) -> HttpRequest:
    context = {'usrs': User.objects.all()}

    return render(request, "search.html", context)


@user_passes_test(lambda u: u.groups.filter(name='Admin'), login_url='userAccessDenied')
@login_required(login_url='login')
def adminRedir(request):
    return redirect('admin:index')



@login_required(login_url='login')
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

@user_passes_test(lambda u: u.groups.filter(name='Manager').exists() or u.groups.filter(name='Employee') or u.groups.filter(name='Admin'), login_url='userAccessDenied')
@login_required(login_url='login')
def getthepeeps(request, EmployeeId):
    User = get_user_model()
    users = User.objects.all()
    valex  = int(EmployeeId)
    context = {'users': users, 'ValX': valex}
    
    return render(request, "search.html", context)

@user_passes_test(lambda u: u.groups.filter(name='Manager').exists() or u.groups.filter(name='Employee') or u.groups.filter(name='Admin'), login_url='userAccessDenied')
@login_required(login_url='login')
def filesView(request):
    usr = request.user
    files = Files.objects.all()
    context = {"files": files, 'usr': usr}
    if request.method == 'POST':
        if 'fileAdd' in request.POST:
            fileName = request.POST['fileName']
            Url = request.POST['Url']
            f = Files.objects.create(fileName = fileName, Url = Url)
            f.save()    
            us = request.user.profile.files
            us.add(f)    
    return render(request, 'files.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists(), login_url='managerAccessDenied')
def createUser(request):
    allTitles=Title.objects.all()
    if request.POST:
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(homeView)
    context = {'form':NewEmployeeForm, 'allTitles':allTitles}
    return render(request, 'createUser.html', context)

