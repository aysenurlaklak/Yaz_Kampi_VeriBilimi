"""
#SORU-1
notlar = [85, 92, 76, 92, 100, 76, 85, 92]
• Listedeki tekrar eden notları silip benzersiz bir liste oluşturun.
• En yüksek ve en düşük notu bulun.
• Notları küçükten büyüğe sıralayın.
notlar = [85, 92, 76, 92, 100, 76, 85, 92]
yeni_notlar= np.unique(notlar)
print(yeni_notlar)

print("En yüksek not:",np.max(notlar))
print("En düşük not:",np.min(notlar))

print("Sıralanmış notların listesi:",np.sort(notlar))
************************************************************************
#SORU-2 Armstrong sayı kontrolü(153-->1^3 + 5^3 + 3^3=153 şeklinde)
print("ARMSTRONG SAYI MI ? ")
sayi=int(input("lütfen bir sayı giriniz:"))

def armstrong_mu(sayi):
    str_sayi=str(sayi)
    
    toplam =0
    for i in str_sayi:
        toplam+=int(i)**3
    if toplam==sayi:
        print("Girilen sayi armstrong bir sayıdır..")
    else:
        print("Girilen sayı armstrong değildir..")
        
armstrong_mu(sayi)
********************************************************************
#SORU-3
Aşağıdaki iki küme verilmiştir:
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}
• Ortak dilleri bulun.
• Sadece A’da olan dilleri listeleyin.
• İki kümenin birleşimini alfabetik olarak yazdırın.
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}
a=np.array(list(A))
b=np.array(list(B))
#ORTAK DİL
ortak=np.intersect1d(a,b)
print("ortak diller:",ortak)

#SADECE A'DA OLANLAR
c=np.setdiff1d(a,b)
print("Sadece A'da bulunanlar:",c)

#BİRLEŞİM
birlestir=np.union1d(a,b)
birlestir.sort()
print("Birleşim",birlestir)
*****************************************************************
#SORU-4
random modülünü kullanarak 1–100 arasında 10 rastgele sayı üretin.
• Bu sayıların ortalamasını ve standart sapmasını statistics modülü ile hesaplayın
A=np.random.randint(1,101,10)
print("Random sayılar:",A)
print("ortalama:",A.mean())
print("standart sapma:",A.std())
*****************************************************************
#SORU-5
kelime_sayacı(metin) adında bir fonksiyon yazın.
Fonksiyon verilen metindeki:
• toplam kelime sayısını
• en uzun kelimeyi
• en sık geçen kelimeyi döndürsün.

from collections import Counter
def kelime_sayaci(metin):
    kelimeler=metin.split()
    kelime_sayisi=len(kelimeler)
    
    en_uzun_kelime=max(kelimeler,key=len)
    
    en_cok=Counter(kelimeler).most_common(1)[0][0] #en çok geçen 1 kelimeyi al, dönen listenin ilk elemanını al demek..
    #most_common(3) yazsaydı en çok geçen üç kelime 
    #counter ile bu liste şöyle oluyor: [(aysenur,3),(laklak,2),(kelime,adet)] 
    
    
    print("kelime sayisi:",kelime_sayisi)
    print("en uzun kelime :",en_uzun_kelime)
    print("en sık geçen kelime:",en_cok)
    
    
    
metin=input("Lütfen bir metin giriniz:")
kelime_sayaci(metin)
****************************************************************
#SORU-6
Aşağıdaki liste için map, filter, sorted gibi gömülü fonksiyonları kullanarak:
sayilar = [5, 12, 7, 18, 24, 3, 16]
• Sadece çift sayıları filtreleyin.
• Bu sayıların karelerini bulun.
• Karelerini azalan sırada sıralayın

#normal çözüm:
import numpy as np 
sayilar = [5, 12, 7, 18, 24, 3, 16]
np_sayilar=np.array(sayilar)

ciftler=np_sayilar[(np_sayilar) % 2 ==0 ]
print("Çift sayılar:",ciftler)

kareler=np.square(np_sayilar)
print("sayıların kareleri:",kareler)
sirali_kareler=np.sort(kareler)[::-1]
print("karelerin sıralanmış hali:",sirali_kareler)

********
#map fonksiyonu: listedeki her eleman için fonksiyonu uygular..bu örnekte listedeki her bir elemanın karesini almak uygulanacak fonksiyondur..
sayilar = [5, 12, 7, 18, 24, 3, 16]
kareler=list(map(lambda x: x**2,sayilar))
print("kareler:",kareler)

#filter fonksiyonu:
ciftler=list(filter(lambda x: x%2==0,sayilar))
print(ciftler)

#bu fonksiyonlar birer nesne döndürdüğü için liste içine yazdık.
***************************************************
#SORU-7
Aşağıdaki listeyi, her kelimenin uzunluğuna göre küçükten büyüğe sıralayın.
kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]
Bunu sorted + lambda ile yapın.

#sort ve sorted farkı: sort orijinal liste üzerinde çalışırken sorted yeni bir liste oluşturur
#sort sadece listeler ile çalışırken sorted liste tuple stringler ile çalışabilir..

kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]
sirali=sorted(kelimeler,key=lambda x:len(x))
print(sirali)

**************************************************************
#SORU-8
Bir string içinde geçen tüm rakamları bulun ve bunların toplamını döndüren bir fonksiyon
yazın.
Örn: "abc12def3" → 12 + 3 = 15

rakamlar=[]
kelime=input("Harf ve rakamlardan oluşan bir string giriniz:")
for i in kelime:
    if i.isdigit():
        rakamlar.append(int(i))
print(rakamlar)

def topla(rakamlar):
    toplam=sum(rakamlar)
    print("rakamlar toplamı:",toplam)
topla(rakamlar)
********************************************************************

#SORU-9
10 elemanlı bir numpy dizisi oluşturun.
• Elemanlar 0–50 arasında rastgele sayılar olsun.
• Dizinin ortalamasını, standart sapmasını ve en büyük değerini bulun.

import numpy as np
dizi=np.random.randint(0,51,10)
print(dizi)
print("ortalama:",np.mean(dizi))
print("standart sapma:",np.std(dizi))
print("max eleman:",np.max(dizi))
************************************************************

SORU-10
5x5 boyutunda rastgele 0–1 arasında değerlerden oluşan bir numpy matrisi üretin.
• Her sütunun ortalamasını bulun.
• 0.5’ten büyük olan değerleri 1, küçük eşit olanları 0 yaparak binary matris oluşturun.




"""
import numpy as np
matris=np.random.rand(5,5)
print("matris:\n",matris)

sutun_ort = np.mean(matris, axis=0)
print("\nSütun ortalamaları:", sutun_ort)

binary_matris = (matris > 0.5).astype(int)
print("\nBinary matris:\n", binary_matris)


    


    





        






