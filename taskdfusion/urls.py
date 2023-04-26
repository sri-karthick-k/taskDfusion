from django.urls import path, include
from .views import register, login, allprojects, members, add_members

urlpatterns = [
    path('signup', register),
    path('login', login),
    path('getprojects', allprojects),
    path('members', members),
    path('addmember', add_members)
]
