# Profil
- Nama: Veronica Ivana Dewani
- NIM: 26/583110/PT/11281

# Deskripsi Program
Program Python interaktif untuk mencari end-effector di ujung tibia berbasis FK. Pada program ini, saya mengimplementasikan sistem 3-DoF yang terdiri dari Coxa, Femur, dan Tibia. 

Berdasarkan aturan penugasan studi kasus, panjang Coxa, Femur, dan Tibia ditetapkan sebagai berikut:
- Panjang Coxa: 5 cm (asumsi)
- Panjang Femur: 10 cm (2 digit terakhir NIU)
- Panjang Tibia: 81 cm (2 digit terakhir NIF)

Program akan meminta pengguna memasukkan sudut rotasi (dalam derajat) untuk ketiga servo. Sudut CW bernilai negatif, sedangkan CCW bernilai positif. Program kemudian mengonversi sudut ke radian dan menggunakan fungsi trigonometri (`math.sin` dan `math.cos`) untuk menjumlahkan posisi akhir secara kumulatif.

# Tabel Fitur
| Status | Fitur
| :---: | :--- 
| ✅ | Tugas Wajib
| ✅ | Nilai Tambah (2-6)


# Cara Penggunaan (How to Run)
Untuk menjalankan program ini secara lokal, pastikan Python 3 sudah terinstal. Program ini membutuhkan library seperti NumPy dan Matplotlib.

1. Buka terminal atau command prompt.
2. Jika belum terinstal, jalankan perintah ini untuk menginstal library yang dibutuhkan:
   ```bash
   pip install numpy matplotlib