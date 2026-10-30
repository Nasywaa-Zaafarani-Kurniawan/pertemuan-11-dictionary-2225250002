# pertemuan-11-dictionary-2225250002

---

## Tujuan Repositori

Repositori ini dibuat untuk memenuhi tugas praktikum Pertemuan 11 mata kuliah Algoritma dan Pemrograman. Repositori ini berfokus pada penggunaan *dictionary/map* dalam Python, khususnya pengelolaan pasangan *key-value*, akses data berdasarkan *key*, manipulasi data, iterasi, serta penerapan *nested dictionary* dan fungsi untuk mengelola data mahasiswa.

---

## Algoritma Tugas

1. **Inisialisasi Data**: Buat sebuah *dictionary* bernama `data_mahasiswa` dengan NIM sebagai *key* utama. Setiap *value* berupa *dictionary* yang berisi nama, kelas, dan nilai mahasiswa. Siapkan minimal lima data mahasiswa.

2. **Pencarian Data Mahasiswa**:
   - Buat fungsi `cari_mahasiswa(data, nim)` untuk mencari data berdasarkan NIM.
   - Gunakan `get()` atau pemeriksaan `in` agar pencarian NIM yang tidak tersedia tidak menyebabkan `KeyError`.
   - Tampilkan data mahasiswa jika NIM ditemukan dan pesan "Data tidak ditemukan" jika NIM tidak tersedia.

3. **Penambahan Data**: Tambahkan satu mahasiswa baru ke dalam *dictionary* menggunakan NIM sebagai *key* dan data nama, kelas, serta nilai sebagai *value*.

4. **Pembaruan Data**: Ubah nilai salah satu mahasiswa dengan mengakses NIM dan *key* nilai pada *nested dictionary*.

5. **Menampilkan Seluruh Data**: Gunakan `items()` untuk menelusuri dan menampilkan seluruh pasangan NIM beserta informasi mahasiswa.

6. **Menghitung Rata-rata Nilai**:
   - Buat fungsi `rata_rata_nilai(data)` untuk menjumlahkan seluruh nilai mahasiswa.
   - Hitung rata-rata dengan membagi total nilai dengan jumlah mahasiswa.
   - Tangani kondisi *dictionary* kosong agar tidak terjadi error pembagian dengan nol.

7. **Output Data**: Tampilkan hasil pencarian, data setelah penambahan dan pembaruan, seluruh rekap mahasiswa, serta rata-rata nilai kelas.

---

## Hasil Pengujian (Test Case Wajib)

| Data / Aksi | Yang diperiksa | Hasil yang diharapkan | Status |
| :--- | :--- | :--- | :-: |
| `A003` | Pencarian NIM tersedia | Data Citra ditampilkan | Sesuai |
| `A999` | Pencarian NIM tidak tersedia | Data tidak ditemukan | Sesuai |
| `A002` menjadi `82` | Pembaruan nilai mahasiswa | Nilai A002 berubah menjadi 82 | Sesuai |
| Menambahkan `A006` | Penambahan data mahasiswa | Key A006 tersedia setelah ditambahkan | Sesuai |
| `items()` | Menampilkan rekap data | Seluruh NIM dan data mahasiswa ditampilkan | Sesuai |
| Seluruh data mahasiswa | Perhitungan rata-rata nilai | Rata-rata nilai ditampilkan dengan benar | Sesuai |

---

## Cara Menjalankan

Buka terminal di direktori utama repositori ini, lalu jalankan program utama menggunakan perintah berikut:

```bash
python3 praktik/data_mahasiswa.py
```

---

## Refleksi
Kendala yang perlu diperhatikan dalam penggunaan dictionary adalah kemungkinan terjadinya KeyError ketika program mengakses key yang tidak tersedia. Hal ini dapat diatasi dengan memeriksa keberadaan key menggunakan operator in atau menggunakan method get() agar proses pencarian data lebih aman.
