# Fashion Studio ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge)

---

# 📌 Deskripsi Project

Project ini merupakan implementasi **ETL Pipeline (Extract, Transform, Load)** menggunakan Python untuk mengambil data produk fashion dari website **Fashion Studio Dicoding** melalui proses *web scraping*.

Data hasil *scraping* kemudian dibersihkan, ditransformasikan, divalidasi, dan disimpan dalam format:

- CSV

Project ini juga menerapkan:

- Modular ETL architecture
- Unit testing
- Coverage testing
- Error handling
- Data validation

---

# 🌐 Sumber Data

Website sumber data *scraping*:

```text
https://fashion-studio.dicoding.dev
```

---

# 🎯 Tujuan Project

- Mengambil data produk fashion dari website
- Membersihkan data hasil *scraping*
- Melakukan transformasi data
- Melakukan validasi data
- Menyimpan data hasil ETL dalam format CSV
- Menerapkan konsep modular ETL menggunakan Python
- Menerapkan unit testing dan coverage testing
- Mengimplementasikan error handling pada proses ETL

---

# 🛠️ Teknologi yang Digunakan

- Python
- Requests
- BeautifulSoup4
- Pandas
- Pytest
- Coverage

---

# 📁 Struktur Project

```text
submission-etl/
│
├── tests/
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── utils/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── products.csv
├── requirements.txt
├── submission.txt
├── README.md
└── .gitignore
```

---

# 🔄 ETL Process

## 1️⃣ Extract

Proses pengambilan data produk fashion dari website dilakukan menggunakan:

- `requests`
- `BeautifulSoup`

Data yang diambil meliputi:

- Judul produk
- Harga produk
- Rating produk
- Jumlah pilihan warna
- Ukuran produk
- Gender produk

Data produk diambil dari 50 halaman website Fashion Studio Dicoding.

---

## 2️⃣ Transform

Tahap transformasi dan pembersihan data meliputi:

- Menghapus simbol dolar (`$`)
- Mengonversi harga dari USD ke rupiah
- Mengubah rating menjadi tipe data `float`
- Mengubah jumlah warna menjadi tipe data `integer`
- Membersihkan data ukuran
- Membersihkan data gender
- Menambahkan kolom `timestamp`
- Menghapus *missing values*
- Menghapus data duplikat
- Menghapus produk dengan data tidak valid

---

## 3️⃣ Load

Data hasil transformasi disimpan dalam format CSV.

### 📄 CSV

File hasil proses ETL:

```text
products.csv
```

Proses penyimpanan dilakukan menggunakan fungsi `to_csv()` dari Pandas:

```python
df.to_csv("products.csv", index=False)
```

Parameter `index=False` digunakan agar indeks DataFrame tidak ikut disimpan sebagai kolom tambahan.

---

# 🧪 Unit Testing

Project ini menggunakan:

- `pytest`
- `coverage`

Pengujian dilakukan untuk memastikan seluruh fungsi ETL berjalan dengan baik.

## Menjalankan Unit Test

```bash
pytest
```

## Menjalankan Coverage Test

```bash
coverage run -m pytest tests
coverage report
```

## Hasil Coverage

Project telah berhasil menjalankan unit testing dan coverage testing dengan hasil coverage sebesar **95%**.

---

# 🚀 Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone https://github.com/naylapoetrikurnia-hash/submission-etl.git
```

## 2. Masuk ke Folder Project

```bash
cd submission-etl
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Jalankan ETL Pipeline

```bash
python main.py
```

Setelah proses ETL selesai, file `products.csv` akan dibuat pada folder utama project.

---

# 📊 Output

Output project berupa file:

```text
products.csv
```

File tersebut berisi data produk fashion yang telah melalui proses:

1. Pengambilan data dari website
2. Pembersihan data
3. Transformasi data
4. Validasi data
5. Penyimpanan dalam format CSV

---

# 📚 Referensi

- Dicoding Academy
- Python Documentation
- Pandas Documentation
- BeautifulSoup Documentation
- Requests Documentation
- Pytest Documentation
- Coverage.py Documentation

---

# 👤 Author

**Nayla Poetri Kurnia**  
ID Dicoding: **CDCC200D6X2356**