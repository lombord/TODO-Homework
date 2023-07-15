from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import *
from .forms import *

# Create your views here.


def home_page(request: HttpRequest):
    tasks = TaskModel.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task/home.html', context)


def add_task(request: HttpRequest):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'task/add_task.html', context)


def edit_task(request: HttpRequest, pk: int):
    task = get_object_or_404(TaskModel, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'task/add_task.html', context)


def show_task(request: HttpRequest, pk: int):
    task = get_object_or_404(TaskModel, pk=pk)
    context = {'task': task}
    return render(request, 'task/task.html', context)


def delete_task(request: HttpRequest, pk: int):
    task = get_object_or_404(TaskModel, pk=pk)
    task.delete()
    return redirect('home')


def finish_task(request: HttpRequest, pk: int):
    task = get_object_or_404(TaskModel, pk=pk)
    task.status = True
    task.save()
    return redirect('home')
