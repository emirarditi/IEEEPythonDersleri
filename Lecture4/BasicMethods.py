# Void örnekleri

def cizgiKoyan(adamin_adi):
    print("-" * len(adamin_adi))


print("Ali Emek")
cizgiKoyan("Ali Emek")
print("Ayşe Deniz")
cizgiKoyan("Ayşe Deniz")
print("Ali Koç <3")
cizgiKoyan("Ali Koç <3")
print("Aziz Yıldırım :@")
cizgiKoyan("Aziz Yıldırım :@")


# Return Örnekleri

def benimEnBuyugum(asjkhdf, bsfjşdf):
    return asjkhdf if asjkhdf > bsfjşdf else bsfjşdf


benimEnBuyugum(benimEnBuyugum(711, 248), 3)

# pass by reference vs pass by value

tryy = 5


def passByValue(a):
    return a + 2


tryy = passByValue(tryy)
print(tryy)

by = [3, 3, 3, 3, 3, 3]


def passByReference(k):
    k[0] = 2


passByReference(by)
print(by)


def multipleReturn():
    return 2, 3, 4


f, g, k = multipleReturn()
print(f, g, k)
