# Praktikum TG - Kelas C - Kelompok C05

| Name | NRP |
| --- | --- |
| Ahmad Satrio Arrohman | 5025241061 |
| Ahsin Khuluqil Karim | 5025241063 |
| Liem, Alfred Haryanto | 5025241100 |

## The Knight's Tour

### `open_tour.py` (Open Knight's Tour)
Kode ini mencari solusi di mana kuda mengunjungi setiap kotak pada papan catur tepat satu kali, namun tidak harus kembali ke posisi awal di langkah terakhir.

Algoritma: Menggunakan Backtracking yang dioptimalkan dengan Warnsdorff’s Rule.

Warnsdorff’s Rule: Sebuah heuristik yang memprioritaskan gerakan ke kotak yang memiliki jumlah gerakan lanjutan paling sedikit (aksesibilitas terendah). Ini sangat mempercepat pencarian solusi dibandingkan backtracking biasa.

Fitur:
- Meminta input posisi awal (x, y).
- Jika jalan buntu, algoritma akan mundur (backtrack) dan mencoba rute lain.
- Visualisasi jalur kuda menggunakan panah merah.

### `closed_tour.py` (Closed Knight's Tour)
Kode ini mencari solusi di mana kuda mengunjungi setiap kotak tepat satu kali dan langkah terakhir harus bisa kembali ke posisi awal (membentuk siklus tertutup/loop).

Algoritma: Menggunakan pendekatan Greedy dengan Mutasi Acak (pendekatan Genetic Algorithm sederhana).

Kode ini tetap menggunakan Warnsdorff’s Rule, namun menambahkan nilai acak (random mutation) pada skor heuristiknya.

Tujuannya adalah untuk mencegah algoritma terjebak di "local optimum" (jalan buntu yang sama) dengan memberikan variasi pada keputusan langkah kuda.

Fitur:
- Meminta input posisi awal (x, y).
- Mengecek kondisi khusus di akhir, apakah langkah ke-64 bisa memukul kembali langkah ke-1?
- Visualisasi jalur dengan panah merah, ditambah panah hijau putus-putus yang menghubungkan posisi akhir kembali ke awal.

Input:
```
Baris (0-7): x
Kolom (0-7): y
```

Contoh:
```
4
5
```

Output:
![](knights_tour_open.png)
![](knights_tour_closed.png)
