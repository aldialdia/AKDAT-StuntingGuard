import streamlit as st
import pandas as pd
from helpers import preprocess_data  # Kita akan panggil fungsi pembersih dari helpers.py

def show_preprocessing():
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🧹 Preprocessing Data</h1>", unsafe_allow_html=True)

    # 1. CEK DATA: Apakah user sudah upload data di halaman sebelumnya?
    if st.session_state.get("raw_df") is None:
        st.warning("⚠️ Data belum ada. Silakan upload dataset terlebih dahulu!")
        if st.button("← Kembali ke Upload Dataset"):
            st.session_state["page"] = "Upload Dataset"
            st.rerun()
        return

    # Ambil data mentah dari session state
    df_raw = st.session_state["raw_df"]
    
    st.markdown("""
    <div class='info-box'>
        Tahap ini akan membersihkan data dari duplikat, nilai kosong (missing values), 
        dan mengubah data teks (Laki-laki/Perempuan) menjadi angka agar bisa diproses algoritma.
    </div>
    """, unsafe_allow_html=True)

    # 2. TAMPILKAN STATISTIK DATA KOTOR
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Baris", df_raw.shape[0])
    col2.metric("Total Kolom", df_raw.shape[1])
    col3.metric("Data Kosong", df_raw.isna().sum().sum())

    st.markdown("---")

    # 3. TOMBOL EKSEKUSI PREPROCESSING
    # Tombol ini yang akan memicu proses pembersihan
    if st.button("✨ Bersihkan & Proses Data", type="primary", use_container_width=True):
        
        with st.spinner("Sedang membersihkan data..."):
            # Panggil fungsi 'preprocess_data' yang nanti kita buat di helpers.py
            # Fungsi ini mengembalikan 2 hal: Data Bersih (df_clean) dan Info Proses (process_info)
            clean_df, process_info = preprocess_data(df_raw)
            
            # Simpan hasil ke session state
            st.session_state["clean_df"] = clean_df
            st.session_state["preprocess_info"] = process_info
            
            st.success("✅ Preprocessing Selesai!")
            st.rerun()

    # 4. TAMPILKAN HASIL (JIKA SUDAH DIPROSES)
    if st.session_state.get("clean_df") is not None:
        info = st.session_state["preprocess_info"]
        df_clean = st.session_state["clean_df"]

        st.markdown("### 📊 Hasil Pembersihan")
        
        # Tampilkan ringkasan perubahan dalam kotak hijau
        st.markdown(f"""
        <div style="background-color: #E8F5E9; padding: 15px; border-radius: 10px; border: 1px solid #4CAF50;">
            <ul>
                <li><b>Duplikat Dihapus:</b> {info['duplicates_removed']} data</li>
                <li><b>Sisa Baris Data:</b> {info['rows_after']} baris</li>
                <li><b>Status:</b> Siap untuk analisis Decision Tree 🌳</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Preview Data Bersih
        st.write("Preview Data Bersih (Perhatikan kolom 'Jenis Kelamin' sudah jadi angka):")
        st.dataframe(df_clean.head(), use_container_width=True)

        # Tombol Lanjut ke Analisis
        st.markdown("<br>", unsafe_allow_html=True)
        col_left, col_right = st.columns([3, 1])
        with col_right:
            if st.button("Lanjut ke Analisis Decision Tree 👉", use_container_width=True):
                st.session_state["page"] = "Data Analysis"
                st.rerun()