import streamlit as st

def init_session_state():
    """
    Inisialisasi semua variabel st.session_state yang dibutuhkan aplikasi Stunting Guard.
    Agar data tidak hilang saat pindah halaman.
    """

    # 1. Penanda Halaman Aktif
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    # 2. Tempat Simpan Data Mentah (Upload CSV)
    if "raw_df" not in st.session_state:
        st.session_state["raw_df"] = None

    # 3. Tempat Simpan Data Bersih (Setelah Preprocessing)
    if "clean_df" not in st.session_state:
        st.session_state["clean_df"] = None

    # 4. Tempat Simpan Model Decision Tree
    if "model" not in st.session_state:
        st.session_state["model"] = None

    # 5. Tempat Simpan Info Hasil Preprocessing (Mapping label, jumlah baris dihapus, dll)
    if "preprocess_info" not in st.session_state:
        st.session_state["preprocess_info"] = {}

    # 6. Daftar Fitur Default untuk Stunting Guard
    if "features" not in st.session_state:
        st.session_state["features"] = [
            "Umur (bulan)",
            "Jenis Kelamin",
            "Tinggi Badan (cm)"
        ]