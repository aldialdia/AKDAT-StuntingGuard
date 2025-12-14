import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_visualization():
    # Header
    st.markdown("""
        <div class="hero-section">
            <h1>Visualisasi Data Balita</h1>
        </div>
    """, unsafe_allow_html=True)

    # 1. CEK DATA
    if st.session_state.get("clean_df") is None:
        st.warning("⚠️ Data belum tersedia. Silakan lakukan preprocessing terlebih dahulu.")
        if st.button("← Kembali ke Preprocessing Data"):
            st.session_state["page"] = "Preprocessing Data"
            st.rerun()
        return
    
    df = st.session_state["clean_df"]
    
    # Info Box
    st.markdown("""
    <div class='info-box'>
        <p style="margin: 0;">
            Halaman ini menampilkan statistik deskriptif dari data yang telah diupload.
            Grafik di bawah membantu kita memahami pola sebaran status gizi balita.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- ROW 1: Pie Chart Status Gizi & Bar Chart Gender ---
    st.markdown("""
        <h3 style="margin: 24px 0 20px 0;">1. Komposisi Data</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style="
                background: white;
                padding: 20px;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                border: 1px solid rgba(0, 0, 0, 0.05);
            ">
                <p style="font-weight: 600; color: #374151; margin: 0 0 16px 0;">Persentase Status Gizi</p>
        """, unsafe_allow_html=True)
        
        status_counts = df["Status Gizi"].value_counts()
        
        fig1, ax1 = plt.subplots(figsize=(6, 5))
        colors = ['#10B981', '#F59E0B', '#EF4444', '#3B82F6']
        ax1.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, 
                colors=colors[:len(status_counts)], 
                wedgeprops=dict(width=0.7, edgecolor='white'))
        ax1.axis('equal')
        st.pyplot(fig1)
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.caption("Grafik ini menunjukkan seberapa banyak kasus stunting dibandingkan normal.")

    with col2:
        st.markdown("""
            <div style="
                background: white;
                padding: 20px;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                border: 1px solid rgba(0, 0, 0, 0.05);
            ">
                <p style="font-weight: 600; color: #374151; margin: 0 0 16px 0;">Sebaran Jenis Kelamin</p>
        """, unsafe_allow_html=True)
        
        gender_data = df["Jenis Kelamin"].map({0: "Laki-laki", 1: "Perempuan"})
        
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        sns.countplot(x=gender_data, palette=["#3B82F6", "#EC4899"], ax=ax2)
        ax2.set_xlabel("Jenis Kelamin", fontsize=11)
        ax2.set_ylabel("Jumlah Anak", fontsize=11)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig2)
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.caption("Perbandingan jumlah data laki-laki dan perempuan.")

    st.markdown("---")

    # --- ROW 2: GRAFIK KMS ---
    st.markdown("""
        <h3 style="margin: 24px 0 16px 0;">2. Grafik Pola Pertumbuhan</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style="color: #6B7280; margin-bottom: 16px;">
            Grafik ini memetakan <b>Umur (X)</b> dan <b>Tinggi Badan (Y)</b>. Warna titik menunjukkan status gizi.
        </p>
    """, unsafe_allow_html=True)
    
    # Scatter Plot dalam card
    st.markdown("""
        <div style="
            background: white;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.05);
        ">
    """, unsafe_allow_html=True)
    
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    
    palette = {'normal': '#10B981', 'stunted': '#F59E0B', 'severely stunted': '#EF4444', 'tinggi': '#3B82F6'}
    
    sns.scatterplot(data=df, x="Umur (bulan)", y="Tinggi Badan (cm)", 
                    hue="Status Gizi", palette="deep", alpha=0.7, s=60, ax=ax3)
    
    ax3.set_title("Sebaran Tinggi Badan berdasarkan Umur", fontsize=14, fontweight='bold', pad=20)
    ax3.set_xlabel("Umur (bulan)", fontsize=11)
    ax3.set_ylabel("Tinggi Badan (cm)", fontsize=11)
    ax3.grid(True, linestyle='--', alpha=0.3)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.legend(title="Status Gizi", loc='lower right')
    plt.tight_layout()
    st.pyplot(fig3)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.info("💡 **Insight:** Titik-titik yang berada di bagian bawah grafik (rendah) cenderung menunjukkan status Stunted, sedangkan yang di atas menunjukkan Normal/Tinggi.")

    st.markdown("---")

    # --- ROW 3: BOXPLOT ---
    st.markdown("""
        <h3 style="margin: 24px 0 16px 0;">3. Analisis Sebaran Tinggi Badan</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="
            background: white;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.05);
        ">
    """, unsafe_allow_html=True)
    
    fig4, ax4 = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=df, x="Status Gizi", y="Tinggi Badan (cm)", 
                palette=["#10B981", "#3B82F6", "#F59E0B", "#EF4444"][:df["Status Gizi"].nunique()], 
                ax=ax4)
    ax4.set_title("Rentang Tinggi Badan per Kategori Status Gizi", fontsize=14, fontweight='bold', pad=20)
    ax4.set_xlabel("Status Gizi", fontsize=11)
    ax4.set_ylabel("Tinggi Badan (cm)", fontsize=11)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig4)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Tombol Navigasi
    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([3, 1])
    with col_right:
        if st.button("Lanjut ke Prediksi & Mitigasi", use_container_width=True, type="primary"):
            st.session_state["page"] = "Prediksi & Mitigasi"
            st.rerun()