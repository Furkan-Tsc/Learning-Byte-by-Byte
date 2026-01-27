# Quick Sort
# Bu algoritma diziden bir referans eleman seçer ve ondan küçükleri soluna büyükleri sağına atar bunu sürekli yaparak sıralamayı sağlar.

dizi = [19, 5, 3, 8, 2, 15, 10]

print(dizi)

def bol(dizi, bas, son):
    referans = dizi[son]
    i = bas - 1 # küçük elemanlar

    for j in range(bas, son): # diziyi baştan sona tararız referans hariç
        if dizi[j] <= referans: # o anki eleman referansdan küçükse
            i += 1 # sınırı bir sağa kaydır
            dizi[i], dizi[j] = dizi[j], dizi[i] # elemanı küçüklerin olduğu bölgeye at küçükler = i
        
        dizi[i + 1], dizi[son] = dizi[son], dizi[i + 1] # döngü bitti ise referansı küçükler ve büyüklerin arasına yerleştir
    
    # referansın yeni yerini döndür
    return i + 1

def quick_sort(dizi, bas, son):
    if bas < son:  # eleman sayısı 0 yada 1 kalırsa dur
        referans_index = bol(dizi, bas, son) # diziyi parçala ve referansın indexini bul

        quick_sort(dizi, bas, referans_index - 1) # referansın sol tarafını aralarında sırala
        quick_sort(dizi, referans_index + 1, son) # referansın sağ tarafını aralarında sırala

quick_sort(dizi, 0, len(dizi) - 1) # fonksiyonu dizinin ilk yani 0 ve son yani len-1 indexi ile kullanırız