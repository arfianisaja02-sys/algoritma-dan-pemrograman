# ============================================================
# Program: Bubble Sort Sederhana
# Deskripsi:
#   - Mengurutkan data dengan cara membandingkan pasangan elemen
#     dan menukarnya jika urutannya salah.
#   - Proses diulang sampai tidak ada lagi pertukaran.
# ============================================================

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Jika elemen sekarang lebih besar dari sebelahnya → tukar
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# Contoh penggunaan
if __name__ == "__main__":
    angka = [64, 34, 25, 12, 22, 11, 90]
    print("Sebelum sort:", angka)
    print("Sesudah sort:", bubble_sort(angka))

# ============================================================
# Program: Selection Sort Sederhana
# Deskripsi:
#   - Mengurutkan data dengan mencari elemen terkecil kemudian
#     menukarnya dengan posisi paling depan.
#   - Lebih efisien dari Bubble Sort pada beberapa kasus.
# ============================================================

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i  # anggap elemen pertama sebagai yang paling kecil

        # Cari nilai terkecil di sisa list
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        # Tukar dengan elemen posisi 'i'
        data[i], data[min_index] = data[min_index], data[i]

    return data


# Contoh penggunaan
if __name__ == "__main__":
    angka = [64, 25, 12, 22, 11]
    print("Sebelum sort:", angka)
    print("Sesudah sort:", selection_sort(angka))


# ============================================================
# Program: Insertion Sort Sederhana
# Deskripsi:
#   - Mengurutkan data seperti cara kita menyusun kartu.
#   - Ambil satu per satu elemen lalu sisipkan ke posisi yang benar.
# ============================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Geser elemen yang lebih besar ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # Tempatkan key pada posisi yang seharusnya
        data[j + 1] = key

    return data


# Contoh penggunaan
if __name__ == "__main__":
    angka = [12, 11, 13, 5, 6]
    print("Sebelum sort:", angka)
    print("Sesudah sort:", insertion_sort(angka))

