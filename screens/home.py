import streamlit as st

def show_home():
    # Judul Besar dengan Animasi Masuk (Opsional, pakai emoji biar fresh)
    st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Selamat Datang di Stunting Guard 👶</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2rem; color: #555; margin-bottom: 40px;'>
        Sistem Cerdas Deteksi Dini & Mitigasi Risiko Stunting berbasis <b>Decision Tree</b>
    </p>
    """, unsafe_allow_html=True)

    # --- FITUR UTAMA DALAM KARTU ---
    col1, col2, col3 = st.columns(3)
    
    # Kartu 1: Input Data
    with col1:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">📂</span>
            <span class="feature-title">Input Fleksibel</span>
            <p class="feature-desc">
                Mendukung upload dataset massal (CSV) atau input data manual per anak dengan mudah.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Kartu 2: AI Analysis
    with col2:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🤖</span>
            <span class="feature-title">AI Cerdas</span>
            <p class="feature-desc">
                Dilengkapi algoritma <b>Decision Tree</b> yang mampu mempelajari pola gizi dengan akurasi tinggi.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Kartu 3: Mitigasi
    with col3:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🛡️</span>
            <span class="feature-title">Solusi Mitigasi</span>
            <p class="feature-desc">
                Tidak hanya mendeteksi, tapi memberikan <b>saran tindakan & gizi</b> spesifik sesuai umur anak.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- SEKSI CTA (Call to Action) ---
    st.markdown("""
    <div style='background-color: #F1F8E9; padding: 30px; border-radius: 20px; text-align: center; border: 1px dashed #4CAF50;'>
        <h3 style='color: #2E7D32 !important; margin:0;'>Siap Memantau Tumbuh Kembang Anak?</h3>
        <p style='color: #555 !important; margin-top: 10px; margin-bottom: 20px;'>
            Mulailah dengan mengupload data historis untuk melatih model kecerdasan buatan kami.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol ditaruh di luar div agar tetap berfungsi sebagai widget Streamlit
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True) # Spacer
        if st.button("🚀 Mulai Deteksi Sekarang", use_container_width=True, type="primary"):
            st.session_state["page"] = "Upload Dataset"
            st.rerun()