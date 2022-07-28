from numpy import median
import pandas as pd
import numpy as np

def myfunc(nama,x):
    try :
        z = x * 100
        a = 5
        print(nama,(a))
    except:
        print(" kode ada yang salah, tolong ulangi")   

myfunc("Yogi",12)

# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - 0.3 # baris pertama
hb1 = harga_bayar * total_harga # baris kedua
pajak_bayar = pajak * hb1 # baris ketiga
hb2 = hb1 + pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", hb2)

x = [1,5,7,4,0,6,900,9,6,100]
print(median(x))
"""
username = input("Masukan Nama Anda :" )
sepatu = input("Berapa Sepatu? :")
baju = input("Berapa Baju? :")
total = int (sepatu) + int (baju)

print("Nama Anda adalah :" + username, + int (sepatu), + int (baju))
print("Total Yang Harus Anda Bayar adalah:", total)
"""
#myorder = "Saya Mau beli {} Sepatu Dan {} Baju"
#print(myorder.format(sepatu,baju))
sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }

harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu + harga_baju + harga_baju)
print(harga_sepatu)
print(harga_baju)
print(harga_celana)
print(total_harga)

sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }

harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu + harga_baju + harga_celana)
print(harga_sepatu)
print(harga_baju)
print(harga_celana)
print(total_harga)

jam = 13
if jam >= 5 and jam < 12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >=12 and jam < 17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam < 19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")

txt = " Hello World "
x = txt.strip()
print(str.lower(x))