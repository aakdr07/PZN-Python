# 1. Apa itu String?
# String adalah tipe data yang digunakan untuk menyimpan teks atau kumpulan karakter.
# Kutip tunggal '
buah = 'apel'
print(buah)

# Kutip ganda ""
nama = "ucok"
print(nama)

angka = "30"
print(angka, type(angka)) #tetap str karena penulisannya berbentuk str

# 2. Menggabungkan String
# Untuk menggabungkan string, kita menggunakan operator +.
nama_depan = "abdul"
nama_belakang = "salam"
nama_lengkap = nama_depan + " " + nama_belakang #"spasi" untuk meberi spasi
print(nama_lengkap)

# atau dengan cara
print(nama_depan + " " + nama_belakang)


# 3. String tidak bisa langsung digabungkan dengan tipe data lain

nama = "ucok"
umur = 20
# data = nama + umur # akan eror karena str dan tipe data lain tidak bisa digabung
data = nama + str(umur) # kita ubah tipe data yang bukan str menjadi str agar bisa digabung dengan str lain
print(data)

print()

# Apa itu len()?
# len() adalah function yang digunakan untuk mengetahui panjang suatu string, yaitu jumlah karakter di dalam teks tersebut, termasuk spasi.

kalimat = "Belajar Python"
panjang_kalimat = len(kalimat) #bisa meggunakan variabe;
print(panjang_kalimat)
print(len(kalimat)) # atau bisa ditampilkan langsung


# Setiap karakter memiliki index
# Dalam Python, setiap karakter pada string memiliki posisi yang disebut index. Index dimulai dari angka 0, bukan 1.

kata = "Python"

# Untuk mengambil karakter tertentu, kita menggunakan tanda kurung siku []

print(kata[0])
print(kata[1])
print(kata[2])
print(kata[3])

print()

# Python juga memungkinkan kita mengakses karakter dari belakang menggunakan index negatif.
print(kata[-1])
print(kata[-2])
print(kata[-3])

print()

# Rumus String Slicing
# String slicing digunakan untuk mengambil sebagian karakter dari sebuah string.

# rumus
# nama[index_awal:index_akhir]

kata = "belajar"

# menentukan index awal dan akhir
print(kata[0:3]) # -> diambil dari 0,1,2 
print(kata[2:6]) # -> diambil dari 2,3,4,5

# Tidak menuliskan index awal
print(kata[:4]) # hitunganya 0:4

# Tidak menuliskan index akhir
print(kata[3:]) #hitungannya dimulai dari index 3 sampai akhir

# Mengambil seluruh string
print(kata[:])
print()

# Latihan
print("===Latihan===")
kata = "Belajar"
print(kata[0:3])
print(kata[2:5])
print(kata[:4])
print(kata[3:])

laptop = "DELL-G5590-256"
print(laptop[5:10])