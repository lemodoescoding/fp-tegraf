# Longest Monotonically Increasing Subsequence

Implementasi Longest Monotonically Increasing Subsequence (aplikasi menggunakan tree)

`Penjelasan algoritma `
1. Input berupa banyaknya jumlah sequence, diikuti dengan sequence itu sendiri. 
2. Tree akan dibuat untuk memetakan semua kemungkinan increasing subsequence yang mungkin terjadi. 
3. Untuk mencari subsequence terpanjang, pencarian dilakukan menggunakan DFS yang setiap sequence yang di track akan disimpan pada sebuah array. 
4. Setelah melakukan DFS dan mendapat subsequence terpanjang, program akan melakukan print pada subsequence terpanjang yang sudah tercatat. 

`Penjelasan kode`
![img_alt](./img/1.png)


![img_alt](./img/2.png)


![img_alt](./img/3.png)


![img_alt](./img/4.png)


![img_alt](./img/5.png)



Contoh Input : 
```
n
a1, a2, a3, ..., an
```

Contoh Output : 

`Case 1`
Input 
```
5
1 2 3 4 5
```

Output : 
```
[1, 2, 3, 4, 5]
```

`Case 2
Input 
```
5
5 4 3 2 1
```

Output : 
```
[5]
```

`Case 3`
Input 
```
8
3 10 4 12 5 6 8 9
```

Output : 
```
[3, 4, 5, 6, 8, 9]
```

`Case 4`
Input 
```
9
4 1 13 7 0 2 8 11 3
```

Output : 
```
[4, 7, 8, 11]
```