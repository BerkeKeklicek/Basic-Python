

ogrenciler = ["Berke","Ahmet","Mehmet","Salih"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciiler:
  fileToAppend.write(ogrenci)
  fileToAppend.write("\n")

fileToAppend.close()
