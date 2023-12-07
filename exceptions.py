
try:
    sayi = int(input("Sayı Giriniz: "))
except ValueError:
    print("Tip uyuşmuyor : Lütfen tam sayı giriniz!")
except ZeroDivisionError:
    print("Payda sıfır olamaz : Lütfen geçerli sayı giriniz!")
except:
    print("Bir hata oluştu")
    
print("Bitti")