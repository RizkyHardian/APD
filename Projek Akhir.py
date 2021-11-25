import os
import time

#time sleep
print("\n    LOADING.......0%")
time.sleep(4)
print("\n    LOADING.......25%")
time.sleep(6)
print("\n    LOADING.......75%")
time.sleep(4)
print("\n    LOADING COMPLETE!!!")
time.sleep(1)

#color
class color:
   b = '\033[94m'
   g = '\033[92m'
   y = '\033[93m'
   r = '\033[91m'
   p = '\033[95m'
   w = '\033[0m'

#data-data
rumah = {1:{"Nama Pemilik" : "Rizky","Tipe": 36, "Alamat" : "Jl. M. Yamin No. 59","Harga" : 214000000,"Luas Bangunan" : 40, "Luas Tanah" : 60, "Nomor Handphone": "082233445559"},
2:{"Nama Pemilik":"Jerry", "Tipe": 54, "Alamat" : "Jl. Pramuka 2A No. 67", "Harga" : 980000000,"Luas Bangunan" : 59, "Luas Tanah" : 105,"Nomor Handphone":"08765432167"},
3:{"Nama Pemilik":"Dani","Tipe":45,"Alamat":"Jl. Perjuangan Baru No. 92","Harga": 920000000, "Luas Bangunan":47,"Luas Tanah":110, "Nomor Handphone":"080813756492"}}

data_rumah = {}

username = ["admin","user"]
password = ["596","792"]

#Fungsi-fungsi
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def login():
    while True:
        clear_screen() 
        print(color.g+"="*60)
        print("""||                    Selamat Datang Di                   ||
||             Program Agensi Jual Beli Rumah             ||""")
        print("="*60)
        print("||                1. Login                                ||")
        print("||                3. Keluar                               ||")
        print("="*60)
        pilihan = input("||    Masukkan Pilihan :  "+color.b).lower()
        if pilihan == ("1" or "login"):
            print(color.g+"="*60)
            auth = input("||    Masukkan Username : "+color.b).lower()
            pw = input(color.g+"||    Masukkan Password : "+color.b)
            if auth == username[0] and pw == password[0]:
                print(color.g+"="*60)
                print("\n    Login Berhasil...")
                time.sleep(2)
                print("\n    Menampilkan Menu Admin....")
                time.sleep(3)
                admin()
            elif auth == username[1] and pw == password[1]:
                print (color.g+"="*60)
                print("\n    Login Berhasil...")
                time.sleep(2)
                print("\n    Menampilkan Menu User....")
                time.sleep(3)
                user()
            else:
                print(color.r+"="*60)
                print("||          Username dan Password Tidak Valid!!!          ||")
                print("="*60)
                input(color.w+"\n    Tekan Enter Untuk Kembali......")
                time.sleep(3)
        elif pilihan == ("3" or "keluar"):
            print(color.g+"="*60)
            print ("||       Terimakasih Telah Menggunakan Program Kami       ||")
            print("="*60)
            time.sleep(3)
            break
        else:
            print(color.r+"="*60)
            print("||                  Pilihan Tidak Valid!!                 ||")
            print("="*60)
            input(color.w+"\n    Tekan Enter Untuk Kembali......")
            time.sleep(3)

def admin():
        clear_screen()
        print(color.g+60*"=")
        print("""||             Program Agensi Jual Beli Rumah             ||
||                     Menu Admin                         ||""")
        print(60*"=")
        print("||                1. Lihat Data Rumah                     ||")
        print("||                2. Tambahkan Data Rumah                 ||")
        print("||                3. Ubah Data Rumah                      ||")
        print("||                4. Hapus Data Rumah                     ||")
        print("||                5. Kembali                              ||")
        print("="*60)
        pilihan1=input("||    Masukkan Pilihan : "+color.b).lower()
        if pilihan1 == ("1" or "lihat data rumah"):
            time.sleep(3)
            clear_screen()
            print(color.g+"="*60)
            for w,x in rumah.items():
                print("|| Rumah",w)
                for y,z in x.items():
                    print("||\t",y,":",z)
                print("="*60)
            print()
            time.sleep(1)
            input(color.w+"    Tekan Enter Untuk Kembali......")
            time.sleep(4)
            admin()
        elif pilihan1 == ("2" or "tambahkan data rumah"):
            while True:
                try:
                    time.sleep(2)
                    clear_screen()
                    print(color.g+"="*60)
                    pemilik = input("||    Masukkan Nama Pemilik Rumah : ")
                    if len(pemilik) <= 2:
                        print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                        print(color.g+"="*60)
                        continue
                    tipe = int(input("||    Masukkan Tipe Rumah : "))
                    if tipe <= 0:
                        print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                        print(color.g+"="*60)
                        continue
                    alamat = input("||    Masukkan Alamat Rumah : ")
                    if len(alamat) <= 5:
                        print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                        print(color.g+"="*60)
                        continue
                    harga = int(input("||    Masukkan Harga Rumah : "))
                    if harga <= 0:
                        print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                        print(color.g+"="*60)
                        continue
                    lb = int(input("||    Masukkan Luas Bangunan : "))
                    if lb <= 0:
                        print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                        print(color.g+"="*60)
                        continue
                    lt = int(input("||    Masukkan Luas Tanah : "))
                    if lt <= 0:
                        print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                        print(color.g+"="*60)
                        continue
                    hp = input("||    Masukkan Nomor Handphone Pemilik : ")
                except ValueError:
                    print(color.r+"||    Error! Masukkan Input Dengan Benar!!")
                    print(color.g+"="*60)
                    continue
                else:
                    break
            data_rumah["Nama Pemilik"] = pemilik
            data_rumah["Tipe"] = tipe
            data_rumah["Alamat"] = alamat
            data_rumah["Harga"] = harga
            data_rumah["Luas Bangunan"] = lb
            data_rumah["Luas Tanah"] = lt
            data_rumah["Nomor Handphone"] = hp
            time.sleep(2)
            clear_screen()
            print("="*60)
            print("||       Berikut Ini Data Rumah Yang Anda Masukkan!       ||")
            print("="*60)
            for w,x in data_rumah.items():
                print("||\t",w,":",x)
            print("="*60)
            confirm = input("|| Konfirmasi Data Rumah Berikut (Ya/Tidak) : ").lower()
            print("="*60)
            if confirm == "ya":
                rumah[len(rumah)+1]=data_rumah
                print("\n    Sukses Menambahkan Data Rumah!!\n")
            else:
                print("\n Data Rumah Tidak Ditambahkan!!\n")
            print("="*60)
            input(color.w+"\n    Tekan Enter Untuk Kembali......")
            time.sleep(4)
            admin()    
        elif pilihan1 == ("5" or"kembali"):
            print(color.g+"="*60)
            print("\n    Menampilkan Menu Login....")
            time.sleep(4)
        else:
            print(color.r+"="*60)
            print("||                  Pilihan Tidak Valid!!                 ||")
            print("="*60)
            input(color.w+"\n    Tekan Enter Untuk Kembali......")
            time.sleep(4)
            admin()

def user():
    clear_screen()
    print(color.g+60*"=")
    print("""||             Program Agensi Jual Beli Rumah             ||
||                        Menu User                       ||""")
    print(60*"=")       
    print("||                1. Beli Rumah                           ||")
    print("||                2. Jual Rumah                           ||")
    print("||                3. Kembali                              ||")
    print(60*"=")
    pilihan2=input("Masukkan Pilihan : "+color.b)
    input("\n    Tekan Enter Untuk Kembali......")

login()
