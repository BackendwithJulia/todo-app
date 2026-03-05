from django.shortcuts import render, redirect
from .models import Task
from .forms import Taskform

def home(request):
    tasks = Task.objects.all()
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)


def updateTask(request, primarykey):
    task = Task.objects.get(id=primarykey)
    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form':form}

    return render(request, 'tasks/update_task.html', {'form': form})


def deleteTask(request, primarykey):
    item = Task.objects.get(id=primarykey)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
