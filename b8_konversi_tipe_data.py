# konversi tipe data adalah proses mengubah data dari satu tipe data, ke tipe data lainnya

data_text = "20" # disini berbentuk string
print("data text:", data_text, "dengan tipe data", type(data_text))

print()

# 1.int()
# Digunakan untuk mengubah data menjadi integer (bilangan bulat).
data_int = int(data_text) # -> diubah menjadi int
print("data int:", data_int)
print("dengan tipe data:", type(data_int)) 
print()

# 2. str()
# Digunakan untuk mengubah data menjadi string (teks).
umur = 18 # -> tipe datanya adalah int
print("tipe data umu:", type(umur))

umur_str = str(umur) # -> menjadi str
print("umur_str:", umur_str)
print("tipe data umur_str:", type(umur_str))

print()

# float()
# Digunakan untuk mengubah data menjadi float (bilangan desimal).

print("umur:",umur, type(umur)) # -> disini kita ambil contoh varibel umur diatas

umur_float = float(umur) # yang awalnya int menjadi float
print("umur float:", umur_float)
print("tipe data umur_float:", type(umur_float))

print()

# 4. bool()
# Digunakan untuk mengubah data menjadi boolean.

nilai = 0 # -> tipe data ini int
nilai_bool = bool(nilai)
print("nilai awal:", nilai, type(nilai))
print("nilai_bool:", nilai_bool, type(nilai_bool))

print()

print("===Studi kasus dengan input ===")
nama_murid = input("Masukkan nama murid: ")
usia_murid = int(input("Masukkan Usia murid: ")) # -> disini kita bisa langsung mengubah tipe datanya dengan membungkus input dengan tipe data yang kita mau
tinggi_murid = float(input("Masukkan tinggi murid: "))
berat_murid = float(input("Masukkan BB Murid: "))

print("Nama Murid:", nama_murid, type(nama_murid))
print("Usia Murid:", usia_murid, type(usia_murid))
print("Tinggi Murid:", tinggi_murid, type(tinggi_murid))
print("Berat badan murid:", berat_murid, type(berat_murid))
