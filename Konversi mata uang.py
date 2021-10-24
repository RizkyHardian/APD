#Saya mengelompokkan baris kode setiap hasil dan kalkulasi dari setiap mata uang asing
def USD(): 
    print("===========================================================")
    IDR = int(input("        Masukkan Nominal = Rp."))
    USD = float(IDR/14230.80)
    print("        Mata Uang USD    = $", USD)
    loops()
def SGD():
    print("===========================================================")
    IDR = int(input("        Masukkan Nominal = Rp."))
    SGD = float(IDR/10556.19)
    print("        Mata Uang SGD    = $", SGD)
    loops()
def EUR():
    print("===========================================================")
    IDR = int(input("        Masukkan Nominal = Rp."))
    EUR = float(IDR/16570.41)
    print("        Mata Uang EUR    = €", EUR)
    loops()
def JPY():
    print("===========================================================")
    IDR = int(input("        Masukkan Nominal = Rp."))
    JPY = float(IDR/125.41)
    print("        Mata Uang JPY    = ¥", JPY)
    loops()
#Saya juga mengelompokkan Inputan dan loops
def konversi():
    print("==========================================================")
    print("         Konversi Mata Uang IDR - Mata Uang Asing")
    print("Silahkan Pilih Salah Satu Konversi Dari Mata Uang Berikut!")
    print("==========================================================")
    print ("                    1. IDR - USD")
    print ("                    2. IDR - SGD")
    print ("                    3. IDR - EUR")
    print ("                    4. IDR - JPY")
    option = int(input(" Pilih Konversi Mata Uang Yang Anda Inginkan! 1/2/3/4 : "))
    if option == 1:
        USD()
    elif option == 2:
        SGD()
    elif option == 3:
        EUR()
    elif option == 4:
        JPY()
    else:
        print("===========================================================")
        print("    Terjadi Kegagalan Ketika Mengidentifikasi Mata Uang")
        loops()
def loops():
    print("===========================================================")
    x = str(input("Apakah Anda Masih Ingin Mengkonversi Uang? Ya/Tidak : "))
    while x == "Ya":
        konversi()
        break
konversi() #Disini saya memanggil def konversi dan program mulai berjalan
print("===========================================================")
print ("    Terimakasih Telah Menggunakan Jasa Pelayanan Kami")
print("===========================================================")
