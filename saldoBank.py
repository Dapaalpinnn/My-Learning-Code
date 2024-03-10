# Menghitung saldo tahun ketiga menggunakan Compound Interest
# Compount Interest adalah bunga ber-bunga, biasanya digunakan pada Bank

# Saldo awal
saldoAwal = int(input("Masukkan saldo awal kamu: "))

# Bunga dan saldo tahun pertama
bungaTahunPertama = (10/100) * saldoAwal
saldoTahun1 = bungaTahunPertama + saldoAwal

# Bunga dan saldo tahun kedua
bungaTahunKedua = (10/100) * saldoTahun1
saldoTahun2 = bungaTahunKedua + saldoTahun1

# Bunga dan saldo tahun ketiga
bungaTahunKetiga = (10/100) * saldoTahun2
saldoTahun3 = bungaTahunKetiga + saldoTahun2

# Tampilkan hasil saldo tahun ke- 3 setelah 
print(f"Saldo kamu pada tahun ketiga setelah mendapat tambahan bunga 10% sebesar {saldoTahun3} Rupiah")
