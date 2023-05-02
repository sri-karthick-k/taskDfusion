from django.urls import path, include
# from .views import register, login, allprojects, members, add_members, add_project
from .account_views import register, login
from .task_views import create_task, list_task, list_tasks, update_task, delete_task


urlpatterns = [
    path('signup', register),
    path('login', login),
    # path('getprojects', allprojects),
    # path('members', members),
    # path('addmember', add_members),
    # path('addproject', add_project)
    path('addtask', create_task),
    path('list-task', list_task),
    path('list-tasks', list_tasks),
    path('task-update', update_task),
    path('task-delete', delete_task),
]
