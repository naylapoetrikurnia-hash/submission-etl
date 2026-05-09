# Fashion Studio ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

---

# 📌 Deskripsi Project

Project ini merupakan implementasi **ETL Pipeline (Extract, Transform, Load)** menggunakan Python untuk mengambil data produk fashion dari website **Fashion Studio Dicoding** melalui proses web scraping.

Data hasil scraping kemudian dibersihkan, ditransformasikan, dan disimpan ke beberapa repository data yaitu:

- CSV
- Google Sheets
- PostgreSQL

Project ini juga menerapkan:
- modular ETL architecture,
- unit testing,
- coverage testing,
- error handling,
- dan data validation.

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
- Menyimpan data hasil ETL ke beberapa repository data
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
- Gspread
- OAuth2Client
- SQLAlchemy
- PostgreSQL

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
├── google-sheets-api.json
└── .gitignore
```

---

# 🔄 ETL Process

## 1️⃣ Extract

Proses pengambilan data produk fashion dari website menggunakan:

- `requests`
- `BeautifulSoup`

Data yang diambil meliputi:

- title produk
- price produk
- rating produk
- jumlah colors
- size produk
- gender produk

Data diambil dari:

- 50 halaman website Fashion Studio Dicoding

---

## 2️⃣ Transform

Tahap transformasi dan pembersihan data meliputi:

- Menghapus simbol dollar (`$`)
- Konversi harga USD ke Rupiah
- Mengubah rating menjadi tipe float
- Mengubah colors menjadi integer
- Membersihkan data size
- Membersihkan data gender
- Menambahkan kolom timestamp
- Menghapus missing values
- Menghapus duplicate data
- Menghapus invalid product

---

## 3️⃣ Load

Data hasil transformasi disimpan ke beberapa repository data:

### 📄 CSV

File:

```bash
products.csv
```

### 📊 Google Sheets

Digunakan untuk penyimpanan data berbasis cloud spreadsheet.

### 🗄️ PostgreSQL

Menggunakan Neon PostgreSQL sebagai cloud database.

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
Project telah berhasil menjalankan unit testing dan coverage testing dengan hasil coverage sebesar 95%.
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

Output project berupa:

- File CSV (`products.csv`)
- Google Sheets
- PostgreSQL Database

yang berisi data produk fashion hasil scraping dan cleaning.

---

# 🔗 Repository Data

## Google Sheets

https://docs.google.com/spreadsheets/d/1avogYpGysORP1giZRqJVt4ujRkPFPwzEOAttRjSdBG4/edit?gid=0#gid=0

---

# 📚 Referensi

- Dicoding Academy
- Pandas Documentation
- BeautifulSoup Documentation
- Requests Documentation
- Pytest Documentation
- PostgreSQL Documentation

---

# 👤 Author

**Nayla Poetri Kurnia**  
ID Dicoding: **CDCC200D6X2356**