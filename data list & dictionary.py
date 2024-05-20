import modul as mod


print("selamat datang di program menejemen stok barang")
print("1.tambah data barang")
print("2.edit")
print("3.hapus data barang")
print("4.cari data")
print("5.tampilkan data barang")
print("6.tampilkan jumlah data")
print("7.keluar")
while True :
    pilihan = int(input("masukan pilihan : "))
    if pilihan == 1 :
        mod.tambah_data()
    elif pilihan == 2 :
        mod.edit_data()
    elif pilihan == 3 :
        mod.hapus_data()
    elif pilihan == 4 :
        mod.cari_data()
    elif pilihan == 5 :
        mod.tampil_data()
    elif pilihan == 6 :
        mod.jumlah_data()
    elif pilihan == 7 :
        print("terima kasih")
        break