from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from django.db import connection


@csrf_exempt
def register(request):
    with connection.cursor() as conn:
        if request.method == 'POST':
            # data = json.loads(request.body.decode('UTF-8'))
            uname = request.POST['username']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            email = request.POST['email']
            if password == confirmpassword:
                conn.execute("INSERT INTO accounts (name, email, password) values (%s, %s, %s)", [uname, email, password])
                return render(request, 'base.html', {'email': email, 'name': uname})
            else:
                return render(request, 'wrong.html', {'value': 'Password did not match'})


# Check credentials to login
@csrf_exempt
def login(request):
    with connection.cursor() as conn:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            conn.execute("SELECT password, name from accounts WHERE email=(%s)", [email])
            row = conn.fetchall()
            uname = row[0][1]
            if password == row[0][0]:
                return render(request, 'base.html', {'email': email, 'name': uname})
            else:
                return render(request, 'wrong.html', {'value': 'Incorrect Password'})


@csrf_exempt
def logpage(request):
    return render(request, 'index.html')


@csrf_exempt
def sample(request):
    email = request.GET['email']
    password = request.GET['password']
    return render(request, 'base.html', {'email': email, 'password': password})

@csrf_exempt
def signup_page(request):
    return render(request, 'signup.html')
