# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 \
**Nama  : Nadira Maysa Dyandra** \
**NPM   : 2106632232** \
**Kelas : A**

## Tautan Aplikasi Heroku
Berikut adalah tautan menuju hasil lab: 
https://tugas2nadira.herokuapp.com/mywatchlist/

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

## Implementasi Checklist
1. Membuat aplikasi mywatchlist dengan perintah
```
python manage.py startapp wishlist
```
2. Membuat models.py pada folder mywatchlist untuk membuat object
3. Lakukan perintah 
```
python manage.py makemigrations
```
untuk mempersiapkan migrasi skema model ke dalam *database* Django lokal \
4. Lakukan perintah 
```
python manage.py migrate
```
untuk menerapkan skema model yang telah dibuat ke dalam *database* Django lokal \
5. Memasukkan data melalui file initial_watchlist_data.json pada folder fixtures di dalam folder mywatchlist \
6. Menjalankan perintah 
```
python manage.py loaddata initial_watchlist_data.json
```
untuk memasukkan data ke dalam *database* Djangko lokal. \

## Postman