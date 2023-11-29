
class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2

matematik = Matematik()
print("Toplam = " + str(matematik.topla(2,28)))
