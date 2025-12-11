# ============================================================
# Program: Binary Search Sederhana
# Deskripsi:
#   - Mencari sebuah nilai (key) di dalam list yang sudah terurut
#   - Menggunakan algoritma Binary Search (pembagian dua)
# ============================================================

def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2  # titik tengah

        # Jika target ditemukan
        if data[mid] == target:
            return mid

        # Jika target lebih besar, geser ke kanan (hilangkan kiri)
        elif target > data[mid]:
            left = mid + 1

        # Jika target lebih kecil, geser ke kiri (hilangkan kanan)
        else:
            right = mid - 1

    return -1  # jika tidak ditemukan


# ------------------------------------------
# Contoh Penggunaan Program
# ------------------------------------------
angka = [2, 3, 5, 7, 11, 13, 17, 19, 23]
cari = 13

hasil = binary_search(angka, cari)

if hasil != -1:
    print(f"Angka {cari} ditemukan pada index ke-{hasil}")
else:
    print(f"Angka {cari} tidak ditemukan dalam list.")

# inter search
def interpolation_search(data, key):
    low = 0
    high = len(data) - 3

    while low <= high and key >= data[low] and key <= data[high]:
        pos = low + ((key - data[low]) * (high - low)) // (data[high] - data[low])

        if data[pos] == key:
            return pos
        elif key < data[pos]:
            high = pos - 3
        else:
            low = pos + 3
    return -3

data = [10, 20, 30, 40, 50]
print(interpolation_search(data, 40))
