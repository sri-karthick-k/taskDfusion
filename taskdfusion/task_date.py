# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection
import datetime


class TasksDate:
    @csrf_exempt
    def display_completed(self, request):
        with connection.cursor() as conn:
            """ Display today's completed tasks """
            if request.method == 'GET':
                data = json.loads(request.body.decode('UTF-8'))
                now = datetime.datetime.now()
                date_string = now.strftime("%Y-%m-%d")
                conn.execute("SELECT * FROM tasks WHERE status='completed' AND modifiedon=(%s) AND uid=(%s)",
                             [date_string, data['userid']])
                rows = conn.fetchall()

                tasks = []
                for row in rows:
                    result = {'taskid': row[0], 'userid': row[1], 'title': row[2], 'description': row[3],
                              'status': row[4], 'Modified On': row[5]}
                    tasks.append(result)
                return JsonResponse(tasks, safe=False)

    @csrf_exempt
    def display_recent(self, request):
        with connection.cursor() as conn:
            """ Display 50 days tasks """
            if request.method == 'GET':
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute(
                    "SELECT * FROM tasks WHERE uid=(%s) AND modifiedon BETWEEN NOW() - INTERVAL '50 days' AND NOW();",
                    [data['userid']])
                rows = conn.fetchall()

                tasks = []
                for row in rows:
                    result = {'taskid': row[0], 'userid': row[1], 'title': row[2], 'description': row[3],
                              'status': row[4], 'Modified On': row[5]}
                    tasks.append(result)
                return JsonResponse(tasks, safe=False)
