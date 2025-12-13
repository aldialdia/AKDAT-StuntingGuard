import streamlit as st

# Import modul lokal (pastikan file-file ini ada di folder yang sama/sesuai struktur)
from style import add_custom_css
from state import init_session_state

# Import halaman-halaman dari folder screens
from screens.home import show_home
from screens.upload_dataset import show_upload_dataset
from screens.preprocessing import show_preprocessing
from screens.analysis import show_analysis
from screens.visualization import show_visualization
from screens.prediction import show_prediction
from screens.about import show_about

# ----------------------------
# 1. KONFIGURASI HALAMAN (Wajib paling atas)
# ----------------------------
st.set_page_config(
    page_title="Stunting Guard - Deteksi Dini Stunting",
    page_icon="👶",
    layout="wide"
)

# ----------------------------
# 2. INISIALISASI STATE (Agar data tidak hilang)
# ----------------------------
init_session_state()

# ----------------------------
# 3. LOAD CSS (Agar tampilan cantik)
# ----------------------------
add_custom_css()

# ----------------------------
# 4. SIDEBAR & NAVIGASI
# ----------------------------
with st.sidebar:
    # --- LOGO & JUDUL ---
    # Jika kamu punya logo.png di folder images, uncomment baris bawah:
    # st.image("images/logo.png", width=200) 
    
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #4CAF50; margin:0;">👶 Stunting Guard</h1>
            <p style="font-size: 12px; color: #666;">Sistem Deteksi Dini Stunting</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    # --- MENU PILIHAN ---
    # Kita pakai radio button yang disamarkan jadi menu navigasi
    menu_options = [
        "Home",
        "Upload Dataset",
        "Preprocessing Data",
        "Data Analysis",
        "Visualisasi Data",
        "Prediksi & Mitigasi",  # Halaman Utama (Decision Tree)
        "Tentang Kami"
    ]

    # Ambil halaman aktif saat ini dari session state
    current_page = st.session_state.get("page", "Home")

    # Logika agar radio button mengikuti posisi halaman yang sedang aktif
    # (Misal: kalau diklik "Next" di Home, sidebar otomatis pindah ke Upload)
    if current_page in menu_options:
        index_menu = menu_options.index(current_page)
    else:
        index_menu = 0

    selected_menu = st.radio(
        "Menu Navigasi",
        menu_options,
        index=index_menu,
        label_visibility="collapsed" # Sembunyikan label "Menu Navigasi" biar rapi
    )

    # --- UPDATE HALAMAN JIKA KLIK MENU ---
    if selected_menu != current_page:
        st.session_state["page"] = selected_menu
        st.rerun() # Refresh halaman segera

    # --- INFO TAMBAHAN DI BAWAH ---
    st.markdown("---")
    st.caption("© 2025 Tugas Besar Akuisisi Data")
    st.caption("Kelompok Stunting Guard")

# ----------------------------
# 5. PAGE ROUTER (Pengarah Halaman)
# ----------------------------
# Kode ini yang menentukan fungsi mana yang dipanggil berdasarkan menu

page = st.session_state["page"]

if page == "Home":
    show_home()

elif page == "Upload Dataset":
    show_upload_dataset()

elif page == "Preprocessing Data":
    show_preprocessing()

elif page == "Data Analysis":
    show_analysis()

elif page == "Visualisasi Data":
    show_visualization()

elif page == "Prediksi & Mitigasi":
    show_prediction()

elif page == "Tentang Kami":
    show_about()

else:
    show_home()