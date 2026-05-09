# Fashion Studio ETL Pipeline

## Deskripsi Project

Project ini merupakan ETL Pipeline untuk mengambil data produk fashion dari website Fashion Studio menggunakan web scraping.

Data kemudian dibersihkan (transform) dan disimpan ke dalam file CSV.

---

## Teknologi yang Digunakan

- Python
- Requests
- BeautifulSoup
- Pandas

---

## Struktur Project

```bash
submission-etl/
│
├── extract.py
├── transform.py
├── load.py
├── main.py
├── products.csv
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan Project

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Jalankan ETL pipeline

```bash
python main.py
```

---

## Output

Output project berupa file:

```bash
products.csv
```

yang berisi data produk fashion hasil scraping dan cleaning.

---

## ETL Process

### Extract
Mengambil data produk dari website Fashion Studio menggunakan Requests dan BeautifulSoup.

### Transform
Membersihkan dan mengubah format data:
- Menghapus simbol dollar pada price
- Konversi USD ke Rupiah
- Mengubah rating menjadi float
- Membersihkan dirty data
- Menghapus duplicate dan null values

### Load
Menyimpan data bersih ke dalam file CSV.