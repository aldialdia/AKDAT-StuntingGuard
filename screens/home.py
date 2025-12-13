import streamlit as st

def show_home():
    # Judul Besar di Tengah
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>Selamat Datang di Stunting Guard 👶</h1>", unsafe_allow_html=True)
    
    # Deskripsi Aplikasi
    st.markdown("""
    <div class='info-box' style='text-align: center;'>
        <p style="font-size: 18px;">
            Sistem Deteksi Dini Risiko Stunting pada Balita menggunakan Algoritma <b>Decision Tree</b>.
        </p>
        <p>
            Aplikasi ini dirancang untuk membantu Kader Posyandu dalam memantau status gizi anak 
            dan memberikan rekomendasi mitigasi yang tepat.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Kolom untuk gambar ilustrasi (Opsional, jika tidak ada gambar akan kosong rapi)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Jika punya gambar ilustrasi, bisa ditaruh di sini
        st.markdown("---")

    # Fitur Utama
    st.subheader("🚀 Fitur Utama")
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("### 📂 Input Mudah")
        st.write("Upload data balita (CSV) atau input manual.")
    
    with col_b:
        st.markdown("### 🤖 AI Cerdas")
        st.write("Menggunakan Decision Tree untuk klasifikasi akurat.")
    
    with col_c:
        st.markdown("### 🛡️ Mitigasi")
        st.write("Saran tindakan jika terdeteksi risiko stunting.")

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Tombol Mulai Besar di Tengah
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("Mulai Deteksi Sekarang 👉", use_container_width=True):
            st.session_state["page"] = "Upload Dataset"
            st.rerun()