import sys

liste = [7,"berke",0,3,"6"]

for x in liste:
    try:
        print("Sayı: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç : " + str(sonuc))
    except:
        print(str(x) + " hesaplanamadı!")
        print("Hatanın sebebi : " + str(sys.exc_info()[0]))
    finally:
        print("İşlemler sona erdi")
