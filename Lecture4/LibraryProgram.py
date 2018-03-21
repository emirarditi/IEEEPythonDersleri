class Kitap:
    def __init__(self, isim):
        self.isim = isim
        self.mevcutluk = True
        self.kimde = None

    def kitabiTeslimVer(self, isim):
        self.mevcutluk = False
        self.kimde = isim

    def kitabiTeslimAl(self):
        self.mevcutluk = True
        self.kimde = None

    def __str__(self):
        return self.isim


class Kutuphane:
    def __init__(self, isim, lokasyon):
        self.isim = isim
        self.lokasyon = lokasyon
        self.kitaplar = []

    def kitabiTeslimVer(self, isim, kullanici_ismi):
        for kitap in self.kitaplar:
            if kitap.isim == isim:
                kitap.kitabiTeslimVer(kullanici_ismi)
                break

    def kitabiTeslimAl(self, isim):
        for kitap in self.kitaplar:
            if kitap.isim == isim:
                kitap.kitabiTeslimAl()
                break

    def mevcutlukKontrolu(self, isim):
        for kitap in self.kitaplar:
            if kitap.isim == isim:
                if kitap.mevcutluk == True:
                    print("Kitap kütüphanemizde mevcuttur.")
                else:
                    print("Kitap mevcut değil." + kitap.kimde + " isimli kişidedir.")

    def kitapEkle(self, kitap):
        self.kitaplar.append(kitap)


ilk_kutuphanemiz = Kutuphane("Atatürk Kütüphanesi", "Anıtkabir")
ilk_kitap = Kitap("Otomatik Portakal")
ikinci_kitap = Kitap("Nutuk")
ucuncu_kitap = Kitap("Bir Dünya Kurmak")
dorduncu_kitap = Kitap("1984")
besinci_kitap = Kitap("Animal Farm")

ilk_kutuphanemiz.kitapEkle(ilk_kitap)
ilk_kutuphanemiz.kitapEkle(ikinci_kitap)
ilk_kutuphanemiz.kitapEkle(ucuncu_kitap)
ilk_kutuphanemiz.kitapEkle(dorduncu_kitap)
ilk_kutuphanemiz.kitapEkle(besinci_kitap)


kullanici = input("Lütfen adınızı giriniz: ")
print("""Merhaba, kütüphane programına hoşgeldiniz: """)
while True:
    kullanici_girdisi = input("""1) Kitap Teslim Al
    2) Kitap Teslim Et
    3) Kitap Sorgula
    4) Kitap Ekle
    5) Kıtapları Görüntüle
    Lütfen bir seçenek seçin: """)
    if kullanici_girdisi == "1":
        kitap_adi = input("Lütfen Teslim Almak İstediğiniz Kıtabın Adını Girin: ")
        ilk_kutuphanemiz.kitabiTeslimVer(kitap_adi, kullanici)
    elif kullanici_girdisi == "2":
        kitap_adi = input("Lütfen Teslim Etmek İstediğiniz Kıtabın Adını Girin: ")
        ilk_kutuphanemiz.kitabiTeslimAl(kitap_adi)
    elif kullanici_girdisi == "3":
        kitap_adi = input("Kitap Adı Girin: ")
        ilk_kutuphanemiz.mevcutlukKontrolu(kitap_adi)
    elif kullanici_girdisi == "4":
        kitap_adi = input("Lütfen Eklemek İstediğiniz Kıtabı Girin: ")
        ilk_kutuphanemiz.kitapEkle(Kitap(kitap_adi))
    elif kullanici_girdisi == "5":
        for kitap in ilk_kutuphanemiz.kitaplar:
            print(kitap)
    else:
        print("Hatalı Giriş!!!")
