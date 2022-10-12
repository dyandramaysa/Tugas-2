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
...
```
## Implentasi Tugas 6
1. Membuat *view* baru yang mengembalikan seluruh data task dalam bengtuk JSON.
```
from django.http import HttpResponse
from django.core import serializers
...
data = Task.objects.all()
def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
2. Membuat *path* `/todolist/json` yang mengarah ke *view* yang baru.
3. Lakukan pengambilan task menggunakan AJAX GET.
4. Membuat sebuah tombol `Add Task` yang membuka sebuah modal dengan form untuk menambahkan task. 
5. Membuat *view* baru untuk menambahkan task baru ke dalam *database*
6. Membuat *path* `/todolist/add` yang mengarah ke *view* yang baru dibuat. 
