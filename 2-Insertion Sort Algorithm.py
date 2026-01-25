import time
import os

# Insertion Sort
# Bu algoritma dizideki her elemanı sırayla alır kendinden önceki sayılara bakar ve küçükten büyüğe doğru olcak şekilde uygun boşluğa ekler.

dizi = [19, 5, 3, 8, 2, 15, 10]
i = 0

def ciz(dizi): # listeyi yıldızlarla gösterme fonksiyonu
    for i in dizi:
        print("*" * i)

os.system("cls")
ciz(dizi)
time.sleep(1)

for i in range(1, len(dizi)): # ilk eleman zaten sıralı kabul edildiği için 2. den başladık
    sayi = dizi[i]
    x = i - 1 # seçilen sayının hemen solundaki komşunun yerini gösterir
    while x >= 0 and dizi[x] > sayi: # seçilen sayıdan daha büyük önceki sayıları birer adım sağa kaydırır ve seçilen sayı için yer açar
        dizi[x+1] = dizi[x] # x. indeksdeki elemanı (x+1). indekse kopyalar
        x = x - 1
        
        os.system("cls") # konsolu siler daha hoş görüntü için
        ciz(dizi)
        time.sleep(0.3)
        
    dizi[x+1] = sayi # doğru boşluk bulunduğunda doğru sayıyı oraya yerleştirir

    os.system("cls")
    ciz(dizi)
    time.sleep(0.5)
