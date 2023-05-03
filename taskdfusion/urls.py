from django.urls import path, include
from .account_views import Account
from .task_views import Tasks


class URLS(Account):

    a1 = Account()
    t1 = Tasks()

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
    ]


u1 = URLS()

urlpatterns = u1.urlpatterns
