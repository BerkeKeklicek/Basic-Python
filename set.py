

studentsSet = {"Mert","Salih","Aslan","Icardi"}
print(studentsSet) #Set rastgele sıralar

for student in studentsSet:
    print(student)

print("mert" in studentsSet) #Listede mert var mı? Büyük küçük harf önemli!

if "Mert" in studentsSet:
    print("Listede var")
    
studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve","Meliha","Selin"])
print(studentsSet)


print(len(studentsSet))

studentsSet.remove("Meliha")
print(len(studentsSet))

studentsSet.discard("Ahmet") #Öyle bir öğrenci olmasa bile hata vermez
print(len(studentsSet))

x = studentsSet.clear()
print(studentsSet)
