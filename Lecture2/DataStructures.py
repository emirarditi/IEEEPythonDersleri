# Listeler

yami = []
yami.append(44)
yami.append(78)
yami.append(128)
print(yami)
print(yami[0:2])
print(yami[:2])
print(yami[-1])
print(yami[:])
print(yami)

# Alternatif yol
yami = [44, 78, 128]

# Sözlük
stok = {"domates": 0, "şeftali": 0, "muz": 0}
stok["şeftali"] += 300
stok["domates"] += 400
stok["muz"] += 144
stok["patlıcan"] = 1500
print(stok)

print(stok.keys())
print(stok.values())

#in

a = [1,2,3,4,5]
yy = a.index(3)
print(yy)
if 3 in a:
    print("Found it")
