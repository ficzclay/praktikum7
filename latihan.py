# Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda.

# Fungsi lambda untuk menghitung kuadrat dari x
a = lambda x: x**2

# Fungsi lambda untuk menghitung panjang sisi miring dari segitiga siku-siku dengan panjang sisi x dan y
b = lambda x, y: math.sqrt(x**2 + y**2)

# Fungsi lambda untuk menghitung rata-rata dari sekumpulan angka
c = lambda *args: sum(args)/len(args)

# Fungsi lambda untuk menghapus duplikat karakter dalam string s
d = lambda s: "".join(set(s))