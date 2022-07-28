"""
Ekspedisi Pamanku
Aku menyambar ponsel di meja dan membuka pesan singkat dari paman tempo hari yang menjelaskan
jika paman harus mengeluarkan uang sebesar 1,5 juta per mobil dalam sehari. 
Tapi, beliau selalu kebingungan total pengeluaran per bulan karena adanya aturan ganjil-genap
 yang membuat pengoperasian mobil yang berbeda.

“Kalau begitu, aku akan masukkan variabel jumlah_hari berisi jumlah hari dalam sebulan
dan variabel list_plat_nomor berisi seluruh nomor plat mobil milik paman,” gumamku sendiri. 
Kalau seperti ini paman hanya perlu mengganti variabel jumlah_hari atau modifikasi 
variabel list_plat_nomor untuk melacak total pengeluaran paman selama sebulan. 
Ide Cemerlang!
"""
class kuis:
    def hitungGanjilgenap(self,uang_jalan):
    # Data
        jumlah_hari = 31
        list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
        # Pengecekan kendaraan dengan nomor pelat ganjil atau genap 
        # Deklarasikan kendaraan_genap dan kendaraan_ganjil = 0
        #print(list_plat_nomor.index(2198))

        kendaraan_genap = 0 
        kendaraan_ganjil = 0
        for plat_nomor in list_plat_nomor:
            if plat_nomor %2 == 0 :
                kendaraan_genap += 1
                #print("kendaraan_genap",kendaraan_genap)
            
            else:
                kendaraan_ganjil +=1
                #print("kendaraan_ganjil",kendaraan_ganjil)


        # Total pengeluaran untuk kendaraan dengan nomor pelat ganjil 
        # dan genap dalam 1 bulan
        
        i = 1
        total_pengeluaran = 0
        while i <= jumlah_hari:
            if i % 2 == 0:
                #print(i,"ini modulus hari GENAP")
                total_pengeluaran +=  (kendaraan_genap * uang_jalan)
                #print(total_pengeluaran,"INI YANG BARU GENAP")
            else:
                #print(i,"ini modulus hari GANJIL")
                total_pengeluaran += (kendaraan_ganjil * uang_jalan) 
                #print(total_pengeluaran,"INI YANG BARU GANJIL")
            i += 1
            #print(i,"PERULANGAN LOOPING")
        # Cetak total pengeluaran
        print("Total Yang Haru Di Bayar",total_pengeluaran)

    hitungGanjilgenap(1500000)

app = kuis()
app.hitungGanjilgenap(20000)