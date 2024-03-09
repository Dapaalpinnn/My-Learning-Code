#Konversi nilai kurs
Kursusd = 13950

# Informasi Program
print('Program konversi kurs USD ke IDR ')
print(f'Kurs saat ini 1 USD = {Kursusd} Rupiah')

# Input jumlah USD yang mau ditukar
jumlahUsd = float(input("Masukkan jumlah uang yang mau ditukar ke Rupiah: "))

# Hitung nilainya dalam rupiah
dalamRupiah = jumlahUsd * Kursusd

# Tampilkan hasilnya
print(f"Hasil konversi = Rp. {dalamRupiah} ")


