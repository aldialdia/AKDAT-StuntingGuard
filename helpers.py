import pandas as pd
import pickle
from io import BytesIO
from sklearn.preprocessing import LabelEncoder

# Konstanta Target (Nama kolom label di CSV)
TARGET_COL = "Status Gizi"

def preprocess_data(df):
    """
    Membersihkan dataset balita dan melakukan encoding agar bisa dibaca AI.
    """
    # 1. Siapkan Info Statistik Awal
    info = {
        "rows_before": df.shape[0],
        "cols": df.shape[1],
        "missing_total_before": df.isna().sum().sum()
    }

    # 2. Hapus Duplikat
    df_clean = df.drop_duplicates()
    info["duplicates_removed"] = info["rows_before"] - df_clean.shape[0]

    # 3. Hapus Data Kosong (Missing Values)
    df_clean = df_clean.dropna()
    
    # 4. Encoding Variabel Kategorikal (PENTING untuk Decision Tree)
    
    # a. Ubah Jenis Kelamin: laki-laki -> 0, perempuan -> 1
    # Kita pakai .lower() agar tidak sensitif huruf besar/kecil
    if 'Jenis Kelamin' in df_clean.columns:
        # Normalisasi teks dulu ke huruf kecil semua
        df_clean['Jenis Kelamin'] = df_clean['Jenis Kelamin'].astype(str).str.lower()
        
        # Mapping manual agar konsisten
        gender_map = {'laki-laki': 0, 'perempuan': 1}
        df_clean['Jenis Kelamin'] = df_clean['Jenis Kelamin'].map(gender_map)
        
        # Jika ada data aneh yang jadi NaN setelah mapping, isi dengan 0 (Laki-laki) sebagai default
        df_clean['Jenis Kelamin'] = df_clean['Jenis Kelamin'].fillna(0) 

    # b. Encoding Target (Status Gizi) menjadi angka
    # Contoh: Normal -> 0, Stunted -> 1, dst.
    if TARGET_COL in df_clean.columns:
        le = LabelEncoder()
        # Buat kolom baru dengan akhiran _Encoded
        df_clean[TARGET_COL + '_Encoded'] = le.fit_transform(df_clean[TARGET_COL])
        
        # Simpan kamus (dictionary) mappingnya, misal: {0: 'normal', 1: 'stunted'}
        # Ini penting agar nanti kita bisa menerjemahkan balik hasil prediksi angka ke teks
        mapping = dict(zip(le.transform(le.classes_), le.classes_))
        info['target_mapping'] = mapping

    # 5. Simpan Statistik Akhir
    info["rows_after"] = df_clean.shape[0]
    info["missing_total_after"] = df_clean.isna().sum().sum()
    
    return df_clean, info

def save_model_to_file(model, features):
    """
    Menyimpan model yang sudah dilatih ke dalam format file (.pkl)
    agar bisa didownload user.
    """
    output = BytesIO()
    data = {
        "model": model, 
        "features": features
    }
    pickle.dump(data, output)
    return output.getvalue()