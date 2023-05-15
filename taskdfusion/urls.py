from django.urls import path, include
from .account_views import Account
from .task_views import Tasks
from .task_date import TasksDate

class URLS(Account, Tasks, TasksDate):

    a1 = Account()
    t1 = Tasks()
    t2 = TasksDate()

    urlpatterns = [

        # account
        path('signup', a1.register),
        path('login', a1.login),

        # tasks
        path('addtask', t1.create_task),
        path('list-task', t1.list_task),
        path('list-tasks', t1.list_tasks),
        path('task-update', t1.update_task),
        path('task-delete', t1.delete_task),

        path('today-complete', t2.display_completed),
        path('display-recent', t2.display_recent)
    ]


u1 = URLS()

urlpatterns = u1.urlpatterns
