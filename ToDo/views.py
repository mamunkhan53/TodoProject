from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'home.html', context)

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete(request, pk):
    task = Task.objects.filter(pk=pk)
    task.delete()
    return redirect('home')

def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task = request.POST['task']
        get_task.task = task
        get_task.save()
        return redirect('home')
    return render(request, 'editTask.html', locals())

