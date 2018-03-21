while True:
    deniz = input("Lütfen bir işlem girin: ")
    if deniz == "-1":
        print("Goodbye!!!")
        break
    karakterler = deniz.split(" ")
    ilk_sayi = float(karakterler[0])
    ikinci_sayi = float(karakterler[2])
    islem = karakterler[1]
    result = None
    if islem == "+":
        result = ilk_sayi + ikinci_sayi
    elif islem == "-":
        result = ilk_sayi - ikinci_sayi
    elif islem in ["*", "x", "X"]:
        result = ilk_sayi * ikinci_sayi
    elif islem in ["**", "^"]:
        result = ilk_sayi ** ikinci_sayi
    elif islem == "/":
        if ikinci_sayi == 0:
            print("Bölmede payda 0 olamaz!")
            continue
        result = ilk_sayi / ikinci_sayi
    else:
        print("Girdiğiniz işlem hatalı, lütfen tekrar deneyiniz!")
    if result is not None:
        print(result)