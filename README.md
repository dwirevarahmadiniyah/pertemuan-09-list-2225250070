# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Dwi Reva Rahmadiniyah  
**NIM:** 2225250070 
**Kelas:** 3E

## Tujuan

Tujuan praktikum ini adalah memahami penggunaan list dalam Python dan mengolah kumpulan data numerik. Melalui praktikum ini, saya belajar mengakses dan mengubah elemen list, menghitung jumlah serta rata-rata nilai, dan menentukan mahasiswa yang lulus berdasarkan batas nilai tertentu.

## Struktur Program

Program pada pertemuan ini terdiri dari folder `latihan` dan `praktik`.

1. **Folder `latihan`** digunakan untuk mencoba dasar-dasar list, seperti membuat list, mengakses elemen menggunakan indeks, melakukan slicing, menambah dan menghapus elemen, serta menghitung statistik sederhana.

2. **Folder `praktik`** berisi file `analisis_nilai_mahasiswa.py` yang digunakan untuk mengolah data nilai mahasiswa. Program ini menghitung rata-rata nilai, menyeleksi nilai yang memenuhi batas kelulusan, serta menampilkan jumlah mahasiswa yang lulus dan tidak lulus.

## Cara Menjalankan

Untuk menjalankan program, buka terminal pada folder utama proyek, kemudian masukkan perintah berikut:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Jika menggunakan Windows dan perintah tersebut tidak dapat dijalankan, gunakan:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

## Test Case

**Data yang digunakan:**

```python
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
```

Batas kelulusan ditetapkan sebesar 60. Mahasiswa dinyatakan lulus apabila memperoleh nilai lebih besar dari atau sama dengan 60.

| Komponen | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Jumlah mahasiswa | 10 | 10 | Berhasil |
| Total nilai | 695 | 695 | Berhasil |
| Rata-rata nilai | 69.50 | 69.50 | Berhasil |
| Nilai lulus | [78, 90, 67, 60, 82, 71, 88] | [78, 90, 67, 60, 82, 71, 88] | Berhasil |
| Jumlah mahasiswa lulus | 7 | 7 | Berhasil |
| Nilai tidak lulus | [55, 45, 59] | [55, 45, 59] | Berhasil |
| Jumlah mahasiswa tidak lulus | 3 | 3 | Berhasil |

*Catatan: Hasil aktual di atas sesuai dengan kode program yang telah dibuat sebelumnya. Pastikan kembali dengan menjalankan program di VS Code.*

## Refleksi

Melalui praktikum ini, saya memahami bahwa list dapat digunakan untuk menyimpan banyak nilai dalam satu variabel. Setiap elemen list memiliki indeks yang dimulai dari 0, sehingga elemen pertama dapat diakses menggunakan indeks 0. Saya juga memahami cara menggunakan perulangan dan kondisi untuk menyeleksi nilai mahasiswa yang memenuhi batas kelulusan.

Salah satu kesalahan yang berhasil saya perbaiki adalah penulisan indentasi pada perulangan `for` dan kondisi `if`. Saya belajar bahwa kode di dalam blok perulangan dan kondisi harus ditulis dengan indentasi yang benar agar program dapat berjalan tanpa kesalahan.
