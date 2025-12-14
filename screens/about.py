import streamlit as st

def show_about():
    # Header
    st.markdown("""
        <div class="hero-section">
            <h1>Tim Pengembang</h1>
        </div>
    """, unsafe_allow_html=True)

    # Deskripsi Proyek
    st.markdown("""
    <div class='info-box' style='text-align: center;'>
        <p style="margin: 0 0 8px 0;">
            Aplikasi <b>Stunting Guard</b> ini dipersembahkan sebagai Luaran 
            <b>Tugas Besar Mata Kuliah Akuisisi Data</b>.
        </p>
        <p style="margin: 0;">
            Kami berkomitmen untuk menghadirkan solusi teknologi tepat guna 
            dalam membantu pencegahan stunting di Indonesia.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Data Anggota Kelompok
    team_members = [
        {
            "name": "Aldi",
            "nim": "2311521012",
            "role": "Hacker (Programmer)",
            "img_url": "https://ui-avatars.com/api/?name=Aldi&background=059669&color=fff&size=256&bold=true&font-size=0.4"
        },
        {
            "name": "Amanda Fitri Abdillah",
            "nim": "2311522034",
            "role": "Hacker (Programmer)",
            "img_url": "https://ui-avatars.com/api/?name=Amanda+Fitri&background=DB2777&color=fff&size=256&bold=true&font-size=0.4"
        },
        {
            "name": "Hasbi Ash Shiddiqi",
            "nim": "2311523014",
            "role": "Hacker (Programmer)",
            "img_url": "https://ui-avatars.com/api/?name=Hasbi+Ash&background=2563EB&color=fff&size=256&bold=true&font-size=0.4"
        }
    ]

    # Tampilkan Kartu Anggota
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    colors = ["#059669", "#DB2777", "#2563EB"]
    
    for i, col in enumerate(columns):
        member = team_members[i]
        color = colors[i]
        with col:
            st.markdown(f"""
            <div style="
                background: white;
                border-radius: 20px;
                padding: 32px 24px;
                text-align: center;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
                border: 1px solid rgba(0, 0, 0, 0.05);
                border-top: 5px solid {color};
                margin-bottom: 20px;
            ">
                <img src="{member['img_url']}" style="
                    border-radius: 50%; 
                    width: 100px; 
                    height: 100px; 
                    margin-bottom: 20px;
                    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                    border: 4px solid white;
                ">
                <h3 style="
                    font-family: 'Inter', sans-serif;
                    color: #1F2937; 
                    font-size: 1.1rem; 
                    font-weight: 700;
                    margin: 0 0 8px 0;
                ">{member['name']}</h3>
                <p style="
                    color: #6B7280; 
                    font-size: 0.9rem; 
                    margin: 0 0 16px 0;
                ">NIM: {member['nim']}</p>
                <span style="
                    background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
                    color: #047857; 
                    padding: 8px 20px; 
                    border-radius: 25px; 
                    font-size: 0.85rem;
                    font-weight: 600;
                    display: inline-block;
                ">{member['role']}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Footer Quote
    st.markdown("""
    <div style="
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        border-radius: 20px;
        margin-top: 20px;
    ">
        <p style="
            font-size: 1.25rem;
            font-style: italic;
            color: #065F46;
            margin: 0;
            line-height: 1.6;
        ">
            "Mencegah stunting adalah investasi terbaik untuk masa depan bangsa."
        </p>
    </div>
    """, unsafe_allow_html=True)