from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(reqiest):
    tasks = Task.objects.order_by('-id')
    return render(reqiest, 'main/index.html', {'title':'Главная страница сайта', 'tasks':tasks})

def about(reqiest):
    return render(reqiest, 'main/about.html')

def create(reqiest):
    error = ''
    if reqiest.method == 'POST':
        form = TaskForm(reqiest.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(reqiest, 'main/create.html', context)