# Görev 1: Liste Kontrolü
meyveler = ["elma", "armut", "çilek", "kiraz"]
kullanici_meyve = input("Bir meyve adı girin: ")
if kullanici_meyve in meyveler:
    print("Girdiğiniz meyve listede var.")
else:
    print("Girdiğiniz meyve listede yok.")

# Görev 2: Parola Kontrolü
parola = "PyThOn123"
kullanici_karakter = input("Bir karakter girin: ")
if kullanici_karakter not in parola:
    print("Parolada bu karakter yok.")
else:
    print("Parolada bu karakter var.")