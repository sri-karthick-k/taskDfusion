from django.urls import path, include
from .views import register, login, allprojects

urlpatterns = [
    path('signup', register),
    path('login', login),
    path('getprojects', allprojects),


]