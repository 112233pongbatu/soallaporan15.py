def cek_prima(n, pembagi=None):
    if n < 2:
        return False
    if pembagi is None:
        pembagi = n - 1
    if pembagi == 1:
        return True
    if n % pembagi == 0:
        return False
    return cek_prima(n, pembagi - 1)

# Program utama
angka = int(input("Masukkan bilangan: "))

if cek_prima(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")
