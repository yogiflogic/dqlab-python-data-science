import pandas as pd
from pandas.io.clipboards import to_clipboard

dataiklan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
print(dataiklan.head(10))
print('=================================================')
databaru = {'Negara':['Inggris', 'Amerika', 'Italy'],
            'Valuasi':['2000M', '3000M', '5000M']}

df = pd.DataFrame(databaru,columns=['Negara','Valuasi'])

print(df.head(2))
print("Algoritma Kalkulator")
data1 = 2000
data2 = 1000
hasil1 = data1 + data2
totall = hasil1 * 0.20
print(totall)
print("==============")
print(" Latihan Baru ")
print("==============")
def fungsiTambah(nama, asal,a = 10, b = 11,c = 200) :
    d = a + b
    f = d * c
    if (f < 2500) :
        print(f"Saldo {nama} Kurang Tambah Dulu Ya")
    else :
        print (f"Hasil perkaliaan dari {nama} asal {asal} adalah =",f)
fungsiTambah("yogi","ID")



# Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
# Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"] 
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana
# Hitung harga kena pajak
total_pajak = total_harga * 0.1
# Cetak total_harga + total_pajak
print(total_pajak)