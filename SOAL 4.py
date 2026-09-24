n = int(input("Masukkan batas nilai (n): "))

print(f"Angka ganjil dari 1 sampai {n}:")
# Menggunakan perulangan dengan step 2 dari angka 1
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()