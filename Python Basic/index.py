"""
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke tagihan berikutnya
    if tagihan[i] < 0:
        i += 1
        print([i])
        continue
    total_tagihan = total_tagihan + tagihan[i]
    i = i+ 1
print(total_tagihan) 

a = 5
for i in range(0, a):
    for j in range(0, i + 1):
        print('* ' , end='')
    print('')

a = 5
for i in range(0, a):
    for j in range(0, a - 1):
        print('* ' , end='')
    a -= 1
    print('')


a = 5
for i in range(0, a + 1):
    for j in range (0,i + 1):
        print('* ' , end='')
    print(" ")
 
for i in range(1,11):
    for j in range(1,11 + 1):
        print("*", end='')
    print("_")

def hitungBarang(baju,celana):

    total_harga = 0
    hari = 30

    i = 1
    while i < hari:
        
        if i < 7:
            total_harga = hari * (baju + celana)
            print(total_harga)
        i +=1

hitungBarang(50000,279000)



j = int(input("Angka Baru : "))
i = 1

while i < j:
    if j %  i == 5:
        print(j,i)
    else:
        print("yang tidak nol",i)
    i+=1
"""

