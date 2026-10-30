def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")
mahasiswa = {
"24126xxxx1": {"nama": "August", "nilai": 67},
"24126xxxx2": {"nama": "Jason", "nilai": 86}
}

print(cari(mahasiswa, "24126xxxx2"))
print(cari(mahasiswa, "24126xxxx3"))