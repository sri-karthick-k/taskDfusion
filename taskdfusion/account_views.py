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
            data = json.loads(request.body.decode('UTF-8'))
            conn.execute("INSERT INTO accounts (name, email, password) values (%s, %s, %s)",
                         [data['name'], data['email'], data['password']])
            return JsonResponse(data, safe=False)


# Check credentials to login
@csrf_exempt
def login(request):
    with connection.cursor() as conn:
        if request.method == 'GET':
            data = json.loads(request.body.decode('UTF-8'))

            conn.execute("SELECT password from accounts WHERE email=(%s)", [data['email']])
            row = conn.fetchall()
            if data['password'] == row[0][0]:
                return HttpResponse("Successful Login")
            else:
                # return HttpResponse("Wrong Password")
                return render(request, 'wrong.html')


@csrf_exempt
def logpage(request):
    return render(request, 'index.html')


@csrf_exempt
def sample(request):
    email = request.GET['email']
    password = request.GET['password']
    return render(request, 'base.html', {'email': email, 'password': password})
