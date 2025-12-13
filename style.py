import streamlit as st

def add_custom_css():
    st.markdown("""
        <style>
        /* 1. SETTING FONT UTAMA */
        html, body, [class*="css"] {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* 2. JUDUL (H1) */
        /* Warna Hijau Cerah yang terbaca jelas di Hitam maupun Putih */
        h1 {
            color: #4CAF50 !important; 
            font-weight: 700;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        
        /* 3. WARNA TEKS PARAGRAF UMUM */
        /* Kita biarkan adaptif (Putih di Dark Mode, Hitam di Light Mode) */
        p, li, span {
            /* color: inherit; */
        }

        /* 4. KOTAK INFORMASI (INFO BOX) - KUNCI TAMPILAN CERAH */
        /* Kita PAKSA kotak ini tetap Terang (Hijau Muda) meski di Dark Mode */
        .info-box {
            padding: 20px;
            background-color: #E8F5E9 !important; /* Background Hijau Muda Cerah */
            color: #1B5E20 !important;             /* Teks Hijau Tua (Biar terbaca di background terang) */
            border-left: 5px solid #4CAF50;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Tips Tambahan: Agar teks di dalam info-box tidak berubah jadi putih saat dark mode */
        .info-box p, .info-box li, .info-box span, .info-box h1, .info-box h2, .info-box h3 {
             color: #1B5E20 !important;
        }

        /* 5. TOMBOL UTAMA (Tetap Hijau Segar) */
        div.stButton > button:first-child {
            background-color: #4CAF50; 
            color: white !important;
            border-radius: 8px;
            border: none;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        div.stButton > button:first-child:hover {
            background-color: #388E3C;
            transform: translateY(-2px);
        }

        /* 6. INPUT FIELD (Kotak Isian) */
        /* Beri border hijau agar terlihat jelas batasnya di mode gelap */
        div[data-baseweb="input"], div[data-baseweb="select"] {
            border: 1px solid #4CAF50;
            border-radius: 8px;
        }
        
        /* 7. TABEL DATAFRAME */
        div[data-testid="stDataFrame"] {
            border: 1px solid #4CAF50;
            border-radius: 5px;
            overflow: hidden;
        }
        </style>
    """, unsafe_allow_html=True)