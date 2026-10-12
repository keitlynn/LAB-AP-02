usia = int(input("masukan usia anda :"))
anggota = input("apakah anggota? (ya/tidak) :")
if usia < 5 :
    harga = 0 
elif usia <= 12 :
    harga = 50000
elif usia <=59 :
    harga = 100000
else :
    harga = 70000

harga_akhir = harga * 0.08 if anggota == "ya" else harga 
print ("harga_tiket: Rp", harga_akhir)
    



