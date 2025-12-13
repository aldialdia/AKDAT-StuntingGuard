import streamlit as st

def show_about():
    # Judul Halaman
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>👥 Tim Pengembang</h1>", unsafe_allow_html=True)

    # Deskripsi Proyek
    st.markdown("""
    <div class='info-box' style='text-align: center;'>
        <p>
            Aplikasi <b>Stunting Guard</b> ini dipersembahkan sebagai Luaran 
            <b>Tugas Besar Mata Kuliah Akuisisi Data</b>.
        </p>
        <p>
            Kami berkomitmen untuk menghadirkan solusi teknologi tepat guna 
            dalam membantu pencegahan stunting di Indonesia.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Data Anggota Kelompok (Sesuai Request)
    team_members = [
        {
            "name": "Aldi",
            "nim": "2311521012",
            "role": "Hacker (Programmer)",
            "img_url": "https://ui-avatars.com/api/?name=Aldi&background=4CAF50&color=fff&size=256"
        },
        {
            "name": "Amanda Fitri Abdillah",
            "nim": "2311522034",
            "role": "Hacker (Programmer)",
            "img_url": "https://ui-avatars.com/api/?name=Amanda+Fitri&background=E91E63&color=fff&size=256"
        },
        {
            "name": "Hasbi Ash Shiddiqi",
            "nim": "2311523014",
            "role": "Hacker (Programmer)",
            "img_url": "https://ui-avatars.com/api/?name=Hasbi+Ash&background=2196F3&color=fff&size=256"
        }
    ]

    # Tampilkan Kartu Anggota (3 Kolom Sejajar)
    col1, col2, col3 = st.columns(3)

    # Loop untuk menampilkan setiap anggota di kolom masing-masing
    columns = [col1, col2, col3]
    
    for i, col in enumerate(columns):
        member = team_members[i]
        with col:
            # Tampilan Kartu dengan CSS Custom
            st.markdown(f"""
            <div style="
                background-color: white; 
                border-radius: 15px; 
                padding: 20px; 
                text-align: center;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                border-top: 5px solid #2E7D32;
                margin-bottom: 20px;
            ">
                <img src="{member['img_url']}" style="border-radius: 50%; width: 100px; height: 100px; margin-bottom: 15px;">
                <h3 style="color: #333; font-size: 18px; margin: 0;">{member['name']}</h3>
                <p style="color: #666; font-size: 14px; margin: 5px 0;"><b>NIM: {member['nim']}</b></p>
                <span style="
                    background-color: #E8F5E9; 
                    color: #2E7D32; 
                    padding: 5px 10px; 
                    border-radius: 20px; 
                    font-size: 12px;
                    font-weight: bold;
                ">{member['role']}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Footer Quote
    st.markdown("""
    <div style="text-align: center; color: #888; font-style: italic;">
        "Mencegah stunting adalah investasi terbaik untuk masa depan bangsa."
    </div>
    """, unsafe_allow_html=True)