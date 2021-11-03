print("=================================================================================================================================")
print("                                                             Toko Trundul")
print("                                                 Menjual barang peralatan rumah tangga")
print("=================================================================================================================================")

#saya membuat inv sebagai dictionary dari barang-barang yang tersedia di toko
inv = {"keranjang":30000,"wajan":45000,"gayung":5000,"panci":30000,"ember":15000,"toples":10000,"dispenser":40000,"sendok":5000,"garpu":5000,"piring":35000,"mangkok":40000,"sikat":2000,"sapu":20000,"baskom":10000}
basket=[]
total=[]

#FUNGSI MESIN KASIR
def kasir():
  user_basket = input("Hi, barang apa yang ingin anda beli? : ").lower()
  while user_basket != "keluar":
    if user_basket in inv:
      basket.append(user_basket)
      user_basket=input("Baik, saya akan menambahkannya di keranjang anda, apa ada lagi yang ingin anda beli? (tulis 'keluar' jika tidak ada) : ").lower()
    else:
      user_basket=input("Mohon maaf, barang yang anda inginkan tidak tersedia. Silahkan pilih barang yang lain.(tulis 'keluar' jika tidak ada) : ").lower()

#FUNGSI KALKULASI DISKON
def diskon():
  if 100000 >= harga_total >= 50000:
    harga_diskon = harga_total-harga_total*(10/100)
    print("Selamat anda mendapatkan diskon sebesar 10%")
    print("Total harga barang anda sebelum diskon sebanyak Rp.", harga_total)
    print("Total harga yang harus anda bayar sebanyak Rp.", harga_diskon)
  elif harga_total >= 100000:
     harga_diskon= harga_total-harga_total*(25/100)
     print("Selamat anda mendapatkan diskon sebesar 25%")
     print("Total harga barang anda sebelum diskon sebanyak Rp.", harga_total)
     print("Total harga yang harus anda bayar sebanyak Rp.", harga_diskon)
  else:
    print("Total harga yang harus anda bayar sebanyak Rp.", harga_total)

kasir()

print("Ini adalah barang-barang yang ada di keranjang anda : ",basket)
answer=input("Apakah masih ada barang yang anda inginkan? yes/no : ").lower()
if answer == "yes":
  kasir()
  print("Ini adalah semua barang yang anda pesan :",basket)
  for items in basket:
    total.append(inv[items])
  harga_total=sum(total)
  diskon()
else:
  for items in basket:
    total.append(inv[items])
  harga_total=sum(total)
  diskon()

print("=================================================================================================================================")
print("                                                Terimakasih telah berkunjung")
print("=================================================================================================================================")



