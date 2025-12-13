import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_visualization():
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>📊 Visualisasi Data Balita</h1>", unsafe_allow_html=True)

    # 1. CEK DATA
    if st.session_state.get("clean_df") is None:
        st.warning("⚠️ Data belum tersedia. Silakan lakukan preprocessing terlebih dahulu.")
        return
    
    df = st.session_state["clean_df"]
    
    # Keterangan Halaman
    st.markdown("""
    <div class='info-box'>
        Halaman ini menampilkan statistik deskriptif dari data yang telah diupload.
        Grafik di bawah membantu kita memahami pola sebaran status gizi balita.
    </div>
    """, unsafe_allow_html=True)

    # --- ROW 1: Pie Chart Status Gizi & Bar Chart Gender ---
    st.subheader("1. Komposisi Data")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Persentase Status Gizi**")
        
        # Hitung jumlah per kategori
        status_counts = df["Status Gizi"].value_counts()
        
        # Buat Pie Chart
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        ax1.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, 
                colors=sns.color_palette("pastel"))
        ax1.axis('equal')  # Agar lingkaran sempurna
        st.pyplot(fig1)
        
        st.caption("Grafik ini menunjukkan seberapa banyak kasus stunting dibandingkan normal.")

    with col2:
        st.write("**Sebaran Jenis Kelamin**")
        
        # Mapping angka 0/1 kembali ke teks biar grafik bagus
        # (Asumsi di preprocessing: 0=Laki-laki, 1=Perempuan)
        gender_data = df["Jenis Kelamin"].map({0: "Laki-laki", 1: "Perempuan"})
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.countplot(x=gender_data, palette="Set2", ax=ax2)
        ax2.set_xlabel("Jenis Kelamin")
        ax2.set_ylabel("Jumlah Anak")
        st.pyplot(fig2)
        
        st.caption("Perbandingan jumlah data laki-laki dan perempuan.")

    st.markdown("---")

    # --- ROW 2: GRAFIK KMS (Umur vs Tinggi Badan) ---
    st.subheader("2. Grafik Pola Pertumbuhan (Mirip KMS)")
    st.write("Grafik ini memetakan **Umur (X)** dan **Tinggi Badan (Y)**. Warna titik menunjukkan status gizi.")
    
    # Scatter Plot
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    
    # Kita pakai scatterplot seaborn dengan 'hue' status gizi
    sns.scatterplot(data=df, x="Umur (bulan)", y="Tinggi Badan (cm)", 
                    hue="Status Gizi", palette="deep", alpha=0.6, ax=ax3)
    
    ax3.set_title("Sebaran Tinggi Badan berdasarkan Umur")
    ax3.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig3)
    
    st.info("💡 **Insight:** Titik-titik yang berada di bagian bawah grafik (rendah) cenderung berwarna merah/kuning (Stunted), sedangkan yang di atas berwarna hijau/biru (Normal/Tinggi).")

    st.markdown("---")

    # --- ROW 3: BOXPLOT (Analisis Statistik) ---
    st.subheader("3. Analisis Sebaran Tinggi Badan")
    
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x="Status Gizi", y="Tinggi Badan (cm)", palette="Set3", ax=ax4)
    ax4.set_title("Rentang Tinggi Badan per Kategori Status Gizi")
    st.pyplot(fig4)
    
    # Tombol Navigasi
    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([3, 1])
    with col_right:
        if st.button("Lanjut ke Prediksi & Mitigasi 👉", use_container_width=True):
            st.session_state["page"] = "Prediksi & Mitigasi"
            st.rerun()