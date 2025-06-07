def jumlah_ganjil_dari_faktorial(n):
    # Fungsi rekursif menghitung faktorial
    def faktorial(x):
        if x <= 1:
            return 1
        return x * faktorial(x - 1)

    # Fungsi bilangan ganjil
    def jumlah_ganjil(k):
        if k <= 0:
            return 0
        if k % 2 == 1:
            return k + jumlah_ganjil(k - 2)
        else:
            return jumlah_ganjil(k - 1)

    return jumlah_ganjil(faktorial(n))

# Program utama
n = int(input("Masukkan nilai n: "))
hasil = jumlah_ganjil_dari_faktorial(n)
print(f"Jumlah bilangan ganjil dari 1 sampai {n}! adalah: {hasil}")
