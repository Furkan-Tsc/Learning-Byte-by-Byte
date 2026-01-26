# Merge Sort
# Bu algoritma bir diziyi ikiye böler ve en küçük parçaları sıralayıp birleştirir bunu tekrar tekrar yapar.
# Zamana göre sıralamada gayet iyidir ancak rami yoran bir algoritmadır yani önce listeyi karşılaştırıp ramde bir kopyasıını oluşturur sıraya dizer ve tekrar asıl listeye döker.

dizi = [19, 5, 3, 8, 2, 15, 10]

print(dizi)

def merge_sort(dizi):

    if len(dizi)<= 1: # eleman sayısı 0 yada 1 kalırsa dur çünkü tek elemanlı liste sıralıdır
        return dizi

    orta = len(dizi) // 2 # diziyi ortadan ikiye böl
    sol_yari = dizi[:orta] # sol kısım
    sag_yari = dizi[orta:] # sağ kısım

    # bu iki yarıyıda kendi aralarında en küçük parçaya kadar tekrar tekrar böl ve geri dönen sıralanmış listeyi değişkene kaydet
    sol_yari = merge_sort(sol_yari)
    sag_yari = merge_sort(sag_yari)

    return birlestir(sol_yari, sag_yari) # iki sıralı parçayı birleştir ve döndür
    
def birlestir(sol_yari, sag_yari): # iki ayrı sıralanmış listeyi tek listeye doğru sıralı şekilde dönüştürür
    siralanmis_dizi = []
    i = 0 # sol yarının indexi
    x = 0 # sağ yarının indexi

    while i < len(sol_yari) and x < len(sag_yari): # eğer iki listedede eleman var ise karşılaştırmaya devam et
        if sol_yari[i] < sag_yari[x]: # sol tarafın elemanı daha küçükse onu asıl listeye ekler
            siralanmis_dizi.append(sol_yari[i])
            i += 1 # solu bir adım kaydır
        else:
            siralanmis_dizi.append(sag_yari[x]) # sağ tarafın elemanı daha küçükse onu asıl listeye ekler
            x += 1 # sağı bir adım kaydır

    # eğer sıralama sonucunda sol kısım boş ve sağ kısımda eleman kalırsa bunları kontrol etmeden listenin sonuna ekleyebiliriz çünkü sıralıdır
    siralanmis_dizi.extend(sol_yari[i:])
    siralanmis_dizi.extend(sag_yari[x:])
    
    return siralanmis_dizi


print(merge_sort(dizi))
