# String Methods
# mengolah dan mencari teks menggunakan method bawaan python

# Rumus umumnya:
# variabel.method()

nama = "ali sodikin"
print("nama:", nama)

# .upper(), huruf besar semua
nama_upper = nama.upper()
print("nama upper:", nama_upper)

# .title(), huruf awal setiap kata menjadi huruf besar
nama_title = nama.title()
print("nama tittle:", nama_title)

# .capitalize(), huruf awal string menjadi besar (kata pertama)
nama_capitalize = nama.capitalize()
print("nama capitalize:", nama_capitalize)

# replace(lama,baru), menggantikan karakter
nama_baru = nama.replace("sodikin","anderson")
print("nama baru:", nama_baru)

# strip(), menghapus spasi di awal dan akhir
kata = " ali "
kata_strip = kata.strip()
print("kata tanpa spasi:", kata_strip)
nama_strip = nama.strip() #spasi di tengah tidak terhapus, hanya awal dan akhir
print(nama_strip)

kalimat = "ular melingkar di pagar pak umar"
print(kalimat)

# .count(karakter), menghitung kemunculan karakter
hitung_r = kalimat.count("r")
print("jumlah r pada kalimat:", hitung_r)
hitung_r2 = kalimat.count("R")
print("jumlah R pada kalimat:", hitung_r2) # hasilnya 0, karena huruf kapitalnya harus sesuai

hitung_kata = kalimat.count("ular")
print("jumlah umar pada kalimat:", hitung_kata)

# find(karakter), mencari posisi, dimulai dari 0 dan jika tidak ada maka -1
posisi_r = kalimat.find("r")
print("posisi r di kalimat:", posisi_r)
posisi_ular = kalimat.find("ular")
print("posisi ular di kalimat:", posisi_ular)
posisi_umar = kalimat.find("Umar")
print("posisi Umarr di kalimat:", posisi_umar) # karena yang ada umar bukan Umar

print()

print("===Latihan==")
nama_produk = "   dell inspiron   "
kategori = "lAPTOP"
deskripsi = "Laptop dengan Java system"
kode = "DELL-G5590-256"

# Bersihkan spasi di awal dan akhir nama_produk.
produk_baru = nama_produk.strip()
print("nama produk dengan nama baru:", produk_baru)

# Ubah nama produk menjadi format huruf awal setiap kata kapital.
produk_baru_title = produk_baru.title()
print("produk baru kapital:", produk_baru_title)

# Ubah kategori menjadi huruf besar semua.
kategori_upper = kategori.upper()
print("kategori dnegan kapital semua:", kategori_upper)

# Ganti kata "Java" pada deskripsi menjadi "Python".
deskripsi_baru = deskripsi.replace("Java", "Python")
print("Deskripsi baru:", deskripsi_baru)

# Cari posisi "G5590" dalam kode.
kode_find = kode.find("G5590")
print("posisi kode:", kode_find)

# Hitung berapa kali huruf "p" muncul dalam nama_produk setelah dibersihkan.

hitung_p = produk_baru.count("p")
print("jumlah p dalam produk baru:", hitung_p)
