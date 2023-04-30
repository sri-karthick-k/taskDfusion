from django.urls import path, include
# from .views import register, login, allprojects, members, add_members, add_project
from .account_views import register, login, sample, logpage, signup_page


urlpatterns = [
    path('signup', register),
    path('login', login),
    path('', logpage),
    path('sample', sample),
    path('signup_page', signup_page),
    # path('getprojects', allprojects),
    # path('members', members),
    # path('addmember', add_members),
    # path('addproject', add_project)
]
