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

        /* 4. KOTAK INFORMASI (INFO BOX) */
        /* Dipaksa Terang (Hijau Muda) meski di Dark Mode */
        .info-box {
            padding: 20px;
            background-color: #E8F5E9 !important; /* Background Hijau Muda Cerah */
            color: #1B5E20 !important;             /* Teks Hijau Tua */
            border-left: 5px solid #4CAF50;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .info-box p, .info-box li, .info-box span, .info-box h1, .info-box h2, .info-box h3 {
             color: #1B5E20 !important;
        }

        /* 5. TOMBOL UTAMA */
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

        /* 6. INPUT FIELD */
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

        /* =========================================
           8. DESAIN KARTU FITUR (FEATURE CARD) - BARU
           ========================================= */
        /* Kartu ini dipaksa berwarna Putih agar terlihat 'Cerah' & Bersih di mode apapun */
        .feature-card {
            background-color: #FFFFFF !important;
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #E0E0E0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); /* Bayangan halus */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-align: center;
            height: 100%; /* Agar tinggi kartu sama */
            margin-bottom: 10px;
        }
        
        /* Efek saat mouse diarahkan ke kartu */
        .feature-card:hover {
            transform: translateY(-5px); /* Naik sedikit */
            box-shadow: 0 8px 25px rgba(76, 175, 80, 0.2); /* Bayangan hijau */
            border-color: #4CAF50;
        }

        /* Ikon di dalam kartu */
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 15px;
            display: block;
        }

        /* Judul di dalam kartu (Hijau) */
        .feature-title {
            color: #2E7D32 !important; /* Hijau Tua */
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 10px;
            display: block;
        }

        /* Deskripsi di dalam kartu (Abu Gelap) */
        .feature-desc {
            color: #555 !important; /* Abu Gelap agar terbaca di background putih */
            font-size: 0.95rem;
            line-height: 1.5;
        }
        </style>
    """, unsafe_allow_html=True)