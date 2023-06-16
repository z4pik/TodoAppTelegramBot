from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = TaskForm()
    return render(request, 'todo_app/create_task.html', {'form': form})


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/edit_task.html', {'form': form, 'task_id': task_id})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    print(task)
    if request.method == 'POST':
        task.delete()
        return redirect('profile')
    return HttpResponse(status=405)
