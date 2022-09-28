# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 \
**Nama  : Nadira Maysa Dyandra** \
**NPM   : 2106632232** \
**Kelas : A**

## Tautan Aplikasi Heroku
Berikut adalah tautan menuju hasil lab:
https://tugas2nadira.herokuapp.com/todolist
https://tugas2nadira.herokuapp.com/todolist/register
https://tugas2nadira.herokuapp.com/todolist/login
https://tugas2nadira.herokuapp.com/todolist/logout
https://tugas2nadira.herokuapp.com/todolist/create-task

## Kegunaan {% csrf_token %} pada Elemen <form>
Cross Site Request Forgery (CSRF) adalah sebuah serangan terhadap *web application* yang memanfaatkan *bug* atau *vulnerability* pada *web application* yang bekerja dengan cara mengeksploitasi suatu task dari sebuah Web dengan memanfaatkan autentikasi yang dimiliki oleh korban. \
Hal ini biasanya terjadi akibat kode yang buruk selama waktu pengembangan sehingga menghasilkan *bug* tersebut yang dapat disalahgunakan oleh orang lain dengan maksud buruk. \
Adapun kegunaan {% csrf_token %} pada Elemen <form> adalah untuk mengamankan web dari serangan CSRF. \
CSRF Token adalah nilai yang unik, rahasia, dan tidak terduga yang dihasilkan oleh aplikasi pada sisi server kemudian dikirimkan ke klien dalam permintaan HTTP berikutnya yang nantinya dibuat di sisi klien. 
Saat permintaan selanjutnya dibuat, aplikasi di sisi server melakukan validasi permintaan tersebut yang diharapkan akan menolak permintaan jika CSRF token tidak ada atau tidak valid.
Sehingga, CSRF Token dapat digunakan untuk mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. 
Karena penyerang tidak dapat menentukan maupun memprediksi nilai token CSRF pengguna, maka penyerang tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut. \
Dengan demikian, dapat disimpulkan bahwa, apabila tidak ada potongan kode {% csrf_token %} pada elemen <form>, maka web akan menjadi rentan terhadap serangan SCRF yang sangat merugikan itu. 

## Membuat Elemen <form> Secara Manual
Ya, kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}.
Membuat elemen <form> secara manual dapat dilakukan dengan cara berikut.
```
<form action="[URL DESTINATION]" method="[METHOD]">
    {% csrf_token %}
    <input type="[INPUT TYPE]" other attribute>
    ...
    ...
    <input type="[INPUT TYPE]" other attribute>
</form>
```

## Proses Alur Data
1. User meminta request dengan TyperAddress: http://host/path pada browser \
2. Browser menghasilkan HTTP Request ke http://host/path \
3. Server menerima HTTP Request dan mencari views.py yang sesuai untuk meng-handle permintaan \
4. Views.py yang sesuai akan menghasilkan halaman FORM HTML \
5. Halaman FORM yang dihasilkan views.py di tampilkan kepada user \
6. User mengisi dan mengumpulkan Form \
7. Browser menghasilkan HTTP Request, method, dan arguments ke URL tujuan berdasarkan HTML page FORM \
8. Server menerima HTTP Request dan mencari views.py yang sesuai untuk meng-handle permintaan \
9. Views.py yang sesuai akan melakukan sesuatu (tergantung pada kode) dan menghasilkan halaman HTML \
10. Browser menampilkan halaman HTML kepada user.

## Cara Implementasi *Checklist*
1. Membuat aplikasi todolist dengan perintah berikut.
```
python manage.py startapp todolist
```
2. Menambahkan aplikasi todolist ke dalam INSTALLED_APPS pada settings.py
```
INSTALLED_APPS = [
    .....,
    'todolist',
    .....,
]
```
3. Membuat models.py pada folder todolist untuk membuat model dengan fields user, date, title, description, dan is_finished. \
4. Lakukan perintah berikut di terminal untuk mempersiapkan migrasi skema model ke dalam *database* Django lokal.
```
python manage.py makemigrations
```
5. Lakukan perintah berikut di terminal untuk menerapkan skema model yang telah dibuat ke dalam *database* Django lokal. 
```
python manage.py migrate
```
6. Membuat halaman form untuk pembuatan task dengan cara membuat berkas forms.py pada folder todolist yang berisi kode berikut.
```
from django.forms import ModelForm
from .models import Task
from django import forms

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
```
7. Membuat fungsi show_todolist, create_task, status, delete, registrasi, login, logout user. Hal ini dapat dikodekan pada views.py dengan menuliskan kode-kode berikut.
```
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import CreateTask
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
```
Kemudian mendefinisikan masing-masing fungsi.
```
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
def status(id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def delete(id):
    delete = Task.objects.get(pk=id)
    delete.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

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
```
Setelah itu, membuat berkas HTML baru untuk fungsi register dan fungsi login_user dengan nama register.html dan login.html. Isi dari register.html adalah sebagai berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}

<div class="login">

    <h1>Formulir Registrasi</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}

</div>

{% endblock content %}
```
Sedangkan, isi dari login.html adalah sebagai berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class="login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>

            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}

    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```
Isi dari todolist.html adalah sebagai berikut.
```
{% extends 'base.html' %}
{% block content %}
<h3>Halo {{user}}!</h3>

<table border="2">
    <tr>
        <th>Date</th>
        <th>Title</th>
        <th>Description</th>
        <th>Status</th>
        <th colspan="3">Detail</th>
    </tr>
    {% for todo in todolist %}
    <tr>
        <th>{{todo.date}}</th>
        <th>{{todo.title}}</th>
        <th>{{todo.description}}</th>
        {% if todo.is_finished %}
        <th>Selesai</th>
        {% else %}
        <th>Belum Selesai</th>
        {% endif %}
        <th><button><a href="{% url 'todolist:status' todo.id %}">Change Status</a></button></th>
        <th><button><a href="{% url 'todolist:delete' todo.id %}">Delete Task</a></button></th>
    </tr>
    {% endfor %}
</table>

<br>
<button><a href="{% url 'todolist:create_task' %}">Create New Task</a></button>
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
<br>
<br>
{% endblock content %}
```
Isi dari create_task.html adalah sebagai berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Create Task</title>
{% endblock meta %}

{% block content %}
<form action="" method="post">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="Submit">
</form>
{% endblock content %}
```
7. Buka urls.py pada folder todolist dan impor semua fungsi yang sudah dibuat.
```
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import status
from todolist.views import delete
```
8. Tambahkan *path url* ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor.
```
...
path('', show_todolist, name='show_todolist'),
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('create-task/', create_task, name='create_task'),
path('status/<int:id>/', status, name='status'),
path('delete/<int:id>/', delete, name='delete'),
...
```
9. Lakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub.
10. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat. Kemudian membuat 2 user dengan masing-masing 3 dummy to do list. 