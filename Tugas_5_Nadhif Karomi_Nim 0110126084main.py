
# Online Python - IDE, Editor, Compiler, Interpreter
print("=== Alat hitung luas bangun datar ===")
print("pilih 1 untuk menghitung luas persegi")
print("pilih 2 untuk menghitung luas lingkaran")
print("pilih 3 untuk menghitung luas segitiga")

pilihan = int(input("Masukkan Pilihan (1/2/3)")) 
match pilihan : 
    case 1:
        s = int(input("Masukkan panjang sisi persegi: "))
        luas = s*s
        print(f"luas persegi adalah: {luas}") 
    case 2:
        r = int(input ("Masukkan panjang jari jari lingkaran:"))
        pi = 3.14
        luas = pi*r**2
        print(f"luas lingkaran adalah:{luas}")
    case 3:
        a = int(input("Masukkan panjang alas segitiga: "))
        t = int(input("Masukkan panjang tinggi segitiga: ")) 
        luasS = a*t/2
        print(f"luas segitiga adalah:{luasS}")
        
    case _:
        print ("Masukkan pilihan dengan benar")
    