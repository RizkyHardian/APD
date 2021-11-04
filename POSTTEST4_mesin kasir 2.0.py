print("||"+"="*56+"||")
print("||                      Toko Trundul                      ||")
print("||          Menjual barang peralatan rumah tangga         ||")
print("||"+"="*56+"||")

username = ["admin","user"]
password = ["059","210"]

inv = {"keranjang":30000,"wajan":45000,"gayung":5000,"panci":30000,"ember":15000,"toples":10000,"dispenser":40000,"sendok":5000,"garpu":5000,"piring":35000,"mangkok":40000,"sikat":2000,"sapu":20000,"baskom":10000}
stock = {"keranjang":30,"wajan":25,"gayung":50,"panci":50,"ember":30,"toples":100,"dispenser":10,"sendok":50,"garpu":50,"piring":50,"mangkok":40,"sikat":20,"sapu":20,"baskom":10}
basket=[]
total=[]
profit=[]

def kasir():
    print("||                  Barang yang tersedia                  ||")
    for x,y in stock.items():
        print("||  ",x,":",y)
    user_basket = input("|| Hi, barang apa yang ingin anda beli? : ").lower()
    while user_basket != "keluar":
        if user_basket in stock and user_basket in inv:
            basket.append(user_basket)
            user_basket=input("|| Baik, saya akan menambahkannya di keranjang anda, apa ada lagi yang ingin anda beli? (tulis 'keluar' jika tidak ada) : ").lower()
        else:
            user_basket=input("|| Mohon maaf, barang yang anda inginkan tidak tersedia. Silahkan pilih barang yang lain.(tulis 'keluar' jika tidak ada) : ").lower()
    print("|| Ini adalah barang-barang yang ada di keranjang anda : ",basket)
    answer=input("|| Apakah masih ada barang yang anda inginkan? yes/no : ").lower()
    if answer == "yes":
        kasir()
        print("|| Ini adalah semua barang yang anda pesan :",basket)
        for items in basket:
            total.append(inv[items])
        harga_total=sum(total)
        if 100000 >= harga_total >= 50000:
            harga_diskon = harga_total-harga_total*(10/100)
            print("|| Selamat anda mendapatkan diskon sebesar 10%")
            print("|| Total harga barang sebelum diskon sebanyak Rp.", harga_total)
        elif harga_total >= 100000:
            harga_diskon= harga_total-harga_total*(25/100)
            print("|| Selamat anda mendapatkan diskon sebesar 25%")
            print("|| Total harga barang sebelum diskon sebanyak Rp.", harga_total)
        else:
            harga_diskon = harga_total
    else:
        for items in basket:
            total.append(inv[items])
        harga_total=sum(total)
        if 100000 >= harga_total >= 50000:
            harga_diskon = harga_total-harga_total*(10/100)
            print("|| Selamat anda mendapatkan diskon sebesar 10%")
            print("|| Total harga barang sebelum diskon sebanyak Rp.", harga_total)
        elif harga_total >= 100000:
            harga_diskon= harga_total-harga_total*(25/100)
            print("|| Selamat anda mendapatkan diskon sebesar 25%")
            print("|| Total harga barang sebelum diskon sebanyak Rp.", harga_total)
        else:
            harga_diskon = harga_total
    print("|| Total harga yang harus anda bayar sebanyak Rp.", harga_diskon)
    profit.append(harga_diskon)
    print("||"+"="*56+"||") 
    print("||              Terimakasih telah berkunjung              ||")
    print("||"+"="*56+"||")
    menu_user()

def menu_user():
    print("||"+"="*56+"||")
    print("||                       MENU USER                        ||")
    print("||"+"="*56+"||")
    print("||    1. Kasir                                            ||")
    print("||    2. Logout                                           ||")
    print("||"+"="*56+"||")
    choose = input("Masukkan pilihan anda : ").lower()
    while True:
        if choose == "1" or choose == "kasir":
            kasir()
        elif choose == "2" or choose == "logout":
            login()
        else:
            print("Mohon maaf pilihan tidak tersedia!!")
            menu_user()

def login():
    print("||"+"="*56+"||")
    print("||                         LOGIN                          ||")
    print("||"+"="*56+"||")
    print("||         Silahkan masukan username dan password         ||")
    cek_username = input("||  Username : ").lower()
    cek_password = input("||  Password : ").lower()
    print("||"+"="*56+"||")
    while True:
        if cek_username == username[0] and cek_password == password[0]:
            menu_admin()
        elif cek_username == username[1] and cek_password == password[1]:
            menu_user()
        else:
            print("|| Maaf username atau password yang anda masukkan salah!!")
            print("|| Silahkan masukkan ulang username atau password yang benar")
            login()

def menu_admin():
    print("||"+"="*56+"||")
    print("||                      MENU ADMIN                        ||")
    print("||"+"="*56+"||")
    print("||    1. Tambahkan stock                                  ||")
    print("||    2. Lihat harga stock                                ||")
    print("||    3. Lihat jumlah stock                               ||")
    print("||    4. Perbarui harga stock                             ||")
    print("||    5. Perbarui jumlah stock                            ||")
    print("||    6. Hapus stock                                      ||")
    print("||    7. Logout                                           ||")
    print("||"+"="*56+"||")
    choose = input("|| Masukkan pilihan anda : ").lower()
    while True:
        if choose == "1" or choose == "tambahkan stock":
            while True:
                try:
                    new_inv = input("|| Masukkan barang yang akan ditambahkan : ").lower()
                    new_stock = int(input("|| Masukkan jumlah yang akan ditambahkan : ").lower())
                    new_price = int(input("|| Masukkan jumlah harga dari barang yang akan ditambahkan : ").lower())
                except ValueError:
                     print("|| Mohon maaf input yang anda masukkan tidak valid!!")
                     continue
                else:
                     break
            inv[new_inv]=new_price
            stock[new_inv]=new_stock
            print("|| Sukses menambahkan barang")
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin()
        elif choose == "2" or choose == "lihat harga stock":
            print("||          List harga barang")
            for x,y in inv.items():
                print("||  ",x,":",y)
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin()
        elif choose == "3" or choose == "lihat jumlah stock":
            print("||           Jumlah stock barang")
            for x,y in stock.items():
                print("||  ",x,":",y)
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin()
        elif choose == "4" or choose == "perbarui harga stock":
            new_inv = input("|| Masukkan barang yang akan diperbarui : ").lower()
            if new_inv in inv.keys():
                while True:
                    try:
                        new_price = int(input("|| Masukkan harga dari barang yang akan diperbarui : ").lower()) 
                    except ValueError:
                        print("|| Mohon maaf input yang anda masukkan tidak valid!!")
                        continue
                    else:
                        break
                stock[new_inv]=new_price
            else:
                print("|| Mohon maaf barang tersebut tidak tersedia!!")
            print("|| Sukses memperbarui harga stock")
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin()
        elif choose == "5" or choose == "perbarui jumlah stock":
            new_inv = input("|| Masukkan barang yang akan diperbarui : ").lower()
            if new_inv in inv.keys():
                while True:
                    try:
                        new_stock = int(input("|| Masukkan jumlah yang akan diperbarui : ").lower())
                    except ValueError:
                        print("|| Mohon maaf input yang anda masukkan tidak valid!!")
                        continue
                    else:
                        break
                inv[new_inv]=new_stock
            else:
                print("|| Mohon maaf barang tersebut tidak tersedia!!")
            print("|| Sukses memperbarui jumlah stock!!")
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin() 
        elif choose == "6" or choose == "hapus stock":
            new_inv = input("|| Masukkan barang yang akan dihapus : ").lower()
            if new_inv in inv.keys():
                inv.pop(new_inv)
                stock.pop(new_inv)
            else:
                print("|| Mohon maaf barang tersebut tidak tersedia!!")
            print("|| Sukses menghapus barang!!")
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin()   
        elif choose == "7" or choose == "logout":
            login()
        else:
            print("|| Mohon maaf pilihan tidak tersedia!!")
            exit = input("|| Tekan apa saja untuk kembali!!")
            menu_admin()
login()
