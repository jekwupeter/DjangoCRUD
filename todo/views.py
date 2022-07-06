from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    """
    Returns:
        todo items as dict"""
    all_items = Todo.objects.order_by("-date")
    #all_items = Todo.objects.all()
    context = {'all_items': all_items}
    return render(request, 'index.html', context)

def show(request, pk):
    item = Todo.objects.get(id = pk)
    context = {"item": item}
    return render(request, 'view.html', context)

def edit(request, pk):
    todo_item = Todo.objects.get(id = pk)
    form = TodoForm(instance=todo_item)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
    context = {"form": form}
    return render(request, 'add.html', context)

def delete(request, pk):
    todo_item = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo_item.delete()
        return redirect("todo:home")
    context = {"todo_item": todo_item}
    return render(request, 'delete.html', context)

def add(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('todo:home')
            except:
                pass
    context = {"form": form}
    return render(request, 'add.html', context)

 