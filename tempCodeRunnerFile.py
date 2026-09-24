a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print(f"Angka terbesar adalah: {terbesar}")