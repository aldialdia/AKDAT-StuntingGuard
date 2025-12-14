import streamlit as st
import pandas as pd

def show_upload_dataset():
    # Header dengan styling
    st.markdown("""
        <div class="hero-section">
            <h1>Upload Dataset Balita</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <p style="margin: 0;">
            Silakan upload file CSV yang berisi data balita. Pastikan dataset memiliki kolom: 
            <b>Umur (bulan)</b>, <b>Jenis Kelamin</b>, <b>Tinggi Badan (cm)</b>, dan <b>Status Gizi</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Upload Area dengan styling premium
    st.markdown("""
        <p style="font-weight: 600; color: #374151; margin-bottom: 8px;">
            Pilih File Dataset
        </p>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"], label_visibility="collapsed")

    # Logika Saat File Diupload
    if uploaded_file is not None:
        try:
            # Baca file CSV
            df = pd.read_csv(uploaded_file)
            
            # Simpan ke session state (Memori Aplikasi)
            st.session_state["raw_df"] = df
            
            # Success message dengan styling
            st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
                    padding: 16px 20px;
                    border-radius: 12px;
                    border-left: 4px solid #10B981;
                    margin: 16px 0;
                ">
                    <p style="margin: 0; color: #065F46; font-weight: 600;">
                        ✓ Berhasil memuat data! Total baris: {df.shape[0]}, Total kolom: {df.shape[1]}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Tampilkan Preview Data
            st.markdown("""
                <h3 style="margin-top: 24px; margin-bottom: 16px;">Preview Data Awal</h3>
            """, unsafe_allow_html=True)
            st.dataframe(df.head(), use_container_width=True)
            
            # Info Kolom dalam expander
            with st.expander("📋 Lihat Informasi Kolom"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Tipe Data Kolom:**")
                    st.write(df.dtypes)
                with col2:
                    st.write("**Statistik Deskriptif:**")
                    st.write(df.describe())
                
            st.markdown("---")
            
            # Tombol Lanjut
            col_left, col_right = st.columns([3, 1])
            with col_right:
                if st.button("Lanjut ke Preprocessing", use_container_width=True, type="primary"):
                    st.session_state["page"] = "Preprocessing Data"
                    st.rerun()

        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")
            
    else:
        # Jika belum ada file yang diupload, cek apakah sebelumnya sudah pernah upload
        if st.session_state["raw_df"] is not None:
            st.info("📁 File sebelumnya sudah tersimpan di memori.")
            st.dataframe(st.session_state["raw_df"].head())
            
            if st.button("Lanjut ke Preprocessing", type="primary"):
                st.session_state["page"] = "Preprocessing Data"
                st.rerun()