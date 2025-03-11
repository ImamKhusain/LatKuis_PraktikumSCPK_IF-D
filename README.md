# LatKuis_Praktikum-SCPK-IF-D-

Untuk mendapatkan file terbaru dalam bentuk CSV dari dataset yang belum dibersihkan menjadi dataset yang telah dibersihkan, ikuti langkah-langkah berikut:

import pandas as pd

# 1️⃣ Baca dataset yang belum dibersihkan
```bash
raw_data_path = "Air_Traffic_Passenger_Statistics.csv"
data = pd.read_csv(raw_data_path)
```

# 2️⃣ Bersihkan Data (Preprocessing)
```bash
# Hapus baris dengan nilai NULL
data_cleaned = data.dropna()

# Hapus data duplikat
data_cleaned = data_cleaned.drop_duplicates()

# Konversi kolom tertentu ke tipe data yang sesuai (jika diperlukan)
if 'Operating Airline IATA Code' in data_cleaned.columns:
    data_cleaned['Operating Airline IATA Code'] = data_cleaned['Operating Airline IATA Code'].astype(str)

if 'Published Airline IATA Code' in data_cleaned.columns:
    data_cleaned['Published Airline IATA Code'] = data_cleaned['Published Airline IATA Code'].astype(str)

# Simpan dataset hasil preprocessing ke file CSV baru
cleaned_data_path = "Air_Traffic_Passenger_Statistics_Cleaned.csv"
data_cleaned.to_csv(cleaned_data_path, index=False)

print(f"✅ Dataset yang telah dibersihkan telah disimpan sebagai '{cleaned_data_path}'")
```

# 3️⃣ Jalankan Kode Ini
Simpan kode di atas ke dalam file preprocessing.py
Jalankan di terminal atau command prompt dengan perintah:
```bash
python preprocessing.py
```

Setelah selesai, file Air_Traffic_Passenger_Statistics_Cleaned.csv akan muncul di folder yang sama.
