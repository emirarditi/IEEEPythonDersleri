import pickle as pkl

dosya = open("first_doc.txt", "r")
not_listesi = {}
for l in dosya:
    bilgiler = l.strip().split(" ")
    kisilik = bilgiler[0] + " " + bilgiler[1]
    not_listesi[kisilik] = int(bilgiler[2])

dosya.close()
f = open("ogrenci_notlari", "wb")
pkl.dump(not_listesi, f)

f.close()

f2 = open("ogrenci_notlari", "rb")
a = pkl.load(f2)
print(a["Emir Arditi"])

