import sys

not_dosyasi = open("first_doc.txt", "r")
fare = 0
kedi = 0
maximus = 0
minimus = sys.maxsize
en_tembel_ogrenci = ""
en_inek_ogrenci = ""
for l in not_dosyasi:
    token = l.split("_")
    not_ = int(token[2].strip())
    if not_ > maximus:
        maximus = not_
        en_inek_ogrenci = token[0] + " " + token[1]
    if not_ < minimus:
        minimus = not_
        en_tembel_ogrenci = token[0] + " " + token[1]
    kedi += not_
    fare += 1

print("Sınıfın inegi " + en_inek_ogrenci)
print("Sınıfın tembeli " + en_tembel_ogrenci)
print(kedi / fare)

not_dosyasi.close()
