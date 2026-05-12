# Sistem Pengelolaan Pesanan Sederhana

## Deskripsi Program
Program ini dibuat untuk mengelola data pesanan menggunakan konsep Object Oriented Programming (OOP) di Python.

Program memiliki dua class utama, yaitu:

### 1. Class Order
Class `Order` digunakan untuk:
- Menyimpan data pesanan seperti:
  - order_id
  - customer_name
  - order_date
  - total_amount
- Menghitung pajak pesanan tunggal sebesar 10%
- Menampilkan informasi pesanan

### 2. Class OrderProcessor
Class `OrderProcessor` digunakan untuk:
- Menyimpan banyak data pesanan ke dalam list
- Mengelola seluruh data pesanan
- Menghitung total pendapatan dari semua pesanan
- Menghitung total pajak dari seluruh pesanan

---

## Konsep Encapsulation
Program ini menggunakan konsep Encapsulation karena data dan fungsi dibungkus di dalam class.

Contohnya:
- Data pesanan disimpan di dalam class `Order`
- Fungsi seperti `calculate_tax()` dan `display_order()` hanya bekerja melalui object yang dibuat dari class tersebut

Dengan demikian, data dan proses perhitungan menjadi lebih terstruktur dan mudah dikelola.

---

## Pengujian Program
Saya memasukkan 3 data pesanan ke dalam program.

Program berhasil:
- Menghitung total pendapatan sebesar Rp 740987
- Menghitung total pajak 10% sebesar Rp 74098.7

Perhitungan dilakukan secara otomatis menggunakan fungsi pada class `OrderProcessor`.