def cek_palindrom(kalimat):
    # Hilangkan spasi dan ubah ke huruf kecil
    kalimat = ''.join(huruf.lower() for huruf in kalimat if huruf.isalnum())

    # Fungsi rekursif di dalam fungsi utama
    def rekursif(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return rekursif(s[1:-1])

    return rekursif(kalimat)

teks = input("Masukkan kalimat: ")
if cek_palindrom(teks):
    print("Kalimat tersebut adalah palindrom.")
else:
    print("Kalimat tersebut bukan palindrom.")
