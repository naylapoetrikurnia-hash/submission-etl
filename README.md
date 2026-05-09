# Fashion Studio ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge)

---

## 📌 Deskripsi Project

Project ini merupakan implementasi **ETL Pipeline (Extract, Transform, Load)** menggunakan Python untuk mengambil data produk fashion dari website **Fashion Studio Dicoding** melalui proses web scraping.

Data yang berhasil diambil kemudian dibersihkan dan ditransformasikan sebelum disimpan ke dalam file CSV agar siap digunakan untuk proses analisis data lebih lanjut.

---

## 🎯 Tujuan Project

- Mengambil data produk fashion dari website
- Membersihkan data hasil scraping
- Melakukan transformasi data
- Menyimpan data bersih ke dalam format CSV
- Menerapkan konsep ETL modular menggunakan Python

---

## 🛠️ Teknologi yang Digunakan

- Python
- Requests
- BeautifulSoup4
- Pandas

---

## 📁 Struktur Project

```bash
submission-etl/
│
├── extract.py
├── transform.py
├── load.py
├── main.py
├── products.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 ETL Process

### 1️⃣ Extract
Proses pengambilan data produk fashion dari website menggunakan:
- `requests`
- `BeautifulSoup`

Data diambil dari:
- 50 halaman website
- title produk
- price
- rating
- colors
- size
- gender

---

### 2️⃣ Transform
Tahap transformasi dan pembersihan data meliputi:
- Menghapus simbol dollar (`$`)
- Konversi harga USD ke Rupiah
- Mengubah rating menjadi tipe float
- Mengubah colors menjadi integer
- Menghapus missing values
- Menghapus duplicate data
- Menghapus invalid product

---

### 3️⃣ Load
Data hasil transformasi disimpan ke dalam file:

```bash
products.csv
```

---

## 🚀 Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/naylapoetrikurnia-hash/submission-etl.git
```

### 2. Masuk ke Folder Project

```bash
cd submission-etl
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan ETL Pipeline

```bash
python main.py
```

---

## 📊 Output

Output project berupa file:

```bash
products.csv
```

yang berisi data produk fashion hasil scraping dan cleaning.

---

## 📚 Referensi

- Dicoding Academy
- Pandas Documentation
- BeautifulSoup Documentation
- Requests Documentation

---

## 👤 Author

**Nayla Poetri Kurnia**