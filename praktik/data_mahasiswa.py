def cari_mahasiswa(data, nim):
    return data.get(nim)
def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

data_mahasiswa = {
"24126xxxx1": {"nama": "August", "nilai": 67},
"24126xxxx2": {"nama": "Jason", "nilai": 86},
"24126xxxx3": {"nama": "Kaito", "nilai": 92},
"24126xxxx4": {"nama": "Rafael", "nilai": 87},
"24126xxxx5": {"nama": "Jude", "nilai": 84}
}
nim = input("Masukkan NIM mahasiswa: ")
hasil = cari_mahasiswa(data_mahasiswa, nim)
if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

data_mahasiswa["24126xxxx6"] = {
"nama": "William",
"kelas": "B",
"nilai": 89
}
data_mahasiswa["24126xxxx2"]["nilai"] = 82
for nim, info in data_mahasiswa.items():
    print(nim, info)
print(f"Rata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")
