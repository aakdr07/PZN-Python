# Menggunakan variabel

nama = "dennis" # -> hasilnya dennis
umur = 22
tinggi = 165.6
is_active = True

# kita bisa langsung menggunakan nama variabelnya:
print(nama) # -> hasilnya dennis

# Kalau ingin menggunakan beberapa variabel dalam print(), pisahkan dengan koma:

print(nama, umur, tinggi)

# variabel dalam operasi
# Variabel juga bisa digunakan dalam perhitungan.

panjang = 20
lebar = 10
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Variabel juga bisa digunakan untuk menggabungkan String:
nama_depan = "budi"
nama_belakang = "santoso"
nama_lengkap = nama_depan + " " + nama_belakang # ->Perhatikan " " di tengah. Itu adalah String berisi satu spasi, supaya kedua nama tidak menempel

print(nama_lengkap)

#  Variabel dan print()
# Kita juga bisa mencampur String dan variabel menggunakan koma:

print("nama lengkap:", nama_lengkap)
print("Luas persegi panjang =", luas_persegi_panjang)