"""Trust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TrustApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name="userProfile"),
    path("login", loginUser, name="login"),
    path("logout", logoutUser, name="logout"),
    path("search+<type>+<prof>", getthepeeps, name = "search"),
    path("userDenied", deniedUser, name="userAccessDenied"),
    path("managerDenied", deniedManager, name="managerAccessDenied"),
    path("adminDenied", deniedAdmin, name="adminAccessDenied"), 
    path("updatePassword", updatePassword, name="password"),
    path("addFiles", filesView, name='addFiles')
]

