from datetime import date, datetime
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import CreateTask
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user = request.user)
    context = {
        'username': request.user,
        'todolist':data,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTask()

    if request.method == "POST":
        form = CreateTask(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    context = {'form':form}
    return render(request, "createtask.html", context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def status(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=id, user=request.user)
        task.is_finished = not task.is_finished
        task.save()

        return JsonResponse({'error': False})

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=id, user=request.user)
        task.delete()

        return JsonResponse({'error': False})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_AJAX(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(user=user,title=title, description=description)
        return JsonResponse({'error': False, 'msg':'Successful'})