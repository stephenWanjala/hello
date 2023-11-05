import datetime

from django.shortcuts import render, redirect, get_object_or_404

from todo.forms.forms import TodoForm
from todo.models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todo/create_todo.html', {'form': form, 'year': datetime.date.today().year})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo, 'year': datetime.date.today().year})
