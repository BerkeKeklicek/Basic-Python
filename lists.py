

#ogrenci1 = "Mert"
#ogrenci2 = "Ahmet"
#ogrenci3 = "Mehmet"

ogrenciler = ["Mert","Ahmet","Mehmet"]
print(ogrenciler[1])

ogrenciler.append("Salih") #Eklemek
print(ogrenciler)
ogrenciler.remove("Mert") #Çıkarmak
print(ogrenciler)
ogrenciler[0] = "Veli"
print(ogrenciler)

#List constructor
sehirler = list(("Ankara","İstanbul","Antalya","Ankara"))
print(sehirler)
print(len(sehirler))

#Diğer fonksiyonlar
#print(sehirler.clear()) #Liste temizlendi
print("Ankara sayısı = " + str(sehirler.count("Ankara")))
print("Ankara indexi = " + str(sehirler.index("Ankara")))
sehirler.pop(1) #İstanbulu sil
sehirler.insert(0, "İstanbul") #En başa İstanbulu ekle
sehirler.reverse() #Tersden başlat
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0]="İzmir"
print(sehirler)
print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3) #Yan yana yazmak
sehirler.sort() #Alfabetik sıralama
sehirler.reverse()
print(sehirler)


