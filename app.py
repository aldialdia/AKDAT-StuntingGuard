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
    page_icon="🛡️",
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
    # --- LOGO & JUDUL - PREMIUM STYLING ---
    st.markdown("""
        <div class="sidebar-brand">
            <h1 style="
                font-size: 1.75rem !important;
                font-weight: 800;
                background: linear-gradient(135deg, #059669 0%, #10B981 50%, #34D399 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin: 0;
                letter-spacing: -0.02em;
            ">Stunting Guard</h1>
            <p style="
                font-size: 0.85rem;
                color: #6B7280;
                margin: 8px 0 0 0;
                font-weight: 500;
            ">Sistem Deteksi Dini Stunting</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""<hr style="margin: 10px 0 20px 0; opacity: 0.3;">""", unsafe_allow_html=True)

    # --- MENU PILIHAN ---
    menu_options = [
        "Home",
        "Upload Dataset",
        "Preprocessing Data",
        "Data Analysis",
        "Visualisasi Data",
        "Prediksi & Mitigasi",
        "Tentang Kami"
    ]

    # Ambil halaman aktif saat ini dari session state
    current_page = st.session_state.get("page", "Home")

    # Logika agar radio button mengikuti posisi halaman yang sedang aktif
    if current_page in menu_options:
        index_menu = menu_options.index(current_page)
    else:
        index_menu = 0

    selected_menu = st.radio(
        "Menu Navigasi",
        menu_options,
        index=index_menu,
        label_visibility="collapsed"
    )

    # --- UPDATE HALAMAN JIKA KLIK MENU ---
    if selected_menu != current_page:
        st.session_state["page"] = selected_menu
        st.rerun()

    # --- INFO TAMBAHAN DI BAWAH ---
    st.markdown("""<hr style="margin: 20px 0; opacity: 0.3;">""", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <p style="font-size: 0.75rem; color: #9CA3AF; margin: 0;">
                © 2025 Tugas Besar Akuisisi Data
            </p>
            <p style="font-size: 0.75rem; color: #9CA3AF; margin: 4px 0 0 0; font-weight: 500;">
                Kelompok Stunting Guard
            </p>
        </div>
    """, unsafe_allow_html=True)

# ----------------------------
# 5. PAGE ROUTER (Pengarah Halaman)
# ----------------------------
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