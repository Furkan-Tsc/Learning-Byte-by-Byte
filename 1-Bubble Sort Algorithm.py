import time
import os

# Bubble Sort
# Bu algoritma yan yana duran iki sayıyı karşılaştırır eğer soldaki sayı sağdakinden büyükse ikisi yer değiştirir. Değilse bir sonraki ikili sayıyı kontrol eder.

dizi = [19, 5, 3, 8, 2, 15, 10]
i = 0

def konsol_temizle():
    os.system('cls' if os.name == 'nt' else 'clear') # windows ise cls mac/linux ise clear)

dizi[i], dizi[i+1] = dizi[i+1], dizi[i] # i ile i+1 indexlerini yer değiştir

print(dizi)

n = len(dizi) # dizinin uzunluğunu al

def ciz(dizi): # listeyi yıldızlarla gösterme fonksiyonu
    for i in dizi:
        print("*" * i)

for i in range(n): # n kere tekrar et
   for x in range(n-i-1): # IndexError almamak için n-i-1 kullandık çünkü index 0dan başlar -i ise zaten sıralanmış olan elemanları tekrar tekrar kontrol etmeyi engeller
        if dizi[x] > dizi[x+1]:
            dizi[x], dizi[x+1] = dizi[x+1], dizi[x]
            konsol_temizle() # her değişimde konsolu siler daha hoş görüntü için
            ciz(dizi)
            time.sleep(0.5)

print(dizi)
