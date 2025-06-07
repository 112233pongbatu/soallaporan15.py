def jumlah_digit_str(n):
    n = str(n)  #\
    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) + jumlah_digit_str(n[1:])

# Program utama
angka = int(input("Masukkan bilangan: "))
hasil = jumlah_digit_str(abs(angka))  
print(f"Jumlah digit dari {angka} adalah: {hasil}")
