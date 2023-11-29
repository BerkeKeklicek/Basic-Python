

sehirler = ["Ankara","İstanbul","İzmir"]

for sehir in sehirler:
    if sehir == "Ankara":
        print(sehir)
        
        
for sehir in sehirler:
    if sehir =="İstanbul":
        break #Komut gerçekleşirse döngüyü sonlandırır.
    print(sehir + " için kod = " + sehir[0:3])
    print("*********")
    
for sehir in sehirler:
    if sehir =="İstanbul":
        continue #Sadece komutu döngü dışı bırakır.
    print(sehir + " için kod = " + sehir[0:3])
    print("*********")
    
#range
    
for x in range(10):
    print(x)
    
for y in range(2,10,2):
    print(y)



sayac = 1
sonuc = 0


while sayac<=10:
    sonuc = sonuc + sayac
    sayac = sayac + 1
print(sonuc)


