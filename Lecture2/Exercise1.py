total = 0
count = 0
while True:
    girdi = int(input("?: "))
    if girdi is -1:
        break
    count += 1
    total += girdi

print(total / count)