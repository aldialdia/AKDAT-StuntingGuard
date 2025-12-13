import streamlit as st
import pandas as pd

def show_upload_dataset():
    st.markdown("<h1 style='text-align: center;'>📂 Upload Dataset Balita</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        Silakan upload file CSV yang berisi data balita. Pastikan dataset memiliki kolom: 
        <b>Umur (bulan)</b>, <b>Jenis Kelamin</b>, <b>Tinggi Badan (cm)</b>, dan <b>Status Gizi</b>.
    </div>
    """, unsafe_allow_html=True)

    # Widget Upload File
    uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])

    # Logika Saat File Diupload
    if uploaded_file is not None:
        try:
            # Baca file CSV
            df = pd.read_csv(uploaded_file)
            
            # Simpan ke session state (Memori Aplikasi)
            st.session_state["raw_df"] = df
            
            st.success(f"✅ Berhasil memuat data! Total baris: {df.shape[0]}, Total kolom: {df.shape[1]}")
            
            # Tampilkan Preview Data (5 baris pertama)
            st.markdown("### 🔍 Preview Data Awal")
            st.dataframe(df.head(), use_container_width=True)
            
            # Info Kolom
            with st.expander("Lihat Informasi Kolom"):
                st.write(df.dtypes)
                
            st.markdown("---")
            
            # Tombol Lanjut (Hanya muncul jika file berhasil diupload)
            col_left, col_right = st.columns([3, 1])
            with col_right:
                if st.button("Lanjut ke Preprocessing 👉", use_container_width=True):
                    st.session_state["page"] = "Preprocessing Data"
                    st.rerun()

        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")
            
    else:
        # Jika belum ada file yang diupload, cek apakah sebelumnya sudah pernah upload
        if st.session_state["raw_df"] is not None:
            st.info("File sebelumnya sudah tersimpan di memori.")
            st.dataframe(st.session_state["raw_df"].head())
            
            if st.button("Lanjut ke Preprocessing 👉"):
                st.session_state["page"] = "Preprocessing Data"
                st.rerun()