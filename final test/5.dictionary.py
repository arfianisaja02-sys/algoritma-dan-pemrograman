# ============================================================
# Program: Contoh Penggunaan Dictionary di Python
# Deskripsi:
#   - Dictionary adalah struktur data pasangan key-value
#   - Key harus unik, dan nilainya bisa berbagai tipe data
# ============================================================

# Membuat dictionary
mahasiswa = {
    "nama": "Andi",
    "nim": "SI2025001",
    "umur": 20,
    "jurusan": "Sistem Informasi",
    "nilai": [85, 90, 88]  # value berupa list
}

# Menampilkan seluruh dictionary
print("Data Mahasiswa:", mahasiswa)

# Mengakses data berdasarkan key
print("Nama:", mahasiswa["nama"])
print("NIM:", mahasiswa["nim"])

# Menambah data baru
mahasiswa["alamat"] = "Majene"
print("Setelah menambah alamat:", mahasiswa)

# Mengubah nilai berdasarkan key
mahasiswa["umur"] = 21
print("Setelah mengubah umur:", mahasiswa)

# Menghapus data berdasarkan key
del mahasiswa["nilai"]
print("Setelah menghapus nilai:", mahasiswa)

# Mengecek apakah key tertentu ada
if "jurusan" in mahasiswa:
    print("Key 'jurusan' ada dalam dictionary.")

# Looping menampilkan key dan value
print("\n--- Looping Dictionary ---")
for key, value in mahasiswa.items():
    print(f"{key} : {value}")
