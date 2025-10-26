# Link Tugas: https://drive.google.com/file/u/2/d/1-hU_TucEdNJxoiGlorD0DeA8qtFa5E-r/view?usp=classroom_web

# Latihan

# 1. Buah buahan
buah = ['apel', 'mangga', 'jeruk', 'anggur', 'pisang']

# a. Tambahkan 'semangka' di akhir list, ezz pzz lemon squizy
buah.append('semangka')
print(buah) # ['apel', 'mangga', 'jeruk', 'anggur', 'pisang', 'semangka']

# b. Sisipkan 'durian' di antara 'jeruk' dan 'anggur', kira kira index ke 3, 
# rumus: .insert(index, data)
buah.insert(3, 'durian')
print(buah) # ['apel', 'mangga', 'jeruk', 'durian', 'anggur', 'pisang', 'semangka']

# c. Hapus 'mangga' dari list
buah.remove('mangga')
print(buah) # ['apel', 'jeruk', 'durian', 'anggur', 'pisang', 'semangka']

# d. Ubah 'pisang' menjadi 'nanas'
# posisi pisang sebelum semangka itu indeks -2
buah[-2] = 'nanas'  
print(buah) # ['apel', 'jeruk', 'durian', 'anggur', 'nanas', 'semangka']

# e. Tampilkan 3 buah pertama,
# Belum diajarin selain pakai index yang buah[0],,buah[1], buah[2], tapi caranya gini:
# data[start:end:step]
print(buah[:3]) # ['apel', 'jeruk', 'durian']

# 2 Mengurutkan angka
angka = [45, 12, 78, 23, 56, 89, 34]

# a. Urutkan secara ascending (kecil ke besar)
angka.sort()
print(angka) # [12, 23, 34, 45, 56, 78, 89]
# b. Urutkan secara descending (besar ke kecil)
angka.reverse()
print(angka) # [89, 78, 56, 45, 34, 23, 12]