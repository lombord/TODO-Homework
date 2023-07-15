from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('addTask', add_task, name='add_task'),
    path('task/<int:pk>/', show_task, name='task'),
    path('edit-task/<int:pk>/', edit_task, name='edit_task'),
    path('finish-task/<int:pk>/', finish_task, name='finish_task'),
    path('delete-task/<int:pk>/', delete_task, name='delete_task'),
]
