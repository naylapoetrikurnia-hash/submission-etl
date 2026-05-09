# Fashion Studio ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge)

---

# 📌 Deskripsi Project

Project ini merupakan implementasi **ETL Pipeline (Extract, Transform, Load)** menggunakan Python untuk mengambil data produk fashion dari website **Fashion Studio Dicoding** melalui proses web scraping.

Data yang berhasil diambil kemudian dibersihkan dan ditransformasikan sebelum disimpan ke dalam file CSV agar siap digunakan untuk proses analisis data lebih lanjut.

---

# 🌐 Sumber Data

Website sumber data scraping:

```bash
https://fashion-studio.dicoding.dev
```

---

# 🎯 Tujuan Project

- Mengambil data produk fashion dari website
- Membersihkan data hasil scraping
- Melakukan transformasi data
- Menyimpan data bersih ke dalam format CSV
- Menerapkan konsep ETL modular menggunakan Python
- Menerapkan unit testing dan coverage testing

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

```bash
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

Proses pengambilan data produk fashion dari website menggunakan:

- `requests`
- `BeautifulSoup`

Data diambil dari:
- 50 halaman website
- title produk
- price produk
- rating produk
- jumlah colors
- size produk
- gender produk

---

## 2️⃣ Transform

Tahap transformasi dan pembersihan data meliputi:

- Menghapus simbol dollar (`$`)
- Konversi harga USD ke Rupiah
- Mengubah rating menjadi tipe float
- Mengubah colors menjadi integer
- Membersihkan data size
- Membersihkan data gender
- Menghapus missing values
- Menghapus duplicate data
- Menghapus invalid product

---

## 3️⃣ Load

Data hasil transformasi disimpan ke dalam file:

```bash
products.csv
```

---

# 🧪 Unit Testing

Project ini menggunakan:

- `pytest`
- `coverage`

untuk memastikan seluruh fungsi ETL berjalan dengan baik.

## Menjalankan Unit Test

```bash
pytest
```

## Menjalankan Coverage Test

```bash
coverage run -m pytest
coverage report
```

## Hasil Coverage

```bash
TOTAL 100%
```

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

---

# 📊 Output

Output project berupa file:

```bash
products.csv
```

yang berisi data produk fashion hasil scraping dan cleaning.

---

# 📚 Referensi

- Dicoding Academy
- Pandas Documentation
- BeautifulSoup Documentation
- Requests Documentation
- Pytest Documentation

---

# 👤 Author

**Nayla Poetri Kurnia**  
ID Dicoding: **CDCC200D6X2356**