# # Apa itu Escape Characters?
# Escape characters adalah cara menuliskan karakter khusus di dalam string Python dengan menggunakan tanda backslash (\).

# Rumus dasarnya:
# \karakter

# \n, newline, baris baru
kalimat ="kalimat atas \nkalimat bawah"
print(kalimat)

# \t,memberi jarak horizontal
print("nama:\tucok")
print("umur:\t20 tahun")

#  \\ menampilkan karakter \, jika ingin double maka dikalikan dua
direktori = "C\\User\\folder"
print(direktori)
print("folder c\\\\user\\\\folder")

# \"" kutip ganda dalam string
print("abdul salam berkata \"dia pergi ke jakata\"")
print("ingat kalimat \"hati-hati di jalan\"")

# \" kutip tunggal dalam string
print("makan baksdo di \'bakos wak kumis\'")
print()

print("====LATIHAN====")
print("Toko Laptop Dennis \n=================== \nProduk \tHarga \nDell G5590 \t7500000 \nSSD 256 GB \t450000 \n==================== \nTotal \t7950000 \n\"Terima Kasih Sudah berbelanja\"")