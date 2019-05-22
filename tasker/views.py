from django.shortcuts import render, redirect
from tasker.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def main(request):
    if request.method == "POST":
        if request.POST.get("id_to_delete"):
            ToDo.objects.get(pk=request.POST.get("id_to_delete")).delete()
        if request.POST.get("id_to_edit"):
            task_to_edit = ToDo.objects.get(pk=request.POST.get("id_to_edit"))
            task_to_edit.text = request.POST.get("edit")
            task_to_edit.save()
        if request.POST.get("todo"):
            ToDo.objects.create(text=request.POST.get("todo"))

    todos = ToDo.objects.all().order_by("creation_date")

    return render(request, 'main.html', {
        'todos': todos
    })

@csrf_exempt
def addtask(request):
    return render(request, 'addtask.html')

@csrf_exempt
def edittask(request, task_id):
    task = ToDo.objects.get(pk=task_id)
    return render(request, 'edittask.html', {
        'task': task
    })