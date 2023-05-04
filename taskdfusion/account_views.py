from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.db import connection


class Account:
    @csrf_exempt
    def register(self, request):
        with connection.cursor() as conn:
            if request.method == 'POST':
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute("INSERT INTO accounts (name, email, password) values (%s, %s, %s)",
                             [data['name'], data['email'], data['password']])
                conn.execute("SELECT uid from accounts WHERE email=(%s)", [data['email']])
                row = conn.fetchall()
                data['userid'] = row[0][0]
                return JsonResponse(data, safe=False)

    # Check credentials to login
    @csrf_exempt
    def login(self, request):
        with connection.cursor() as conn:
            if request.method == 'GET':
                data = json.loads(request.body.decode('UTF-8'))
                try:
                    conn.execute("SELECT password,uid from accounts WHERE email=(%s)", [data['email']])
                    row = conn.fetchall()
                    if data['password'] == row[0][0]:
                        return HttpResponse(row[0][1])
                    else:
                        return HttpResponse("Wrong password")
                except IndexError as e:
                    return HttpResponse("No email Found please register")

