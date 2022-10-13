# Tugas 6: Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 \
**Nama  : Nadira Maysa Dyandra** \
**NPM   : 2106632232** \
**Kelas : A**

## Asynchronus dan Synchronus Programming
### Asynchronus  Programming
*Asynchronus  programming* merupakan arsitektur *non-blocking* yang berarti tidak memblokir eksekusi lebih lanjut saat satu atau lebih operasi sedang berlangsung. Dengan demikian, pada program yang bersifat *asynchronus*, beberapa operasi terkait dapat berjalan secara bersamaan tanpa menunggu tugas lain selesai. <br>
Salah satu contoh penerapan *asynchronus  programming* adalah SMS. Ketika A mengirim pesan kepada B, B dapat merespons kapanpun. Sementara itu,  A dapat melakukan hal lain sambil menunggu tanggapan dari B. 
### Synchronus Programming
*Synchronus programming* merupakan arsitektur pemblokian yang mengikuti serangkaian urutan yang ketat. Hal ini mengindikasikan bahwa operasi dilakukan satu per satu, dalam urutan yang sempurna. Jika suatu operasi sedang dilakukan, maka instruksi operasi lainnya diblokir.
### Asynchronus dan Synchronus Programming
- *Asynchronus* adalah *multi-thread*, yaitu operasi atau program dapat berjalan secara paralel. Sedangkan, *synchronus* adalah *single-thread*, yaitu hanya satu operasi atau program yang akan berjalan pada satu waktu.
- *Asynchronus* meningkatkan *throughput* karena beberapa operasi dapat berjalan secara bersamaan. Sedangkan *synchronus* lebih lambat dan lebih metodis.

## Event-Driven Programming
*Event-driven* merupakan suatu teknik pemrograman yang alur programnya ditentukan oleh suatu peristiwa atau *event* yang merupakan keluaran atau tindakan pengguna, atau dapat berupa pesan dari program lainnya. <br>

Kemudian, berikut adalah komponen-komponen pada *event-driven programming*:
1. **Event**, yaitu sebuah kejadian atau aksi yang muncul pada sebuah sistem yang dapat dipicu oleh berbagai hal, misalnya penekanan tombol, *timer*, atau nilai pembacaan sensor yang melebihi batas tertentu. 
2. **Trigger**, yaitu sebuah fungsi yang memiliki kesesuaian dengan kejadian. Misalnya, fungsi ketika tombol ditekan dan fungsi ketika *timer* menunjukkan nilai tertentu.
3. **Event handler**, yaitu komponen yang melakukan aksi ketika sebuah *event* terjadi.
4. **Event loop**, yaitu komponen yang berfungsi untuk mencari *event-event* yang ada pada sebuah sistem.
5. **Event-driven**, program yang memiliki input, proses, dan output.

### Contoh Penerapannya
- Ketika tombol A ditekan, maka teks pada heading pertama akan berubah warna menjadi warna biru. 
- Ketika tombol B ditekan, maka halaman website diperbesar

## Penerapan Asynchronus Programming pada AJAX
AJAX atau *Asynchronous JavaScript And XML* menggunakan browser untuk meminta data dari *web server* dan JavaScript serta HTML DOM untuk menampilkan data. AJAX dapat menggunakan XML untuk mengirim data tetapi dapat juga menggunakan teks ataupun JSON. AJAX membuat halaman web memperbaharui data secara asinkronus dengan mengirim data ke server di balik layar. Dengan demikian kita dapat memperbaharui sebagian elemen data pada halaman tanpa harus me-*reload* keseluruhan halaman. <br>

Cara kerja AJAX adalah sebagai berikut. 
1. Sebuah event terjadi pada halaman web 
2. Sebuah `XMLHttpRequest` object dibuat oleh JavaScript
3. `XMLHttpRequest` object mengirimkan request ke server
4. Server memproses request tersebut
5. Server mengembalikan response kembali kepada halaman web
6. Response dibaca oleh JavaScript
7. Aksi berikutnya akan dipicu oleh JavaScript sesuai dengan langkah yang dibuat 

Contoh implementasinya adalah sebagai berikut.
```
<script>
    function update(pk) {
        $.post({
            url: `status/${pk}/`,
            type: 'post',
            data: {},
            success: showTodos
        })
    }

    function deleteTask(pk) {
        $.post({
            url: `delete/${pk}/`,
            type: 'post',
            data: {},
            success: showTodos
        })
    }

    function createTask() {
        $.post({
            url: `add/`,
            type: 'post',
            data: {
                'title': $('#title-controller').val(),
                'description': $('#description-controller').val(),
            },
            success: showTodos
        })
    }
    $(`#save-task`).attr('onclick', `createTask()`);

    function showTodos() {
        $.get(
            './json',
            function (data) {
                $('#todos-container').empty();
                for (let i = 0; i < data.length; i++) {
                    $('#todos-container').append(
                        `<div  class="col-md-4">
                            <div class="card">
                                <h2 class="card-title">${data[i].fields.title}</h2>
                                <h3 class="card-date">${data[i].fields.date}</h3>
                                <p class="card-text">${data[i].fields.description}</p>
                                <p id="todo-mark-${i}" class="card-text"></p>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item satu">
                                        <button type="button" onclick="" id="status-button-${i}" class="button">Change Status</button>
                                    </li>
                                    <li class="list-group-item dua">
                                        <button type="button" onclick="" id="delete-button-${i}" class="button">Delete Task</button>
                                    </li>
                                </ul>
                            </div>
                        </div>`
                    )
                    if (data[i].fields.is_finished) {
                        $(`#todo-mark-${i}`).addClass('text-green-500').text('Selesai');
                    } else {
                        $(`#todo-mark-${i}`).addClass('text-red-600').text('Belum Selesai');
                    }
                    $(`#status-button-${i}`).attr('onclick', `update(${data[i].pk})`);
                    $(`#delete-button-${i}`).attr('onclick', `deleteTask(${data[i].pk})`)
                }
            }
        )
    }

    showTodos();
</script>
```
## Implentasi Tugas 6
1. Membuat *view* baru yang mengembalikan seluruh data task dalam bentuk JSON.
    ```
    ...
    from django.http import HttpResponse
    from django.core import serializers
    ...
    @login_required(login_url='/todolist/login/')
    def show_json(request):
        data = Task.objects.filter(user=request.user).order_by('id')
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
2. Membuat *path* `/todolist/json` yang mengarah ke *view* yang baru pada  urls.py yang ada dalam folder todolist.
    ```
    ...
    from todolist.views import show_json
    ...
    urlpatterns = [
        ...
        path('json/', show_json, name='show_json'),
    ]
    ``` 
3. Membuat *view* baru untuk menambahkan task baru ke dalam *database*
    ```
    ...
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    ...
    @login_required(login_url='/todolist/login/')
    @csrf_exempt
    def create_task_AJAX(request):
        if request.method == "POST":
            user = request.user
            title = request.POST.get('title')
            description = request.POST.get('description')

            Task.objects.create(user=user,title=title, description=description)
        return JsonResponse({'error': False, 'msg':'Successful'})
    ```
4. Membuat *path* `/todolist/add` yang mengarah ke *view* yang baru dibuat. 
    ```
    ...
    from todolist.views import create_task_AJAX
    ...
    urlpatterns = [
        ...
        path('add/',create_task_AJAX, name='create_task_AJAX'),
    ]
    ```
6. Melakukan beberapa perubahan di bagian `{% block content %}` pada dokumen todolist.html yang ada pada folder templates seperti yang dilakukan pada step berikutnya.
7. Menambahkan *script* berikut sebelum masuk ke dalam bagian *body*
    ```
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    ```
8. Membuat sebuah tombol `Add Task` yang membuka sebuah modal dengan form untuk menambahkan task. Sehingga bagian *body* pada html menjadi sebagai berikut.
    ```
    <body>
        <section class="p-5">
            <div class="container">
                <h1>Halo {{user}}!</h1>
                <div class="d-grid gap-2 d-md-block">
                    <button class="btn-1"><a href="{% url 'todolist:create_task' %}" class="a1">Create New Task</a></button>
                    <button class="btn-1"><a href="{% url 'todolist:logout' %}" class="a1">Logout</a></button>
                    <!-- Button trigger modal -->
                    <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Task</button>    
                </div>
                
                <!-- Modal -->
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Create Task</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form method="POST" action="">
                                {% csrf_token %}
                                <div class="mt-4">
                                    <label for="Title">Title</label>
                                </div>
                                <input id="title-controller" type="text" name="title" placeholder="Title" required class="form-control">
                                <div class="mt-4">
                                    <label for="description">Description</label>
                                </div>
                                <textarea id="description-controller" name="description" placeholder="Description" cols="30" rows="10" class="form-control" required></textarea>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button id="save-task" type="submit" class="btn btn-primary" value="Submit" onclick="">Save changes</button>
                                </div>
                            </form>
                        </div>
                    </div>
                    </div>
                </div>
                <!-- card  -->
                <div id="todos-container" class="row text-center g-4">
                    
                </div> 
            </div>
        </section>
    </body>
    ```
9. Melakukan sedikit perubahan pada fungsi status dan delete yang ada pada views.py.
    ```
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
    ```
10. Lakukan pengambilan task menggunakan AJAX GET dan implementasi beberapa fungsi lainnya dengan menambahkan kode berikut di dalam `{% block content %}` pada dokumen todolist.html.
    ```
    <script>
        function update(pk) {
            $.post({
                url: `status/${pk}/`,
                type: 'post',
                data: {},
                success: showTodos
            })
        }

        function deleteTask(pk) {
            $.post({
                url: `delete/${pk}/`,
                type: 'post',
                data: {},
                success: showTodos
            })
        }

        function createTask() {
            $.post({
                url: `add/`,
                type: 'post',
                data: {
                    'title': $('#title-controller').val(),
                    'description': $('#description-controller').val(),
                },
                success: showTodos
            })
        }
        $(`#save-task`).attr('onclick', `createTask()`);

        function showTodos() {
            $.get(
                './json',
                function (data) {
                    $('#todos-container').empty();
                    for (let i = 0; i < data.length; i++) {
                        $('#todos-container').append(
                            `<div  class="col-md-4">
                                <div class="card">
                                    <h2 class="card-title">${data[i].fields.title}</h2>
                                    <h3 class="card-date">${data[i].fields.date}</h3>
                                    <p class="card-text">${data[i].fields.description}</p>
                                    <p id="todo-mark-${i}" class="card-text"></p>
                                    <ul class="list-group list-group-flush">
                                        <li class="list-group-item satu">
                                            <button type="button" onclick="" id="status-button-${i}" class="button">Change Status</button>
                                        </li>
                                        <li class="list-group-item dua">
                                            <button type="button" onclick="" id="delete-button-${i}" class="button">Delete Task</button>
                                        </li>
                                    </ul>
                                </div>
                            </div>`
                        )
                        if (data[i].fields.is_finished) {
                            $(`#todo-mark-${i}`).addClass('text-green-500').text('Selesai');
                        } else {
                            $(`#todo-mark-${i}`).addClass('text-red-600').text('Belum Selesai');
                        }
                        $(`#status-button-${i}`).attr('onclick', `update(${data[i].pk})`);
                        $(`#delete-button-${i}`).attr('onclick', `deleteTask(${data[i].pk})`)
                    }
                }
            )
        }
        showTodos();
    </script>
    ```
