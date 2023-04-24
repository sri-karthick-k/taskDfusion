from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.db import connection


@csrf_exempt
def register(request):
    with connection.cursor() as conn:
        if request.method == 'POST':
            data = json.loads(request.body.decode('UTF-8'))
            conn.execute("INSERT INTO accounts (name, email, password) values (%s, %s, %s)", [data['name'], data['email'], data['password']])
            return JsonResponse(data, safe=False)


@csrf_exempt
def login(request):
    with connection.cursor() as conn:
        if request.method == 'GET':
            data = json.loads(request.body.decode('UTF-8'))
            conn.execute("SELECT password from accounts WHERE email=(%s)", [data['email']])
            row = conn.fetchall()
            # print(row[0][0])
            if data['password'] == row[0][0]:
                return HttpResponse("Successful Login")
            else:
                return HttpResponse("Wrong Password")


@csrf_exempt
def allprojects(request):
    with connection.cursor() as conn:
        if request.method == 'GET':
            uid = json.loads(request.body.decode('UTF-8'))
            conn.execute("SELECT * FROM projects WHERE userid=(%s)", [uid['uid']])
            rows = conn.fetchall()
            if len(rows) == 0:
                return HttpResponse("No Projects available")
            else:
                results = []
                for row in rows:
                    result = {"project name": row[1]}
                    results.append(result)
                return JsonResponse(results, safe=False)