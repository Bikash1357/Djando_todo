from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Todo.objects.create(title=title)
    return redirect('index')


def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')
