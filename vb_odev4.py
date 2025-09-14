"""
#SORU1
#5X5 Matris oluştur
#ort,std sapma, varyans hesapla
#max min değer?
#köşegenindeki elemanların toplamı?

import numpy as np

matris=np.random.randint(0,101,25).reshape(5,5)
print(matris)
ortalama = np.mean(matris)
std_sapma=np.std(matris)
varyans=np.var(matris)
print("ortalama:",ortalama)
print("standart sapma:",std_sapma)
print("varyans",varyans)

print("max değer:",np.max(matris))
print("min değer:",np.min(matris))

print("Köşegenler toplamı:",np.trace(matris))
********************************************************

#SORU-2
- 1000 adet öğrencinin sınav puanlarını (0-100 arası, normal dağılımdan gelen) simüle edin.
- Ortalama, medyan ve standart sapmayı hesaplayın.
- 50’den düşük alan kaç öğrenci olduğunu bulun.
import numpy as np
np.random.seed(20) #her seferinde aynı sonuçlar ile çalışayım
puanlar=np.random.normal(loc=60,scale=15,size=1000)
#burada normal dağılımda ort(loc),std sapma(scale) ve kaç tane veri olacağını ayarladık..
puanlar=np.clip(puanlar,0,100) #0-100 aralığı için sınırladık..
print("ortalama",np.mean(puanlar))
print("Medyan:",np.median(puanlar))
print("std sapma:",np.std(puanlar))

ogr_sayisi=np.sum(puanlar<50)
print(f'Puanı 50 den düşük {ogr_sayisi} öğrenci vardır.')
***********************************************************

#SORU-3
import pandas as pd
import matplotlib.pyplot as plt


#dataframe oluşturma

veriler={
    "Öğrenci":["Ali","Ayşe","Mehmet","Zeynep","Ahmet"],
    "Yaş":["20","21","19","22","20"],
    "Bölüm":["Bilgisayar","Fizik","Kimya","Bilgisayar","Fizik"],
    "Matematik":[70,60,80,90,55],
    "Fizik":[65,75,70,85,60],
    "Kimya":[80,85,65,95,70]
    
}

df=pd.DataFrame(veriler) #bu kısmı yapmak gerekiyor..
print(df)

print("Ders ortalamaları:")
print(df[["Matematik","Fizik","Kimya"]].mean())

en_y_mat=df["Matematik"].max()
print("En yüksek matematik notu:",en_y_mat)
index=df["Matematik"].idxmax() 
ogrenci=df.loc[index,"Öğrenci"]
print("En yüksek mat notunu alan öğrenci",ogrenci)

#idxmax: bir sütundaki max değerin indeksini alır
#loc ile seçilmek istenen satır ve sütunlara erişim sağlanıyor.

#Her öğrencinin not ortalaması
df["Ortalama"] = df[["Matematik", "Fizik", "Kimya"]].mean(axis=1)
print("Not Ortalaması Eklenmiş DataFrame:")
print(df)

#Bölüme göre 
print("Bölümlere Göre Ortalama Başarı:")
print(df.groupby("Bölüm")[["Matematik", "Fizik", "Kimya", "Ortalama"]].mean())

#ort 70'ten büyük öğrencilerin filtrelenmesi:
print("Ortalamsı 70 üstü olan öğrenciler",df[df["Ortalama"]>70]) 

#ek görevler:
plt.figure(figsize=(12,6))

#figure yeni bir grafik penceresi açar
#figsize ile genişlik ve yükseklik ayarlanır..

#for döngüsü ile dersleri dolaştık:
#enumarate--> indeks ve değeri birlikte döndürür
dersler = ["Matematik", "Fizik", "Kimya"]
for i, ders in enumerate(dersler):
    plt.subplot(1, 3, i+1)
    plt.hist(df[ders], bins=5,color="purple",edgecolor="black",alpha=0.7)
    plt.title(f"{ders} Dağılımı")
    plt.xlabel("Not")
    plt.ylabel("Öğrenci Sayısı")

plt.tight_layout()#grafikler birbirine sıkışmasın diye otomatik boşluk ayarlar
plt.show()


    
"""


#bölümlere göre bar grafiği:??? 
