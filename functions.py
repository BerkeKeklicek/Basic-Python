

def selamVer(isim):
    print("Merhaba " + isim)

selamVer("Berke")

def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)
print(alan)

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlaniHesapla2(3,6))
