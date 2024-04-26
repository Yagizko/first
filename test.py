print("HELLO WORLD")
liste = {"CRİNGE":"Garip Veya Utandırıcı Birşey",
        "LOL":"Komik Bir Şeye Verilen Cevab"}

kelime = input("Hangi Kelimenin anlamını öğrenmek istiyorsun?")

if kelime in liste.keys():
  print("Sorduğunuz Kelimenin Anlamı =",liste[kelime])
else:
  print("Böyle bir kelime yok!")
