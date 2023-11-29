

tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",[3,4,5],()]

liste[0] = 6 #Tuple sonradan değiştirilemez!


TupleDeger = ("Berke",) #Sondaki , onun tuple olduğunu gösteriyor
print(type(TupleDeger)) 

print(tupleListe[1:2]) 
print(liste[1:2])

print(tupleListe[-2]) #Sağdan ikinci
print(liste[-2])


print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))

