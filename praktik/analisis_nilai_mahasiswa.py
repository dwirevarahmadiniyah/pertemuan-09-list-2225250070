def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menggunakan fungsi
rata = rata_rata(nilai)
daftar_lulus = nilai_lulus(nilai)
daftar_tidak_lulus = [x for x in nilai if x < 60]

# Menampilkan ringkasan
print("=== RINGKASAN NILAI MAHASISWA ===")
print("Daftar nilai:", nilai)
print(f"Jumlah mahasiswa: {len(nilai)}")
print(f"Rata-rata nilai: {rata:.2f}")
print("Nilai lulus:", daftar_lulus)
print(f"Jumlah mahasiswa lulus: {len(daftar_lulus)}")
print("Nilai tidak lulus:", daftar_tidak_lulus)
print(f"Jumlah mahasiswa tidak lulus: {len(daftar_tidak_lulus)}")
