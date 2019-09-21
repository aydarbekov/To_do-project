from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TaskForm
from webapp.models import Article

def index_views(request, *args, **kwargs):
    tasks = Article.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def task_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    return render(request, 'task_view.html', context={'task':task})

def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request,'task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Article.objects.create(description=data['description'], full_descr=data['full_descr'], status=data['status'], date=data['date'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form':form})

def task_delete(request, pk):
    task = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')

def task_update_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={'description': task.description, 'full_descr': task.full_descr, 'status': task.status, 'date': task.date})
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        task.description = request.POST.get('description')
        if not task.description:
            description_error = "This field is required"
        elif len(task.description) > 200:
            description_error = "Field value is too long. Max length is 200 characters."
        else:
            description_error = None

        task.full_descr = request.POST.get('full_descr')
        if not task.full_descr:
            full_descr_error = "This field is required"
        elif len(task.full_descr) > 3000:
            full_descr_error = "Field value is too long. Max length is 3000 characters."
        else:
            full_descr_error = None
        task.status = request.POST.get('status')
        task.date = request.POST.get('date')
        if not description_error and not full_descr_error:
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            context = {'description_error': description_error, 'full_descr_error': full_descr_error, 'task': task}
            return render(request, 'update.html', context=context)



