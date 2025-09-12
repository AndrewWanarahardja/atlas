Name : Andrew Wanarahardja
NPM : 2406407373
Class : PBP A

12 Sep 2025
waktu yang tertulis di pws karena ini dibuat ulang akhibat adanya error
sama dengan catatan commit di github, ini menggunakan repository baru
link repository lama : https://github.com/AndrewWanarahardja/shop

Soal Tugas 2 :
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Pembuatan project django baru bisa dilakukan dengan membuat direktori baru, mengaktifkan virtual
        environment. Lalu menambah berkas seperti .env, .env.prod, .gitignore, requirements.txt. setelah itu perlu menginstall requirements dari requirements.txt. perlu dilakukan migrate untuk langkah awal membuat database. start project django lalu bisa dilakukan dengan perintah    python manage.py startproject .

    pembuatan aplikasi dengan django bisa dilakukan dengan perintah python manage.py startapp main 
        dengan main sebagai nama aplikasi yang dibuat

    untuk melakukan routing ke aplikasi main, pertama aplikasi tersebut harus ditambahkan ke dalam list
        of applications pada berkas settings.py. lalu pada berkas urls.py tingkat project, ditambah sebuah url pattern dengan fungsi path yang mengarahkan request ke urls.py pada tingkat aplikasi dalam aplikasi main 

    pada models.py membuat model dengan melakukan assignment field tertentu terhadap suatu       
        variable sesuai spesifikasi yang diminta tugas

    membuat sebuah fungsi yang mengembalikan nilai nama toko, nama, npm, dan kelas. digunakan untuk 
        mengubah nilai yang ditampilkan di main.html. fungsi path mengambil beberapa argumen, termasuk sebuah dictionary. jika salah satu key dari dictionary tersebut berada dalam dua kurung kurawal seperti {{ dictKey }} maka akan tampil value dari key tersebut pada website

    fungsi show_main pada views.py untuk mengembalikan data ke template html dilakukan dengan fungsi 
        render. untuk melakukan hal tersebut fungsi render mengambil argumen request, file html yang dijadikan template, dan sebuah dictionary yang digunakan untuk menggantikan informasi pada tempat yang tertulis di file html
    
    untuk membuat routing pada urls.py pada aplikasi main, digunakan fungsi path. fungsi path digunakan
        untuk memberi tahu ke mana alurnya bergerak ketika ada url cocok yang masuk. ingin dilakukan routing ke views.py untuk dijalankan fungsi show_main, maka show_main dijadikan argumen kedua pada fungsi path

    deployment ke pws bisa dilakukan dengan membuka pbp.cs.ui.ac.id dan membuat project baru, isi data yang diperlukan, dan menyimpan credentials. Lalu salin isi .env.prod ke dalam raw editor. ikuti langkah url deployment yang tertera pada pws. update allowed_hosts untuk bisa menjalankan server

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Bagan :
    url request --> url.py --> views.py --> models.py --> database 
    --> models.py --> view.py -- > template.py --> output

    Penjelasan : 
    ketika seorang user mengetik url, masuk ke urls.py yang memastikan url yang ditulis benar. Jika 
        benar, lanjut ke views.py. views.py mengirim querysets ke models.py dan models.py berinteraksi dengan database untuk mengembalikan resultset ke views.py. informasi yang didapat lalu ditampilkan berdasarkan format dalam main.html dalam direktori templates.

3. Jelaskan peran settings.py dalam proyek Django!
    Fungsi settings.py adalah menentukan database, menentukan siapa yang bisa melakukan launch server, 
        men-enable dan disable mode debugging, mencatat app apa saja yang ada dalam project.

4. Bagaimana cara kerja migrasi database di Django?
    mengubah databse berdasarkan perubahan yang dibuat pada models.py
    python manage.py makemigrations : membuat file pada migrations yang mendeskripsikan perubahan
                                      yang akan dilakukan
    python manage.py migrations : mengubah database berdasarkan perubahan pada models.py

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Karena django berdasarkan python yang relatif mudah untuk digunakan, mengikuti struktur MVT
    jadi lebih jelas dan terstruktur.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    No comment, cuz it was online