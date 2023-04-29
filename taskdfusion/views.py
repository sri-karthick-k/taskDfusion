import psycopg2
from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.db import connection


# Create New User


"""
# Get list of  projects under individual user
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


# Get a list of userid and usernames of the users present in that project


@csrf_exempt
def members(request):
    with connection.cursor() as conn:
        if request.method == 'GET':
            pid = json.loads(request.body.decode('UTF-8'))
            conn.execute('SELECT userid FROM projects WHERE pid=(%s)', [pid['pid']])
            userid = conn.fetchall()
            user_names = []
            userid = userid[0]
            for user in userid:
                print(user)
                conn.execute('SELECT name FROM accounts WHERE uid=(%s)', [user])
                user_name = conn.fetchall
                user_names.append(user_name)
            print(user_names)
            return HttpResponse('Hello')


# Add new member to the project


@csrf_exempt
def add_members(request):
    with connection.cursor() as conn:
        if request.method == 'POST':
            rows = json.loads(request.body.decode('UTF-8'))
            # conn.execute('UPDATE projects SET userid=ARRAY_APPEND(userid, (%s)) WHERE pid=(%s)')
            print(rows)
            return HttpResponse("Done")


# Create New Project for user
@csrf_exempt
def add_project(request):
    with connection.cursor() as conn:
        if request.method == 'POST':
            rows = json.loads(request.body.decode('UTF-8'))
            print(rows)
            userid = "{" + "".join([str(item) for item in rows['uid']]) + "}"
            username = "{" + "".join([str(item) for item in rows['username']]) + "}"
            try:
                conn.execute('INSERT INTO projects (prname, userid, username) values(%s, %s, %s)',
                             [rows['prname'], userid, username])
            except psycopg2.Error as e:
                return HttpResponse("Couldn't execute: ", e)
            return HttpResponse("...Loading for developer to complete this function/request")
"""