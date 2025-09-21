Name : Andrew Wanarahardja
NPM : 2406407373
Class : PBP A

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

------------------------------------------------------------------------------------------------

Soal Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Karena ada kalanya perlu ada transfer data antar stack. Juga bisa memudahkan jika ada keperluan untuk mengubah data yang sudah ada

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    JSON. JSON lebih populer dibandingkan XML karena filenya berupa text. Oleh karena itu, banyak platform men-support pembuatan file JSON. Selain itu, file JSON juga mudah dibaca dan dimengerti

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    fungsi dari method is_valid adalah untuk memastikan form diisi dengan data yang valid. Method tersebut dibutuhkan untuk menghindari error ketika data diproses dengan nilai yang tidak valid atau dengan data type yang tidak sesuai

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token (cross site request forgery token) adalah sebuah token yang unik terhadap sesi user.token ini perlu dimiliki ketika user tersebut mengirim form. dibutuhkan untuk memastikan request isinya benar, dan berasal dari sumber yang benar. Jika tidak ditambahkan, maka hacker bisa menyerang melalui user karena tidak ada token yang memastikan bahwa pengirim form adalh user tersebut dan bukan hacker. 


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Penambahan fungsi di views.py pada direktori main secara garis besar dilakukan dengan mengambil semua produk yang ada, menggantinya menjadi bentuk xml atau json, lalu mengembalikan sebuah respons http. untuk yang menampilkan produk tertentu saja, dilkukan filter terlebih dahulu dan mengembalikan respons 404 not found jika tidak ditemukan

    lalu dilakukan routing dengan menambahkan path untuk masing masing fungsi kepada urls.py pada direktori main

    untuk penambahan button add dan details, dilakukan penambahan pada main.html yang berada di dalam direktori templates pada direktori main. sebelum pembuatan button tersebut, ditambahkan sebuah refernce ke halaman untuk menambahkan produk untuk button atau detail produk untuk button details agar bisa mengakses halaman tersebut ketika menekan buttonnya.

    Pembuatan form untuk menambahkan objek model bisa dilakukan dengan membuat forms.py pada direktori main dan mengimport Product dari models.py. lalu tuliskan field apa saja yang perlu diisi pada saat pembuatan. tidak harus semuanya field dari model diisi karena ada field yang sudah memiliki default value. data dari forms.py tersebut digunakan oleh add_product.html untuk menampilkan halaman penambahan produk

    Untuk membuat halaman yang berisi detail produk, perlu dibuat product_detail.html yang berisi infromasi dari produk yang ingin dilihat detailnya. Untuk menampilkan halaman ini, telah dibuat button 'Details' pada main.html 

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Good. Very helpful.

url show_xml :
https://andrew-wanarahardja-1610943.postman.co/workspace/Andrew-Wanarahardja's-Workspace~b8cd5790-2b5f-4747-8c0c-3c1ab66cd1b2/request/48319398-223ae9e0-7a92-415e-8bee-2b5eb595d250?historyId=48319398-844aa881-f995-46d4-a96c-0c42dbf325e8&utm_source=postman&utm_medium=response_tab&utm_campaign=core&utm_content=link

url show_json :
https://andrew-wanarahardja-1610943.postman.co/workspace/Andrew-Wanarahardja's-Workspace~b8cd5790-2b5f-4747-8c0c-3c1ab66cd1b2/request/48319398-223ae9e0-7a92-415e-8bee-2b5eb595d250?historyId=48319398-53a8c868-b7c1-481f-ab57-ce7c90f7b69f&utm_source=postman&utm_medium=response_tab&utm_campaign=core&utm_content=link

url show_xml_by_id :
https://andrew-wanarahardja-1610943.postman.co/workspace/Andrew-Wanarahardja's-Workspace~b8cd5790-2b5f-4747-8c0c-3c1ab66cd1b2/request/48319398-223ae9e0-7a92-415e-8bee-2b5eb595d250?historyId=48319398-777232c0-6baa-4e6a-bb0b-648d50a3d96b&utm_source=postman&utm_medium=response_tab&utm_campaign=core&utm_content=link

url show_json_by_id :
https://andrew-wanarahardja-1610943.postman.co/workspace/Andrew-Wanarahardja's-Workspace~b8cd5790-2b5f-4747-8c0c-3c1ab66cd1b2/request/48319398-223ae9e0-7a92-415e-8bee-2b5eb595d250?historyId=48319398-57cf3041-892b-49cd-b6fb-9d75fe142066&utm_source=postman&utm_medium=response_tab&utm_campaign=core&utm_content=link

------------------------------------------------------------------------------------------------

Soal Tugas 4 : 
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    Django AuthenticationForm adalah sebuah fungsi yang digunakan untuk login. Dengan memasukkan password untuk memastikan bahwa user yang melakukan login benar orang tersebut dan bukan orang lain yang menggunakan nama user tersebut. Django AuthenticationForm termasuk cukup aman, bisa menahan brute-force attack. selain itu, banyak tersedia juga dokumentasi, sehingga ketika mencari informasi tentang suatu bagian pasti ada dokumentasinya. Django AuthenticationForm juga bisa dimodifikasi dengan berbagai hal, walaupun akan memerlukan banyak waktu untuk memahami semua hal yang bisa dilakukan. Lalu, Django AuthenticationForm juga dibuat secara generik (tidak spesifik), sehingga mungkin tidak men-support autentikasi yang lebih spesifik

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    autentikasi adalah proses menentukan apakah benar? apakah benar anda orang yang anda bilang anda adalah? Sedangkan otorisasi adalah menentukan tingkat kekuasaan yang dimiliki suatu user ketika sudah dipastikan identitasnya. autentikasi bisa dilakukan dengan form login untuk memastikan identitas user, dan otorisasi bisa dilakukan dengan mengecek jika user tersebut memiliki otoritas yang diperlukan (contoh : user.has_perm()) 

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Session biasanya berisi data yang tidak bersifat tahan-lama, dan akan hilang ketika sesi berakhir. Sedangkan cookies biasanya digunakan untuk data yang bersifat lebih permanen. Namun, sifat permanen tersebut juga berarti bahwa data tersebut harus disimpan di suatu tempat dan memakan ruang penyimpanan, sedangkan data session yang hilang ketika sesi berakhir tidak.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Penggunaan cookies bisa digunakan untuk mencatat data dari suatu sesi, namun, data tersebut bisa saja diambil tanpa permisi dari pengguna. dan bisa juga menjadi salah satu titk penyerangan oleh hacker dengan cross site scripting (XSS). Django menangani hal tersebut dengan beberapa cara. Diantaranya dengan menggunakan cookie yang aman, dan hanya dikirim melalui https (http secure) dan menggunakan csrf token sebagai validasi. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
        untuk mengimplemetasikan registrasi, login, dan logout, harus dilakukan import dari modul yang tersedia di Django. Mengimport ke dalam views.py, UserCreationForm dan AuthenticationForm dari django.contrib.auth.forms dan login dan logout dari django.contrib.auth. lalu membuat fungsi untuk melakukan register, login, ataupun logout, dan menampilkan halaman html dan redirection setelahnya. Lalu dibuat halaman html yang akan ditampilkan. Dan terakhir, membuat routing dari urls.py.

    b. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
        Setelah dibuat fungsi untuk register user, login dan logout, dibuat 2 user. dan masing masing user menambahkan 3 produk dengan menekan tombol Add Product dan mengisi form yang berisi informasi tentang produk tersebut.

    c. Menghubungkan model Product dengan User.
        Pada models.py, import user dari django.contrib.auth.models. lalu pada product, dobuat suatu foreign key yaitu user. Hal ini menghubungkan model dengan user dengan membuat nama user sebagai salah satu data yang tersimpan oleh setiap objek Products. Hal ini bisa digunakan dalam berbagai cara, seperti Mencantumkan nama penjual, melakukan filter terhadap produk yang ditampilkan, dan lainnya.

    d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
        Penampilan username dan informasi last_login bisa dilakukan dengan modifikasi pada view.py pada direktori main. Data tentang username bisa didapatkan dengan request.user.username. Sedangkan data untuk waktu terakhir login bisa dilakukan dengan mengambil timestamp sebagai cookie setiap kali dilakukan login. Dilakukan penambahan username dan last_login pada dictionary, pada show_main (fungsi yang menampilkan halaman utama). Setelah itu dilakukan penambahan pada main.html yang menampilkan perubahan tersebut