import streamlit as st

def show_home():
    # Hero Section dengan styling premium
    st.markdown("""
        <div class="hero-section animate-fade-in">
            <h1 class="hero-title">Selamat Datang di Stunting Guard</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p class="page-subtitle">
            Sistem Cerdas Deteksi Dini & Mitigasi Risiko Stunting berbasis <b>Decision Tree</b>
        </p>
    """, unsafe_allow_html=True)

    # --- FITUR UTAMA DALAM KARTU ---
    col1, col2, col3 = st.columns(3)
    
    # Kartu 1: Input Data
    with col1:
        st.markdown("""
        <div class="feature-card animate-fade-in">
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
        <div class="feature-card animate-fade-in" style="animation-delay: 0.1s;">
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
        <div class="feature-card animate-fade-in" style="animation-delay: 0.2s;">
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
    <div class="cta-section">
        <h3 style="color: #047857 !important; margin: 0 0 12px 0; font-size: 1.5rem; font-weight: 700;">
            Siap Memantau Tumbuh Kembang Anak?
        </h3>
        <p style="color: #6B7280 !important; margin: 0 0 24px 0; font-size: 1.05rem; position: relative; z-index: 1;">
            Mulailah dengan mengupload data historis untuk melatih model kecerdasan buatan kami.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol ditaruh di luar div agar tetap berfungsi sebagai widget Streamlit
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Mulai Deteksi Sekarang", use_container_width=True, type="primary"):
            st.session_state["page"] = "Upload Dataset"
            st.rerun()