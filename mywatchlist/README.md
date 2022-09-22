# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 \
**Nama  : Nadira Maysa Dyandra** \
**NPM   : 2106632232** \
**Kelas : A**

## Tautan Aplikasi Heroku
Berikut adalah tautan menuju hasil lab: \
https://tugas2nadira.herokuapp.com/mywatchlist/html \
https://tugas2nadira.herokuapp.com/mywatchlist/xml \
https://tugas2nadira.herokuapp.com/mywatchlist/json

## Perbedaan JSON, XML, dan HTML
**JSON**
- Mendukung semua browser
- Data dapat disimpan dalam bentuk array dan memudahkan untuk transfer data
- Ukuran sintaks kecil sehingga lebih ringan
- Mendukung banyak bahasa pemrograman lain
- Parsing data di sisi server lebih cepat
- Unggul dalam penanganan API, baik untuk aplikasi berbasis web maupun dektop

**XML**
- Memiliki tag atau data yang tidak terpakai atau kosong
- Ukuran dokumen dan file besar
- Bersifat case sensitive
- Berfungsi untuk menyimpan dan mengirimkan data
- Terdiri dari data struktural
- Bersifat dinamis karena digunakan untuk mentransfer data

**HTML**
- Bersifat case sensitive
- Berfungsi menampilkan data
- Tidak terdiri dari data struktural
- Bersifat statis karena fungsi utamanya menampilkan data
- Harus menggunakan tag tertentu dan tidak memerlukan tag penutup

## Pentingnya *data delivery*
Seiring dengan perkembangan aplikasi, semakin banyak data dengan beragam jenis dan format.  
Data delivery memungkinkan kita untuk mengirimkan data dari satu *stack* ke *stack* lainnya di dalam suatu platform. 
Sehingga, adanya Data Delivery akan membantu aplikasi-aplikasi yang berada di atas platform untuk saling bertukar informasi (memudahkan proses perpindahan data).  

## Implementasi Checklist
1. Membuat aplikasi mywatchlist dengan perintah berikut.
```
python manage.py startapp wishlist
```
2. Menambahkan aplikasi mywatchlist ke dalam INSTALLED_APPS pada settings.py
```
INSTALLED_APPS = [
    .....,
    'mywatchlist',
    .....,
]
```
3. Membuat models.py pada folder mywatchlist untuk membuat model dengan fields watched, title, rating, release_date, dan review.
4. Lakukan perintah berikut di terminal untuk mempersiapkan migrasi skema model ke dalam *database* Django lokal.
```
python manage.py makemigrations
```
5. Lakukan perintah berikut di terminal untuk menerapkan skema model yang telah dibuat ke dalam *database* Django lokal. 
```
python manage.py migrate
```
6. Menambahkan data yang ingin ditampilkan pada file initial_watchlist_data.json pada folder fixtures di dalam folder mywatchlist. \
7. Menjalankan perintah berikut untuk memuat data ke dalam *database* Djangko lokal.
```
python manage.py loaddata initial_watchlist_data.json
```
8. Membuat fungsi-fungsi yang dibutuhkan untuk mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat.
```
def show_watchlist(request):
    .........
def show_xml(request):
    .........
def show_json(request):
    .........
def show_html(request):
    .........
```
9. Membuat folder bernama templates di dalam folder aplikasi mywatchlist dan tambahkan file watchlist.html ke dalamnya.
```
{% extends 'base.html' %}

{% block content %}
<h1>Lab 2 Assignment PBP/PBD</h1>

<h5>Nama: </h5>
<b>{{nama}}</b>
<h5>Student ID: </h5>
<p>{{NPM}}</p>

<table>
    <tr>
        <th>Sudah/Belum</th>
        <th>Judul</th>
        <th>Rating</th>
        <th>Tanggal Rilis</th>
        <th>Review</th>
    </tr>
    {% comment %} Mencetak data ke dalam tabel {% endcomment %}
    {% for film in list_tontonan %}
    <tr>
        <th>{{film.watched}}</th>
        <th>{{film.title}}</th>
        <th>{{film.rating}}</th>
        <th>{{film.release_date}}</th>
        <th>{{film.review}}</th>
    </tr>
    {% endfor %}
</table>

{% endblock content %}
```
10. Membuat routing ke fungsi pada file views.py dengan cara menambahkan file urls.py pada folder mywatchlist sebagai berikut.
```
from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_json, name='show_html'),
]
```
11. Daftarkan aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut.
```
...
path('mywatchlist/', include('mywatchlist.urls')),
...
```
12. Lakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub.\
13. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat. Pada tahap ini memerlukan sedikit konfigurasi pada aplikasi Heroku. Yaitu, perlu memuat ulang file initial_watchlist_data.json secara manual pada run console di dalam aplikasi yang telah dibuat di Heroku.
```
python manage.py loaddata initial_watchlist_data.json
```
## Postman
**Akses HTML**
![](/Assets/PostMan-HTML.png)
**Akses XML**
![](/Assets/PostMan-XML.png)
**Akses JSON**
![](/Assets/PostMan-JSON.png)