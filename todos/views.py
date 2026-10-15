from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})


def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "할 일이 등록되었습니다.")
            return redirect("todos:list")
    else:
        form = TodoForm()
    return render(request, "todos/todo_form.html", {"form": form, "mode": "등록"})


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "할 일이 수정되었습니다.")
            return redirect("todos:list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/todo_form.html", {"form": form, "mode": "수정"})


@require_POST
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.success(request, "할 일이 삭제되었습니다.")
    return redirect("todos:list")


@require_POST
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save(update_fields=["is_completed"])
    return redirect("todos:list")
