#Disini saya menggunakan fungsi def untuk mengelompokkan baris kode menginput biodata dan baris kode loop
def biodata():
    print("===========================================================")
    print("              Silahkan Masukkan Biodata Anda")
    print("===========================================================")
    #Saya menginput data-data yang biasanya terdapat di form biodata
    Nama_Depan = str(input("     Masukkan Nama Depan Anda          : "))
    Nama_Belakang = str(input("     Masukkan Nama Belakang Anda       : "))
    NIM = int(input("     Masukkan NIM Anda                 : "))
    Umur = int(input("     Masukkan Umur Anda                : "))
    Hobi = str(input("     Masukkan Hobi Anda                : "))
    TB = float(input("     Masukkan Ukuran Tinggi Badan Anda : "))
    BB = float(input("     Masukkan Ukuran Berat Badan Anda  : "))
    biodata = [Nama_Depan,Nama_Belakang, NIM, Umur, Hobi, TB, BB]
    print("===========================================================")
    print("                         Biodata")
    print("===========================================================")
    #Saya memisahkan inputan nama depan dan nama belakang sebelumnya dan menampilkan keduanya dalam satu baris
    print("            Nama           :",biodata[0],biodata[1]) 
    print("            NIM            :",biodata[2])
    print("            Umur           :",biodata[3])
    print("            Hobi           :",biodata[4])
    print("            Tinggi Badan   :",biodata[5])
    print("            Berat Badan    :",biodata[6])
    print("===========================================================")
    loops()
def loops(): #saya membuat loop agar biodata bisa diisi berulang kali sampai user ingin berhenti mengisi biodata
    x = str(input(" Apakah Anda Ingin Mengisi Ulang Biodata? Ya/Tidak : "))
    while x == "Ya":
        biodata()
        break
biodata() #Disini saya memanggil fungsi def biodata
print("===========================================================")
print ("    Terimakasih Telah Menggunakan Jasa Pelayanan Kami")
print("===========================================================")
