from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection


class Tasks:
    @csrf_exempt
    def create_task(self, request):
        with connection.cursor() as conn:
            """ Create one task per user """
            if request.method == 'POST':
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute("INSERT INTO tasks (uid, title, dsc, status) values (%s, %s, %s, %s) RETURNING tid",
                                                                                                    [data['userid'],
                                                                                                     data['title'],
                                                                                                     data['dsc'],
                                                                                                     data['status']])
                taskid = conn.fetchall()
                print(taskid)
                return JsonResponse(data, safe=False)

    @csrf_exempt
    def list_task(self, request):
        with connection.cursor() as conn:
            if request.method == 'GET':
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute("SELECT * FROM tasks WHERE uid=(%s) AND tid=(%s)", [data['userid'], data['tid']])
                rows = conn.fetchall()
                tasks = []
                for row in rows:
                    result = {'taskid': row[0], 'userid': row[1], 'title': row[2], 'description': row[3],
                              'status': row[4]}
                    tasks.append(result)
                return JsonResponse(tasks, safe=False)

    @csrf_exempt
    def list_tasks(self, request):
        with connection.cursor() as conn:
            if request.method == 'GET':
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute("SELECT * FROM tasks WHERE uid=(%s)", [data['userid']])
                rows = conn.fetchall()
                tasks = []
                for row in rows:
                    result = {'taskid': row[0], 'userid': row[1], 'title': row[2], 'description': row[3],
                              'status': row[4]}
                    tasks.append(result)
                return JsonResponse(tasks, safe=False)

    @csrf_exempt
    def update_task(self, request):
        with connection.cursor() as conn:
            if request.method == 'PUT':
                """ Title update """
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute('UPDATE tasks SET title=%s WHERE tid=%s', [data['title'], data['tid']])

                conn.execute('SELECT * FROM tasks WHERE uid=(%s) AND tid=(%s)', [data['userid'], data['tid']])
                rows = conn.fetchall()

                tasks = []
                for row in rows:
                    result = {'taskid': row[0], 'userid': row[1], 'title': row[2], 'description': row[3],
                              'status': row[4]}
                    tasks.append(result)
                return JsonResponse(tasks, safe=False)

    @csrf_exempt
    def delete_task(self, request):
        with connection.cursor() as conn:
            if request.method == 'DELETE':
                data = json.loads(request.body.decode('UTF-8'))
                conn.execute('DELETE FROM tasks WHERE uid=(%s) AND tid=(%s)', [data['userid'], data['tid']])
                return HttpResponse("Deleted")

