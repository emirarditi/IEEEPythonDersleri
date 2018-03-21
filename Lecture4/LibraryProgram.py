class Kitap:
    def __init__(self, isim, yazar, sayfa_sayisi, turu, isbn):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.turu = turu
        self.isbn = isbn
        self.mevcutluk = True
        self.kimde = None

    def kitabiTeslimVer(self, isim):
        self.mevcutluk = False
        self.kimde = isim

    def kitabiTeslimAl(self):
        self.mevcutluk = True
        self.kimde = None


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

