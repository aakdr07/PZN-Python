# 1. Assignment dasar
# Tanda = digunakan untuk memberikan nilai kepada variabel.

nama = "dennis" # -> hasilnya dennis
umur = 22
tinggi = 165.6
is_active = True

print(nama)
print(umur)
print(tinggi)
print(is_active)

print() # -> nilai kosong untuk berikan jarak

# 2. Multiple assignment
# Python memungkinkan beberapa variabel diberikan nilai sekaligus.

x = y = z = 10 # -> semua var bernilai 10

print(x)
print(y)
print(z)

a, b, c = 1, 2, 3 # artinya a = 10 dst

print(a,b,c) # -> kita bisa printkan variabel sekaligus

murid, usia = "budi", 20 # -> murid = budi, dst

print(murid, usia)

print()

# 3. Mengubah nilai variabel
# Variabel yang sudah dibuat bisa diberi nilai baru menggunakan =

nilai = 90
print(nilai) # -> nilai yang belum diubah

nilai = 100 # -> nilai diubah, karena python memlilih Assignment baru menggantikan nilai sebelumnya.
print(nilai)


