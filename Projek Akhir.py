import os
import time

#color
class color:
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'
    w = '\033[0m'

#time sleep
print("\n    LOADING.......0%")
time.sleep(3)
print("\n    LOADING.......25%")
time.sleep(3)
print(color.y+"\n    LOADING.......50%")
time.sleep(2)
print(color.y+"\n    LOADING.......75%")
time.sleep(2)
print(color.g+"\n    LOADING COMPLETE!!!")
time.sleep(1)

#data-data
rumah = {"059":{"Nama Pemilik" : "Rizky Hardian Nor","Tipe": 36, "Alamat" : "Jl. M. Yamin No. 59","Harga (Rp)" : 214000000,"Luas Bangunan (m²)" : 40, "Luas Tanah (m²)" : 60, "Nomor Handphone": "082233445559"}, 
        "067":{"Nama Pemilik":"Jerry Fitriansyah", "Tipe": 54, "Alamat" : "Jl. Pramuka 2A No. 67", "Harga (Rp)" : 980000000,"Luas Bangunan (m²)" : 59, "Luas Tanah (m²)" : 105,"Nomor Handphone":"08765432167"},
        "092":{"Nama Pemilik":"Dani Aprilianto","Tipe":45,"Alamat":"Jl. Perjuangan Baru No. 92","Harga (Rp)": 920000000, "Luas Bangunan (m²)":47,"Luas Tanah (m²)":110, "Nomor Handphone":"080813756492"}}
 
username = ["admin","user"]
password = ["2159","6792"]

#Fungsi-fungsi
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def login():
    while True:
        clear_screen()
        print(color.g+"="*60)
        print("""||                   Selamat Datang Di                    ||
||             Program Agensi Jual Beli Rumah             ||""")
        print("="*60)
        print("||                1. Login                                ||")
        print("||                2. Keluar                               ||")
        print("="*60)
        pilihan = input("||    Masukkan Pilihan : "+color.y).lower()
        if pilihan == "1" or pilihan == "login":
            print(color.g+"="*60)
            auth_username = input("||    Masukkan Username : "+color.y).lower()
            auth_password = input(color.g+"||    Masukkan Password : "+color.y)
            if auth_username == username[0] and auth_password == password[0]:
                print(color.g+"="*60)
                print(color.w+"\n    Login Berhasil...")
                time.sleep(2)
                print("\n    Menampilkan Menu Admin....")
                time.sleep(3)
                admin()
            elif auth_username == username[1] and auth_password == password[1]:
                print (color.g+"="*60)
                print(color.w+"\n    Login Berhasil...")
                time.sleep(2)
                print("\n    Menampilkan Menu User....")
                time.sleep(3)
                user()
            else:
                print(color.r+"="*60)
                print("||       Error! Username dan Password Tidak Valid!!       ||")
                print("="*60)
                input(color.w+"\n    Tekan Enter Untuk Kembali......")
                time.sleep(3)
        elif pilihan == "2" or pilihan == "keluar":
            print(color.g+"="*60)
            print ("||       Terimakasih Telah Menggunakan Program Kami       ||")
            print("="*60)
            time.sleep(3)
            break
        else:
            print(color.r+"="*60)
            print("||              Error! Pilihan Tidak Valid!!              ||")
            print("="*60)
            input(color.w+"\n    Tekan Enter Untuk Kembali......")
            time.sleep(3)

def admin():
    clear_screen()
    print(color.g+60*"=")
    print("""||             Program Agensi Jual Beli Rumah             ||
||                       Menu Admin                       ||""")
    print(60*"=")
    print("||                  1. Lihat Data Rumah                   ||")
    print("||                  2. Tambahkan Data Rumah               ||")
    print("||                  3. Ubah Data Rumah                    ||")
    print("||                  4. Hapus Data Rumah                   ||")
    print("||                  5. Kembali                            ||")
    print("="*60)
    pilihan1=input("||    Masukkan Pilihan : "+color.y).lower()
        
    if pilihan1 == "1" or pilihan1 == "lihat data rumah":
        lihat_rumah()
        input(color.w+"\n    Tekan Enter Untuk Kembali......")
        time.sleep(1)
        print("\n    Menampilkan Menu Admin....")
        time.sleep(4)
        admin()
            
    elif pilihan1 == "2" or pilihan1 == "tambahkan data rumah":
        stop = False
        while (not stop):
            tambah_rumah()
            stop10 = False
            while (not stop10):
                print(color.g+"="*60)
                tambah_lagi = input("|| Apakah Anda Masih Ingin Menambahkan Data Rumah? ('Ya'/'Tidak') : "+color.y).lower()
                if tambah_lagi == "tidak":
                    print(color.g+"="*60)
                    stop10 = True
                    stop = True
                    input(color.w+"\n    Tekan Enter Untuk Kembali......")
                    time.sleep(4)
                    print("\n    Menampilkan Menu Admin....")
                    time.sleep(2)
                    admin()
                elif tambah_lagi == "ya":
                    print(color.g+"="*60)
                    stop10 = True
                else:
                    print(color.r+"||    Error! Pilihan Tidak Valid!!")
            
    elif pilihan1 == "3" or pilihan1 == "ubah data rumah":
        stop11 = False
        while (not stop11):
            update_data_rumah()
            stop13 = False
            while (not stop13):
                print(color.g+"="*60)
                update_lagi = input("|| Apakah Anda Masih Ingin Mengubah Data Rumah? ('Ya'/'Tidak') : "+color.y).lower()
                if update_lagi == "tidak":
                    stop13 = True
                    stop11 = True
                    print(color.g+"="*60)
                    input(color.w+"\n    Tekan Enter Untuk Kembali......")
                    time.sleep(4)
                    print("\n    Menampilkan Menu Admin....")
                    time.sleep(2)
                    admin()
                elif update_lagi == "ya":
                    print(color.g+"="*60)
                    stop13 = True
                else:
                    print(color.r+"||    Error! Pilihan Tidak Valid!!")
                        
    elif pilihan1 == "4" or pilihan1 == "hapus data rumah":
        stop14 = False
        while (not stop14):
            hapus_data_rumah(0)
            stop15 = False
            while (not stop15):
                print(color.g+"="*60)
                hapus_lagi = input("|| Apakah Anda Masih Ingin Menghapus Data Rumah? ('Ya'/'Tidak') : "+color.y).lower()
                if hapus_lagi == "tidak":
                    stop15 = True
                    stop14 = True
                    print(color.g+"="*60)
                    input(color.w+"\n    Tekan Enter Untuk Kembali......")
                    time.sleep(4)
                    print("\n    Menampilkan Menu Admin....")
                    time.sleep(2)
                    admin()
                elif hapus_lagi == "ya":
                    print(color.g+"="*60)
                    stop15 = True
                else:
                    print(color.r+"||    Error! Pilihan Tidak Valid!!")
            
    elif pilihan1 == "5" or pilihan1 == "kembali":
        print(color.g+"="*60)
        time.sleep(2)
        print(color.w+"\n    Menampilkan Menu Login....")
        time.sleep(4)
            
    else:
        print(color.r+"="*60)
        print("||              Error! Pilihan Tidak Valid!!              ||")
        print("="*60)
        input(color.w+"\n    Tekan Enter Untuk Kembali......")
        time.sleep(4)
        admin()
             
def user():
    clear_screen()
    print(color.g+60*"=")
    print("""||             Program Agensi Jual Beli Rumah             ||
||                       Menu User                        ||""")
    print(60*"=")       
    print("||                  1. Lihat Rumah                        ||")
    print("||                  2. Jual Rumah                         ||")
    print("||                  3. Beli Rumah                         ||")
    print("||                  4. Kembali                            ||")
    print(60*"=")
    pilihan2 = input("Masukkan Pilihan : "+color.y).lower()
    if pilihan2 == "1" or pilihan2 == "lihat rumah":
        lihat_rumah()
        input(color.w+"\n    Tekan Enter Untuk Kembali......")
        time.sleep(1)
        print("\n    Menampilkan Menu User....")
        time.sleep(4)
        user()
        
    elif pilihan2 == "2" or pilihan2 == "jual rumah":
        stop16 = False
        while (not stop16):
            tambah_rumah()
            stop17 = False
            while (not stop17):
                print(color.g+"="*60)
                tambah_lagi = input("|| Apakah Anda Masih Ingin Menjual Rumah? ('Ya'/'Tidak') : "+color.y).lower()
                if tambah_lagi == "tidak":
                    stop17 = True
                    stop16 = True
                    print(color.g+"="*60)
                    input(color.w+"\n    Tekan Enter Untuk Kembali......")
                    time.sleep(4)
                    print("\n    Menampilkan Menu User....")
                    time.sleep(2)
                    user()
                elif tambah_lagi == "ya":
                    print(color.g+"="*60)
                    stop17 = True
                else:
                    print(color.r+"||    Error!  Pilihan Tidak Valid!!")
    
    elif pilihan2 == "3" or pilihan2 == "beli rumah": 
        stop17 = False
        while (not stop17):
            hapus_data_rumah(1)
            stop18 = False
            while (not stop18):
                print(color.g+"="*60)
                hapus_lagi = input("|| Apakah Anda Masih Ingin Membeli Rumah? ('Ya'/'Tidak') : "+color.y).lower()
                if hapus_lagi == "tidak":
                    stop18 = True
                    stop17 = True
                    print(color.g+"="*60)
                    input(color.w+"\n    Tekan Enter Untuk Kembali......")
                    time.sleep(4)
                    print("\n    Menampilkan Menu User....")
                    time.sleep(2)
                    user()
                elif hapus_lagi == "ya":
                    print(color.g+"="*60)
                    stop18 = True
                else:
                    print(color.r+"||    Error! Pilihan Tidak Valid!!")
        
    elif pilihan2 == "4" or pilihan2 == "kembali":
        print(color.g+"="*60)
        time.sleep(2)
        print(color.w+"\n    Menampilkan Menu Login....")
        time.sleep(4)
        
    else:
        print(color.r+"="*60)
        print("||              Error! Pilihan Tidak Valid!!              ||")
        print("="*60)
        input(color.w+"\n    Tekan Enter Untuk Kembali......")
        time.sleep(4)
        user()
                
def lihat_rumah():
    time.sleep(3)
    clear_screen()
    print(color.g+"="*60)
    print("||             Program Agensi Jual Beli Rumah             ||")
    print("||              Daftar Rumah Yang Tersedia!!              ||")
    print("="*60)
    for w,x in rumah.items():
        print("|| ID",w)
        for y,z in x.items():
            print("||\t",y,":",z)
        print("="*60)
    time.sleep(2)
    
def tambah_rumah():         
    time.sleep(2)
    clear_screen()
    print(color.g+"="*60)
    print("||             Program Agensi Jual Beli Rumah             ||")
    print("||                     Isi Data Rumah                     ||")
    print("="*60)
    stop1 = False
    while (not stop1):
        id_rumah = input(color.g+"||    Masukkan ID (3 digits) : "+color.y)
        if id_rumah.isdigit():
            if len(id_rumah) != 3:
                print(color.r+"||    Error! Masukkan ID Dengan Benar!!")
            else:
                if id_rumah in rumah.keys():
                    print(color.r+"||    Error! ID Sudah Ada! Silahkan Masukkan ID Yang Lain!!")
                else:
                    if id_rumah == "000":
                        print(color.r+"||    Error! Masukkan ID Dengan Benar!!")
                    else:
                        stop1 = True
        else:
            print(color.r+"||    Error! Masukkan ID Dengan Benar!!")
    stop2 = False
    while (not stop2):
        pemilik_rumah = input(color.g+"||    Masukkan Nama Pemilik Rumah : "+color.y).title()
        if len(pemilik_rumah) <= 2:
            print(color.r+"||    Error! Nama Terlalu Pendek!!")
        else:
            stop2 = True
    stop3 = False
    while (not stop3):
        try:
            tipe_rumah = int(input(color.g+"||    Masukkan Nomor Tipe Rumah : "+color.y))
            if tipe_rumah <= 1:
                print(color.r+"||    Error! Tipe Rumah Terlalu Kecil!!")
                continue
            else:
                if tipe_rumah > 500:
                    print(color.r+"||    Error! Tipe Rumah Terlalu Besar!!")
                    continue
                else:
                    stop3 = True
        except ValueError:
            print(color.r+"||    Error! Masukkan Tipe Rumah Dengan Benar!!")
            continue
    stop4 = False
    while (not stop4):
        alamat_rumah = input(color.g+"||    Masukkan Alamat Rumah : "+color.y).title()
        if len(alamat_rumah) <= 5:
            print(color.r+"||    Error! Alamat Terlalu Pendek!!")
        else:
            stop4 = True
    stop5 = False
    while (not stop5):
        try:
            harga_rumah = int(input(color.g+"||    Masukkan Harga Rumah (Rp) : "+color.y))
            if harga_rumah < 0:
                print(color.r+"||    Error! Masukkan Harga Dengan Benar!!")
                continue
            else:
                stop5 = True
        except ValueError:
            print(color.r+"|| Masukkan Harga Dengan Benar!!")
            continue
    stop6 = False
    while (not stop6):
        try:
            luas_bangunan = int(input(color.g+"||    Masukkan Luas Bangunan (m²) : "+color.y))
            if luas_bangunan <= 1:
                print(color.r+"||    Error! Masukkan Luas Bangunan Dengan Benar!!")
            else:
                if luas_bangunan != tipe_rumah:
                    print(color.r+f"||    Error! Nilai Luas Bangunan Harus Sama Dengan Nilai Tipe Rumah!! (Tipe Rumah = {tipe_rumah})")
                    continue
                else:
                    stop6 = True
        except ValueError:
            print(color.r+"||    Error! Masukkan Luas Bangunan Dengan Benar!!")
            continue
        stop7 = False
        while (not stop7):
            try:
                luas_tanah = int(input(color.g+"||    Masukkan Luas Tanah (m²) : "+color.y))
                if luas_tanah <= luas_bangunan:
                    print(color.r+"||    Error! Luas Tanah Harus Lebih Besar Dari Luas Bangunan!!")
                    continue
                else:
                     stop7 = True
            except ValueError:
                print(color.r+"||    Error! Masukkan Luas Tanah Dengan Benar!!")
                continue
        stop8 = False
        while (not stop8):
            handphone = input(color.g+"||    Masukkan Nomor Handphone Pemilik : "+color.y)
            if handphone.isdigit():
                if len(handphone) >=4:
                    if len(handphone) >20:
                        print(color.r+"||    Error! Nomor Handphone Terlalu Panjang!!")
                    else:
                        stop8 = True
                else:
                    print(color.r+"||    Error! Nomor Handphone Terlalu Pendek!!")
            else:  
                print(color.r+"||    Error! Masukkan Nomor Handphone Dengan Benar!!")
        rumah_baru = {}
        rumah_baru["Nama Pemilik"] = pemilik_rumah
        rumah_baru["Tipe"] = tipe_rumah
        rumah_baru["Alamat"] = alamat_rumah
        rumah_baru["Harga (Rp)"] = harga_rumah
        rumah_baru["Luas Bangunan (m²)"] = luas_bangunan
        rumah_baru["Luas Tanah (m²)"] = luas_tanah
        rumah_baru["Nomor Handphone"] = handphone
        time.sleep(2)
        clear_screen()          
        print(color.g+"="*60)
        print("||       Berikut Ini Data Rumah Yang Anda Masukkan!       ||")
        print("="*60)
        print("|| ID", id_rumah)
        for w,x in rumah_baru.items():
            print("||\t",w,":",x)
        print("="*60)
        stop9 = False
        while (not stop9):
            confirm = input(color.g+"|| Konfirmasi Penambahan Data Rumah Berikut ('Ya'/'Tidak') : "+color.y).lower()
            time.sleep(3)
            if confirm == "ya":
                rumah[id_rumah] = rumah_baru
                print(color.g+"="*60)
                print("\n    Sukses Menambahkan Data Rumah!!\n")
                stop9 = True
            elif confirm == "tidak":
                print(color.g+"="*60)
                print("\n Data Rumah Tidak Jadi Ditambahkan!!\n")
                stop9 = True
            else:
                print(color.r+"||    Error! Pilihan Tidak Valid!!")
        
def hapus_data_rumah(x):
    lihat_rumah()
    id_rumah = input(color.g+"|| Masukkan ID Rumah : "+color.y)
    print(color.g+"="*60)
    if id_rumah not in rumah.keys():
       print(color.r+"||    Error! ID Rumah Tidak Ditemukan!!")
    else:
        if x == 0:
            hapus_rumah = rumah.get(id_rumah)
            time.sleep(3)
            clear_screen()
            print(color.g+"="*60)
            print("||      Berikut Ini Data Rumah Yang Ingin Anda Hapus      ||")
            print("="*60)
            print("|| ID",id_rumah)
            for w,x in hapus_rumah.items():
                print("||\t",w,":",x)
            print("="*60)
            stop12 = False
            while (not stop12):
                confirm = input(color.g+"|| Konfirmasi Panghapusan Data Rumah Berikut ('Ya'/'Tidak') : "+color.y).lower()
                if confirm == "ya":
                    print(color.g+"="*60)
                    del rumah[id_rumah]
                    print("||             Sukses Menghapus Data Rumah              ||")
                    stop12 = True
                elif confirm == "tidak":
                    print(color.g+"="*60)
                    print("||\tData Rumah Tidak Jadi Dihapus!!")
                    stop12 = True
                else:
                    print(color.r+"||    Error! Pilihan Tidak Valid!!")
        elif x == 1:
            beli_rumah = rumah.get(id_rumah)
            time.sleep(3)
            clear_screen()
            print(color.g+"="*60)
            print("||       Berikut Ini Data Rumah Yang Ingin Anda Beli      ||")
            print("="*60)
            print("|| ID",id_rumah)
            for w,x in beli_rumah.items():
                print("||\t",w,":",x)
            print("="*60)
            stop12 = False
            while (not stop12):
                confirm = input(color.g+"|| Konfirmasi Pembelian Rumah Berikut ('Ya'/'Tidak') : "+color.y).lower()
                if confirm == "ya":
                    print(color.g+"="*60)
                    del rumah[id_rumah]
                    print("||                  Sukses Membeli Rumah                  ||")
                    stop12 = True
                elif confirm == "tidak":
                    print(color.g+"="*60)
                    print("||\tRumah Tidak Jadi Dibeli!!")
                    stop12 = True
                else:
                    print(color.r+"||    Error! Pilihan Tidak Valid!!")

def update_data_rumah():
    lihat_rumah()
    id_rumah = input(color.g+"|| Pilih ID Rumah : "+color.y)
    print(color.g+"="*60)
    if id_rumah not in rumah.keys():
        print(color.r+"||    Error! ID Rumah Tidak Ditemukan!!")
    else:
        ubah_rumah = rumah.get(id_rumah)
        time.sleep(3)
        clear_screen()
        print(color.g+"="*60)
        print("||       Berikut Ini Data Rumah Yang Ingin Anda Ubah      ||")
        print("="*60)
        for w,x in ubah_rumah.items():
            print("||\t",w,":",x)
        print("="*60)
        stop12 = False
        while (not stop12):
            confirm = input(color.g+"|| Konfirmasi Data Rumah Berikut ('Ya'/'Tidak') : "+color.y).lower()
            if confirm == "ya":
                print(color.g+"="*60)
                stop12 = True
                stop2 = False
                while (not stop2):
                    pemilik_rumah = input(color.g+"||    Masukkan Nama Pemilik Rumah : "+color.y).title()
                    if len(pemilik_rumah) <= 2:
                        print(color.r+"||    Error! Nama Terlalu Pendek!!")
                    else:
                        stop2 = True
                stop3 = False
                while (not stop3):
                    try:
                        tipe_rumah = int(input(color.g+"||    Masukkan Nomor Tipe Rumah : "+color.y))
                        if tipe_rumah <= 1:
                            print(color.r+"||    Error! Tipe Rumah Terlalu Kecil!!")
                            continue
                        else:
                            if tipe_rumah > 500:
                                print(color.r+"||    Error! Tipe Rumah Terlalu Besar!!")
                                continue
                            else:
                                stop3 = True
                    except ValueError:
                        print(color.r+"||    Error! Masukkan Tipe Rumah Dengan Benar!!")
                        continue
                stop4 = False
                while (not stop4):
                    alamat_rumah = input(color.g+"||    Masukkan Alamat Rumah : "+color.y).title()
                    if len(alamat_rumah) <= 5:
                        print(color.r+"||    Error! Alamat Terlalu Pendek!!")
                    else:
                        stop4 = True
                stop5 = False
                while (not stop5):
                    try:
                        harga_rumah = int(input(color.g+"||    Masukkan Harga Rumah (Rp) : "+color.y))
                        if harga_rumah < 0:
                            print(color.r+"||    Error! Masukkan Harga Dengan Benar!!")
                            continue
                        else:
                            stop5 = True
                    except ValueError:
                        print(color.r+"|| Masukkan Harga Dengan Benar!!")
                        continue
                stop6 = False
                while (not stop6):
                    try:
                        luas_bangunan = int(input(color.g+"||    Masukkan Luas Bangunan (m²) : "+color.y))
                        if luas_bangunan <= 1:
                            print(color.r+"||    Error! Masukkan Luas Bangunan Dengan Benar!!")
                        else:
                            if luas_bangunan != tipe_rumah:
                                print(color.r+f"||    Error! Nilai Luas Bangunan Harus Sama Dengan Nilai Tipe Rumah!! (Tipe Rumah = {tipe_rumah})")
                                continue
                            else:
                                stop6 = True
                    except ValueError:
                        print(color.r+"||    Error! Masukkan Luas Bangunan Dengan Benar!!")
                        continue
                stop7 = False
                while (not stop7):
                    try:
                        luas_tanah = int(input(color.g+"||    Masukkan Luas Tanah (m²) : "+color.y))
                        if luas_tanah <= luas_bangunan:
                            print(color.r+"||    Error! Luas Tanah Harus Lebih Besar Dari Luas Bangunan!!")
                            continue
                        else:
                            stop7 = True
                    except ValueError:
                        print(color.r+"||    Error! Masukkan Luas Tanah Dengan Benar!!")
                        continue
                stop8 = False
                while (not stop8):
                    handphone = input(color.g+"||    Masukkan Nomor Handphone Pemilik : "+color.y)
                    if handphone.isdigit():
                        if len(handphone) >=4:
                            if len(handphone) >20:
                                print(color.r+"||    Error! Nomor Handphone Terlalu Panjang!!")
                            else:
                                stop8 = True
                        else:
                            print(color.r+"||    Error! Nomor Handphone Terlalu Pendek!!")
                    else:  
                        print(color.r+"||    Error! Masukkan Nomor Handphone Dengan Benar!!")
                ubah_rumah["Nama Pemilik"] = pemilik_rumah
                ubah_rumah["Tipe"] = tipe_rumah
                ubah_rumah["Alamat"] = alamat_rumah
                ubah_rumah["Harga (Rp)"] = harga_rumah
                ubah_rumah["Luas Bangunan (m²)"] = luas_bangunan
                ubah_rumah["Luas Tanah (m²)"] = luas_tanah
                ubah_rumah["Nomor Handphone"] = handphone

                time.sleep(2)
                clear_screen()          
                print(color.g+"="*60)
                print("||       Berikut Ini Data Rumah Yang Anda Masukkan!      ||")
                print("="*60)
                print("|| ID", id_rumah)
                for w,x in ubah_rumah.items():
                    print("||\t",w,":",x)
                print("="*60)
                stop9 = False
                while (not stop9):
                    confirm = input(color.g+"|| Konfirmasi Perubahan Data Rumah Berikut ('Ya'/'Tidak') : "+color.y).lower()
                    time.sleep(3)
                    if confirm == "ya":
                        rumah[id_rumah] = ubah_rumah
                        print(color.g+"="*60)
                        print("\n    Sukses Mengubah Data Rumah!!\n")
                        stop9 = True
                    elif confirm == "tidak":
                        print(color.g+"="*60)
                        print("\n Data Rumah Tidak Jadi Diubah!!\n")
                        stop9 = True
                    else:
                        print(color.r+"||    Error! Pilihan Tidak Valid!!")
            elif confirm == "tidak":
                print(color.g+"="*60)
                print("\tData Rumah Tidak Jadi Diubah!!")
                stop12 = True
            else:
                print(color.r+"||    Error! Pilihan Tidak Valid!!")

login()
