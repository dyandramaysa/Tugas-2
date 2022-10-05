# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 \
**Nama  : Nadira Maysa Dyandra** \
**NPM   : 2106632232** \
**Kelas : A**

## Tautan Aplikasi Heroku
Berikut adalah tautan menuju hasil lab: \
https://tugas2nadira.herokuapp.com/todolist \
https://tugas2nadira.herokuapp.com/todolist/register \
https://tugas2nadira.herokuapp.com/todolist/login \
https://tugas2nadira.herokuapp.com/todolist/logout \
https://tugas2nadira.herokuapp.com/todolist/create-task 

## Internal, Eksternal, dan Inline CSS
1. **Internal CSS** \
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML.
Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
Internal CSS ini dapat digunakan untuk membuat tampilan yang unik pada setiap halaman website. \
**Kelebihan Internal CSS**
    - Perubahan pada Internal CSS hanya berlaku pada satu halaman saja
    - Pengembang tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file
    - Class dan ID dapat digunakan oleh internal stylesheet \
**Kekurangan Internal CSS** 
    - Tidak efisien jika ingin menggunakan CSS yang sama dalam beberapa file
    - Membuat performa website lebih lambat karena CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali user mengganti halaman website
2. **Eksternal CSS** \
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ini ditulis pada sebuah file khusus berekstensi .css. 
File eksternal CSS ini biasanya diletakkan setelah bagian <head> pada halaman. 
Aplikasi eksternal CSS ini lebih sederhana dan simpel dibandingkan dengan menambahkan kode CSS di setiap elemen HTML yang ingin di atur tampilannya. \
**Kelebihan Eksternal CSS** 
    - Ukuran file HTML lebih kecil
    - Struktur kode HTML lebih rapih
    - Loading website menjadi lebih cepat
    - File CSS dapat digunakan di beberapa halaman website sekaligus \
**Kekurangan Eksternal CSS** 
    - Halaman bisa menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML. Hal ini biasanya terjadi akibat koneksi internet yang lambat. 
3. **Inline CSS** \
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. 
Cara ini kurang efisien karena setiap tak HTML yang diberikan perlu memiliki style masing-masing. Hal ini akan membuat pengembang lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. 
Sebab, Inline CSS hanya digunakan untuk mengubah satu elemen saja. \
**Kelebihan Inline CSS** 
    - Sangat membantu jika pengembang hanya ingin menguji dan melihat perubahan pada satu elemen
    - Dapat memperbaiki kode dengan cepat
    - Proses permintaan HTTP yang lebih kecil akan menyebabkan load website lebih cepat \
**Kekurangan Inline CSS** 
    - Tidak efisien, karena Inline style CSS hanya dapat diterapkan pada satu elemen HTML saja.

## Tag HTML5
**Apa itu HTML?** \
Sebelum membahas tentang HTML5, kita harus memahami terlebih dahulu pengertian dari HTML itu sendiri. HTML atau Hyper Text Markup Language terdiri dari kata Hyper Text yang berarti sebuah teks pada suatu halaman yang memiliki kemampuan untuk dapat terhubung dengan teks pada suatu halaman yang lain dan Markup Language yang berarti HTML ini tersusun atas tak-tak markup dan setiap tak pada HTML menjelaskan perintah isi dokumen yang berbeda-beda. 
Dengan demikian, HTML ini digunakan untuk membuat dasar dari sebuah halaman web dengan memberi struktur, menghubungkan teks/tautan antar halaman, dan membagikan informasi yang terkait dengan sebuah halaman web. \
\
**Cara Kerja HTML** \
Pada dasarnya, HTML ditujukan untuk menampilkan elemen-elemen yang terdapat pada suatu halaman website. Setiap elemen ini ditunjukkan dengan tag <> sebagai pembuka dan tag </> sebagai penutup.
Kedua tag tersebut berisi inisial yang mewakili sebuah elemen halaman website. Contohnya adalah < p > yang merepresentasikan sebuah paragraf yang bisa diketikkan pada sebuah HTML editor.
Namun, agar memiliki konten, pengembang perlu memasukkan teks di antara tag < p > dan < p/ >. Dengan demikian, pengembang telah membuat sebuah paragraf. \
\
**HTML5** \
HTML5 adalah singkatan dari Hyper Text Markup Language Versi 5. Dengan kata lain, HTML5 adalah perbaikan dari HTML. Versi ini diciptakan untuk menunjang berbagai kebutuhan pengembangan website saat ini, misalnya dukungan untuk membuat website yang bersifat mobile-friendly.
HTML5 menggunakan syntax yang lebih sederhana dibandingkan dengan HTML, sehingga pengembang dapat membuat struktur halaman website yang kompleks secara lebih mudah. Selain itu, HTML5 juga memiliki banyak keunggulan lainnya. Misalnya sebagai berikut.
- Penanganan error yang lebih baik
- Kemudahan untuk membuat aplikasi web
- Syntax yang lebih sederhana
- Dukungan untuk pembuatan website yang responsif
- Dukungan untuk konten audio dan video
- Kompatibel dengan lebih banyak browser
- Penyimpanan informasi secara lokal
- Fokus otomatis pada kolom form
- Menjalankan JavaScript pada web Browser
## CSS Selector
**CSS** \
CSS atau Cascading Style Sheet adalah bahasa yang digunakan untuk mengatur tampilan elemen dalam bahasa markup. Fungsi CSS adalah untuk memisahkan teks atau konten dari tampilan visual pada situs. 
Melalui CSS, pengembang dapat mengatur tampilan pada seluruh aspek dalam berkas yang berbeda. Selain itu, pengembang juga dapat menentukan style dan mengintegrasikannya di atas markup HTML. Adapun, proses penentuan style membutuhkan suatu CSS selector yang dapat memengaruhi cara kerja CSS. \
\
**CSS Selector** \
Selector pada CSS digunakan untuk menargetkan elemen HTML di halaman web yang diberi style. Dengan kata lain, CSS selector adalah serangkaian aturan dari CSS yang berfungsi untuk memilihi suatu elemen yang ingin diberi style. \
\
**Jenis-jenis Selector** 
1. Universal Selector
    Selector ini merupakan selector yang sering digunakan untuk menyeleksi dan memilih semua elemen pada suatu dokumen HTML. Pemrogram umumnya menggunakan universal selector pada awal penulisan dokumen CSS untuk mengatur ulang style bawaan dari browser. Untuk membuatnya, kita memerlukan tanda bintang (*). Contoh kodenya adalah sebagai berikut.
    ```
    * {
        border: 1px dashed black;
        color: pink;
    }
    ```
    Kode di atas akan membuat semua elemen pada HTML memiliki border berupa garis tepi patah-patah berwarna hitam dan teks berwarna merah muda.
2. Tag Selector
    Selector ini merupakan selector yang memilih elemen berdasarkan nama tag-nya. Selektor ini juga sering disebut type selector. Untuk membuatnya, kita memerlukan nama tag. Contoh kodenya adalah sebagai berikut.
    ```
    h1{
        color: green;
    }
    ```
    Kode di atas akan membuat teks pada seluruh elemen < h1 > berwarna hijau.
3. ID Selector
    Selector ini merupakan selector yang bersifat unik. Dengan kata lain, ID selector hanya dapat digunakan untuk satu elemen saja. Untuk membuatnya, kita memerlukan tanda pagar (#). Contoh kodenya adalah sebagai berikut. 
    ```
    #first-header{
        background-color: black;
        color: pink;
    }
    ```
    Kode di atas hanya akan mengubah style pada first-header.
4. Class Selector
    Cara kerja selector ini mirip dengan ID selector. Bedanya, selector ini tidak bersifat unik dan untuk membuatnya kita memerlukan tanda titik (.). Karena tidak bersifat unik, maka satu class selector dapat digunakan berulang kali pada lebih dari satu elemen HTML. Selain itu, satu elemen HTML dapat menampung lebih dari satu class selector. Contoh kodenya adalah sebagai berikut.
    ```
    .btn-primary{
        background-color: lightblue;
        color: white;
    }
    ```
5. Atribut Selector
    Selector ini merupakan selector yang memilih elemen berdasarkan tag dan atributnya. Contoh kodenya adalah sebagai berikut.
    ```
    a[title] {
        background-color: black;
        color: pink;
        padding: 5px;
        text-decoration: none;
        border-radius: 5px;
    }
    ```
## Langkah Implementasi Tugas 5
1.  Buka file base.html yang berada pada folder templates. Tambahkan kode-kode berikut pada file.
    ```
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
	
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>

    <!-- fonts google -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- Iconscout CSS -->
    <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
    ```
    Sehingga isi file menjadi seperti berikut.
    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <title>Nadira Maysa Dyandra</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- fonts google -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Iconscout CSS -->
    <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
    
    <!-- style -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    {% block meta %}
    {% endblock meta %}
    </head>

    <body>
    {% block content %}
    {% endblock content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
    </body>

    </html>
    ```
2.  Buka folder templates yang berada di dalam folder todolist. Lakukan perubahan pada masing-masing file html yang berada didalamnya agar tampilan pada website sesuai dengan keinginan.