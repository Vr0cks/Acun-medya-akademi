# Görev 1
user_text = input("Metin Girin.: ")

modified_text = user_text.strip().upper().replace("A", "E")
word_list = modified_text.split()

print("Düzenlenmiş Metin:", modified_text)
print("Kelimeler Listesi:", word_list)

# Görev 2
text = "Python programlama dili"

reversed_text = text[::-1]

replaced_text = text.replace("programlama", "kodlama")

print("Ters Çevrilmiş Metin:", reversed_text)
print("Değiştirilmiş Metin:", replaced_text)
