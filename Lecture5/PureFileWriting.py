a = open("file_to_write.txt", "r+")
print(a.read())
a.write("a")
print(a.read())
a.close()

# Stream Pointer hareketi
