#substring

mesaj = "Merhaba Dünya"
print(mesaj[2:5])  #M=0 e=1 r=2 h=3 a=4 b=5

yenimesaj = mesaj[:5]
print(yenimesaj)
yenimesaj2 = mesaj[12:13] #Aradaki boşluk da sayılacak
print(yenimesaj2)

#len
print(len(mesaj))

yenimesaj3 = mesaj[len(mesaj)-1:len(mesaj)] #=mesaj[12:13] ile aynı mantık
print(yenimesaj3)

#Lower upper
print(mesaj.lower())
print(mesaj.upper())

#replace
print(mesaj.replace("ü", "u"))
mesaj = mesaj.replace("ü","u")
print(mesaj)


bilgi = "Berke Keklicek 18 Konya"
print(bilgi.split())

bilgi = "    Berke Keklicek 18   Konya"
print(bilgi.split())

bilgi = "Berke;Keklicek;18;Konya"
print(bilgi.split(";"))


#input
ad = input("Adınız?")
sayi1 = input("Sayı 1 =?")
sayi2 = input("Sayı 2 =?")
print(int(sayi1) + int(sayi2))




