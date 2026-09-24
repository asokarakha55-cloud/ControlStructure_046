n = int(input("Masukkan jumlah suku (n): "))

a, b = 0, 1

print(f"Deret Fibonacci hingga {n} suku:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()  