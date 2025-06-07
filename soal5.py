def kombinasi(n, r):
    # Basis rekursi
    if r == 0 or r == n:
        return 1
    # Rekursi
    return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

# Program utama
n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

if r > n:
    print("Kombinasi tidak valid. r harus <= n.")
else:
    hasil = kombinasi(n, r)
    print(f"Combinasi({n}, {r}) = {hasil}")
