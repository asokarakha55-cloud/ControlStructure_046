persentase = float(input("Masukkan persentase nilai siswa: "))

if persentase >= 90:
    print("Excellent performance")
elif persentase >= 80:
    print("Very Good performance")
elif persentase >= 70:
    print("Good performance")
elif persentase >= 60:
    print("Average performance")
else:
    print("Needs Improvement")