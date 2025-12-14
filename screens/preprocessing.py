import streamlit as st
import pandas as pd
from helpers import preprocess_data

def show_preprocessing():
    # Header
    st.markdown("""
        <div class="hero-section">
            <h1>Preprocessing Data</h1>
        </div>
    """, unsafe_allow_html=True)

    # 1. CEK DATA
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
        <p style="margin: 0;">
            Tahap ini akan membersihkan data dari duplikat, nilai kosong (missing values), 
            dan mengubah data teks (Laki-laki/Perempuan) menjadi angka agar bisa diproses algoritma.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. TAMPILKAN STATISTIK DATA KOTOR dengan cards premium
    st.markdown("""
        <h3 style="margin-bottom: 16px;">Statistik Data Mentah</h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{df_raw.shape[0]}</div>
                <div class="metric-label">Total Baris</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{df_raw.shape[1]}</div>
                <div class="metric-label">Total Kolom</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        missing = df_raw.isna().sum().sum()
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{missing}</div>
                <div class="metric-label">Data Kosong</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. TOMBOL EKSEKUSI PREPROCESSING
    if st.button("✨ Bersihkan & Proses Data", type="primary", use_container_width=True):
        
        with st.spinner("Sedang membersihkan data..."):
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

        st.markdown("---")
        st.markdown("""
            <h3 style="margin-bottom: 16px;">Hasil Pembersihan</h3>
        """, unsafe_allow_html=True)
        
        # Tampilkan ringkasan dalam card premium
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
            padding: 24px;
            border-radius: 16px;
            border: 1px solid rgba(16, 185, 129, 0.2);
            margin-bottom: 24px;
        ">
            <div style="display: flex; flex-wrap: wrap; gap: 24px;">
                <div style="flex: 1; min-width: 150px;">
                    <p style="color: #6B7280; font-size: 0.9rem; margin: 0;">Duplikat Dihapus</p>
                    <p style="color: #047857; font-size: 1.5rem; font-weight: 700; margin: 4px 0 0 0;">{info['duplicates_removed']} data</p>
                </div>
                <div style="flex: 1; min-width: 150px;">
                    <p style="color: #6B7280; font-size: 0.9rem; margin: 0;">Sisa Baris Data</p>
                    <p style="color: #047857; font-size: 1.5rem; font-weight: 700; margin: 4px 0 0 0;">{info['rows_after']} baris</p>
                </div>
                <div style="flex: 1; min-width: 150px;">
                    <p style="color: #6B7280; font-size: 0.9rem; margin: 0;">Status</p>
                    <p style="color: #047857; font-size: 1rem; font-weight: 600; margin: 4px 0 0 0;">✓ Siap untuk Decision Tree</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Preview Data Bersih
        st.write("**Preview Data Bersih** (Perhatikan kolom 'Jenis Kelamin' sudah jadi angka):")
        st.dataframe(df_clean.head(), use_container_width=True)

        # Tombol Lanjut ke Analisis
        st.markdown("<br>", unsafe_allow_html=True)
        col_left, col_right = st.columns([3, 1])
        with col_right:
            if st.button("Lanjut ke Analisis", use_container_width=True, type="primary"):
                st.session_state["page"] = "Data Analysis"
                st.rerun()