# Machine Learning Analysis - Klasifikasi Kualitas Jeruk Sederhana

Sistem cerdas berbasis Machine Learning untuk mendeteksi dan memprediksi kualitas buah jeruk (Bagus, Sedang, Jelek) berdasarkan fitur fisik dan kandungan internalnya.

## Daftar Isi

  - [Tentang Proyek](https://www.google.com/search?q=%23tentang-proyek)
  - [Apa itu Machine Learning?](https://www.google.com/search?q=%23apa-itu-machine-learning)
  - [Proses Pelatihan Model](https://www.google.com/search?q=%23proses-pelatihan-model)
  - [Teknologi dan Library](https://www.google.com/search?q=%23teknologi-dan-library)
  - [Instalasi](https://www.google.com/search?q=%23instalasi)
  - [Cara Penggunaan](https://www.google.com/search?q=%23cara-penggunaan)

## Tentang Proyek

Proyek ini dikembangkan oleh **Tim Visualcodepo** untuk memberikan solusi otomatis dalam industri pertanian dan perdagangan buah. Menggunakan algoritma klasifikasi, sistem ini mampu memberikan penilaian objektif terhadap kualitas jeruk hanya dengan memasukkan beberapa parameter seperti diameter, berat, dan kadar gula.

## Apa itu Machine Learning?

Machine Learning (ML) adalah cabang dari kecerdasan buatan (AI) yang berfokus pada pengembangan sistem yang mampu belajar dari data untuk meningkatkan akurasinya tanpa diprogram secara eksplisit untuk setiap tugas.

Dalam proyek ini, Machine Learning digunakan untuk menemukan pola tersembunyi dari 500 data jeruk. Sistem "mempelajari" hubungan antara ciri-ciri fisik (misalnya: kadar gula yang tinggi biasanya berkorelasi dengan kualitas 'Bagus') dan menyimpan pengetahuan tersebut ke dalam sebuah model matematika (file `.joblib`).

## Proses Pelatihan Model

Model ini dilatih melalui beberapa tahapan standar dalam Data Science:

1.  **Eksplorasi Data (EDA):** Menganalisis sebaran data jeruk untuk memahami karakteristik setiap kelas kualitas.
2.  **Preprocessing:** Mengubah data kategori (seperti Asal Daerah dan Warna) menjadi format angka menggunakan teknik *One-Hot Encoding* agar dapat dipahami oleh algoritma.
3.  **Data Splitting:** Membagi data menjadi 80% untuk pelatihan (Training Set) dan 20% untuk pengujian (Testing Set).
4.  **Pemilihan Algoritma:** Menggunakan **Random Forest Classifier**. Algoritma ini bekerja dengan membuat banyak "pohon keputusan" dan mengambil keputusan mayoritas untuk menentukan hasil akhir, menjadikannya sangat akurat dan stabil.
5.  **Evaluasi:** Menguji model dengan data yang belum pernah dilihat sebelumnya untuk memastikan akurasi prediksi yang tinggi (rata-rata di atas 90%).

## Teknologi dan Library

Proyek ini dibangun menggunakan ekosistem Python dengan modul-modul berikut:

  - **Pandas:** Digunakan untuk manipulasi dan analisis struktur data tabel.
  - **Scikit-Learn:** Library utama untuk implementasi algoritma Machine Learning (Random Forest) dan evaluasi model.
  - **Streamlit:** Framework utama untuk membangun antarmuka (UI) dashboard web yang interaktif.
  - **Plotly:** Digunakan untuk membuat visualisasi grafik modern seperti Gauge Chart dan 3D Scatter Plot.
  - **Joblib:** Digunakan untuk menyimpan dan memuat kembali model AI yang sudah terlatih.

## Instalasi

Untuk menjalankan proyek ini di perangkat lokal, pastikan Anda telah menginstal Python, lalu ikuti langkah berikut:

1.  Clone repositori ini:
    ```bash
    git clone https://github.com/Dikrey/klasifikasi-jeruk.git
    ```
2.  Masuk ke direktori proyek:
    ```bash
    cd klasifikasi-jeruk
    ```
3.  Instal library yang diperlukan:
    ```bash
    pip install streamlit pandas scikit-learn plotly joblib
    ```

## Cara Penggunaan

1.  Jalankan aplikasi Streamlit:
    ```bash
    streamlit run app.py
    ```
2.  Buka URL yang muncul di terminal (biasanya `http://localhost:8501`).
3.  Masukkan parameter jeruk pada panel input.
4.  Klik tombol **Mulai Analisis** untuk melihat hasil prediksi dan tingkat keyakinan model.

-----

**Kontributor:** [Muhammad Raihan / Tim Visualcodepo](https://www.google.com/search?q=https://github.com/Dikrey)

-----

### Memahami Logika Klasifikasi AI

Agar kamu lebih memahami bagaimana model Random Forest di balik proyekmu bekerja, mari kita lihat simulasi sederhana di bawah ini. Kamu bisa mengubah parameter jeruk dan melihat bagaimana "logika" AI berubah dalam menentukan kualitas.

```json?chameleon
{"component":"LlmGeneratedComponent","props":{"height":"600px","prompt":"Buatkan simulator logika klasifikasi jeruk dalam bahasa Indonesia. \n\nObjektif: Membantu pengguna memahami bagaimana perubahan parameter fisik jeruk mempengaruhi keputusan Machine Learning.\n\nData State:\n- Diameter: 4.0 - 10.0 (default 6.5)\n- Berat: 100 - 250 (default 180)\n- Kadar Gula (Brix): 8.0 - 14.0 (default 11.0)\n- Tebal Kulit: 0.2 - 1.0 (default 0.5)\n\nStrategi: Standard Layout.\n\nInteraksi:\n1. Tampilkan slider untuk keempat parameter di atas.\n2. Tampilkan hasil prediksi secara real-time berdasarkan logika sederhana: \n   - Jika Gula > 12 dan Diameter > 7 -> 'Bagus'\n   - Jika Gula < 9 atau Diameter < 5 -> 'Jelek'\n   - Selain itu -> 'Sedang'.\n3. Tampilkan grafik radar sederhana yang berubah bentuk mengikuti nilai input.\n4. Berikan penjelasan singkat di bawah hasil mengapa AI memilih label tersebut (misal: 'Kualitas Bagus karena kadar gula tinggi').\n\nCatatan Styling: Gunakan gaya desain modern yang bersih dengan latar belakang terang. Jangan gunakan nama warna spesifik dalam instruksi.","id":"im_62c8958ae67f79ec"}}
```