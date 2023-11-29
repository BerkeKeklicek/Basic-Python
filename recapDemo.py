

#sayi = int(input("Kaç yıldız olsun?"))

#yildiz = ""

#for x in range(1,6):
    #yildiz = yildiz + "*"
    #print(yildiz)



sayi = int(input("Sayı Giriniz : "))
asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break
if asalMi:
    print("Asal")
else:
    print("Asal Değil")

    

