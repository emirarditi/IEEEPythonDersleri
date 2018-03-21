# Reversing

deniz = input("Hey sen, bir şeyler gir: ")
resultant = ""
# Birinci yol
for karakterimiss in deniz:
    resultant = karakterimiss + resultant

print(resultant)

# İkinci Yol
res2 = ""
for sayimis in range(len(deniz) - 1, -1, -1):
    res2 += deniz[sayimis]

print(res2)

# Üçüncü yol
res3 = ""
for i in range(0, len(deniz)):
    res3 = deniz[i] + res3

print(res3)

# Dördüncü yol
resultt = deniz[2::-1]
print(resultt)

# Kontroller ve İşlemler

yakamoz = input("Hey sen, bişeyler gir!: ")
# kaç tane var?
yakamoz.count("a")
# ilk gördüğünün indexi ne
yakamoz.index("a")
# en sol ve en sağ boşluk ayıkla
print(yakamoz.strip())
# cümleleştir
print(yakamoz.capitalize())
# değiştirme
yakamoz.replace("l", "b")
# is ler

