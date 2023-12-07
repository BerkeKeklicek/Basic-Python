

sayilar = [1,2,3,4,5]

sayilarKaresi = list(map(lambda sayi: sayi*sayi,sayilar))

sayilarFiltreli = list(filter(lambda sayi: sayi>2,sayilar))

print(sayilarKaresi)
print(sayilarFiltreli)

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)

print(sayilarFaktoriyel)
