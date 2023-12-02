# Inisialisasi dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Fungsi untuk menambah data mahasiswa
def tambah():
    while True:
        nama = input("Masukkan nama mahasiswa: ")
        if nama.isalpha():
            break
        else:
            print("Input tidak valid. Harap masukkan hanya huruf.")

    nilai = int(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa[nama] = nilai
    print(f"Data mahasiswa {nama} berhasil ditambahkan.")

# Fungsi untuk menampilkan daftar nilai mahasiswa
def tampilkan():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        print("Daftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"{nama}: {nilai}")

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data mahasiswa {nama} berhasil dihapus.")
    else:
        print(f"Tidak ada data mahasiswa dengan nama {nama}.")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    if nama in data_mahasiswa:
        nilai_baru = int(input(f"Masukkan nilai baru untuk mahasiswa {nama}: "))
        data_mahasiswa[nama] = nilai_baru
        print(f"Data mahasiswa {nama} berhasil diubah.")
    else:
        print(f"Tidak ada data mahasiswa dengan nama {nama}.")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        tampilkan()
    elif pilihan == '3':
        nama_hapus = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama_hapus)
    elif pilihan == '4':
        nama_ubah = input("Masukkan nama mahasiswa yang akan diubah: ")
        ubah(nama_ubah)
    elif pilihan == '5':
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")