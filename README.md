# Praktikum 6

## Latihan 1

Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda.

```
import math

def a(x):
return x**2

def b(x, y):
return math.sqrt(x**2 + y**2)

def c(*args):
return sum(args)/len(args)

def d(s):
return "".join(set(s))
```

Penjelasan:
Lambda digunakan di sini untuk membuat fungsi-fungsi singkat dan ekspresif tanpa perlu mendefinisikan fungsi secara terpisah.

- `hitung_kuadrat`: Fungsi lambda untuk menghitung kuadrat dari suatu bilangan x.
- `hitung_miring`: Fungsi lambda untuk menghitung panjang sisi miring dari segitiga siku-siku dengan panjang sisi x dan y.
- `hitung_rata_rata`: Fungsi lambda untuk menghitung rata-rata dari sekumpulan angka yang diberikan sebagai argumen.
- `hapus_duplikat`: Fungsi lambda untuk menghapus duplikat karakter dalam string s dengan menggunakan konsep set dalam Python.

Hasil:
![1](https://github.com/ficzclay/praktikum7/assets/148204078/abdeda39-188c-4ec4-a8c8-3abcdbb6abfe)


## Tugas Praktikum

Tugas Praktikum

Buat program sederhana dengan mengaplikasikan penggunaan fungsi
yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
• Fungsi tambah() untuk menambah data
• Fungsi tampilkan() untuk menampilkan data
• Fungsi hapus(nama) untuk menghapus data berdasarkan nama
• Fungsi ubah(nama) untuk mengubah data berdasarkan nama

• Buat flowchart dan penjelasan programnya

Penjelasan:
- Program utama berjalan dalam sebuah loop yang terus berlanjut. Setiap iterasi dari loop, program akan menampilkan menu pilihan untuk pengguna, kemudian menjalankan fungsi yang sesuai berdasarkan pilihan pengguna.
- Jika pengguna memilih opsi 1, fungsi `tambah()` akan dijalankan untuk menambah data mahasiswa.
- Jika pengguna memilih opsi 2, fungsi `tampilkan()` akan dijalankan untuk menampilkan data mahasiswa.
- Jika pengguna memilih opsi 3, program akan meminta nama mahasiswa yang akan dihapus, kemudian menjalankan fungsi `hapus(nama)`.
- Jika pengguna memilih opsi 4, program akan meminta nama mahasiswa yang akan diubah, kemudian menjalankan fungsi `ubah(nama)`.
- Jika pengguna memilih opsi 5, program akan menampilkan pesan perpisahan dan keluar dari loop.
- Program ini menggunakan loop while True untuk menjaga agar program tetap berjalan hingga pengguna memilih untuk keluar. Program menyediakan antarmuka interaktif sederhana untuk mengelola data mahasiswa.



Berikut Hasilnya:
<br>
![hasil_1](https://github.com/ficzclay/praktikum7/assets/148204078/f12b6ad0-aade-4fd4-90ab-4e99bfb5bfee)



Tambah Data:
<br>
![2](https://github.com/ficzclay/praktikum7/assets/148204078/ad055794-585c-48da-8d66-fc6e6c4cd24d)




Lihat Data:
<br>
![read_data](https://github.com/ficzclay/praktikum7/assets/148204078/e4d20e6a-11de-4eef-ba51-e18ec096452f)

<br>


Hapus Data:
<br>
![3](https://github.com/ficzclay/praktikum7/assets/148204078/a6a70e5b-e83a-43fc-956c-6b8046528b50)



Ubah Data:<br>
![4](https://github.com/ficzclay/praktikum7/assets/148204078/d333598c-f46b-4717-b647-f44788a19d9a)


<br>

Keluar:<br>
![5](https://github.com/ficzclay/praktikum7/assets/148204078/c092e7bd-2b03-4cc2-8b91-dd5a6223eef8)


Flowchart:<br>
![6](https://github.com/ficzclay/praktikum7/assets/148204078/7566cb60-e3ff-4fc6-90ad-5aeaf18df42f)




## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir praktikum7
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# praktikum7 >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add .
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
contoh: praktikum6
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository

- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```
