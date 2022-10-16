from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView




def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is invalid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


class TaskView(DetailView):
    model = Task
    template_name = 'main/task.html'
    context_object_name = 'taskdetail'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/edit.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main/delete.html'
    success_url = '/'

