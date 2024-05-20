stok = []
def add():
    nama_barang = input("Masukkan nama barang : ").title()
    stok_barang = input("Masukkan stok barang : ")
    barang = {"nama" : nama_barang, "stok" : stok_barang}
    stok.append(barang)
    return "--- Data berhasil ditambahkan ---"

def edit():
    input_data = int(input("Hapus data ke : "))
    input_data -= 1
    input_nama = input("Masukkan nama : ").title()
    input_stok = int(input("Masukkan stok : "))
    data_change = {"nama" : input_nama, "stok" : input_stok}
    stok[input_data] = data_change
    return "--- Data berhasil diperbarui ---"

def delete():
    input_data = int(input("Hapus data ke : "))
    input_data -= 1
    del stok[input_data]
    return "--- Data berhasil dihapus ---"

def search():
    input_data = input("Cari nama barang : ").title()
    number = 1
    result = []
    for i in stok:
        if input_data in i['nama']:
            result.append(i)
        if result:
            for i in result:
                print(f"{number}. {i['nama']} , Stok : {i['stok']}")
                number += 1
        else:
            print("--- Data tidak ditemukan ---")
        return ""

def list():
    print("--- Data barang ---")
    number = 1
    for i in stok:
        print(f"{number}. {i['nama']} , Stok : {i['stok']}")
        number += 1
    return ""

def total():
    data = f"Jumlah data tersimpan : {len(stok)}"
    return data