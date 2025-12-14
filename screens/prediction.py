import streamlit as st
import pandas as pd
import numpy as np

def show_prediction():
    # Header
    st.markdown("""
        <div class="hero-section">
            <h1>Prediksi & Mitigasi Stunting</h1>
        </div>
    """, unsafe_allow_html=True)

    # 1. CEK MODEL SUDAH ADA BELUM
    model = st.session_state.get("model")
    
    if model is None:
        st.warning("⚠️ Model AI belum dilatih. Silakan pergi ke menu 'Data Analysis' dan klik 'Mulai Latih Model' dulu.")
        if st.button("← Ke Data Analysis"):
            st.session_state["page"] = "Data Analysis"
            st.rerun()
        return

    # Info Box
    st.markdown("""
    <div class='info-box'>
        <p style="margin: 0;">
            Masukkan data balita di bawah ini. Sistem akan memprediksi status gizi dan 
            memberikan <b>Rekomendasi Mitigasi</b> jika terdeteksi risiko.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. FORM INPUT DATA
    st.markdown("""
        <h3 style="margin: 24px 0 16px 0;">Data Balita</h3>
    """, unsafe_allow_html=True)
    
    with st.form("prediksi_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            umur = st.number_input("Umur (bulan)", min_value=0, max_value=60, value=12, help="Usia anak dalam bulan (0-60).")
            jk_input = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        
        with col2:
            tb = st.number_input("Tinggi Badan (cm)", min_value=30.0, max_value=120.0, value=75.0, step=0.1)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Cek Status Gizi Sekarang", type="primary", use_container_width=True)

    # 3. LOGIKA PREDIKSI
    if submitted:
        jk_encoded = 0 if jk_input == "Laki-laki" else 1
        
        input_data = pd.DataFrame([[umur, jk_encoded, tb]], 
                                columns=["Umur (bulan)", "Jenis Kelamin", "Tinggi Badan (cm)"])
        
        try:
            pred_index = model.predict(input_data)[0]
            pred_proba = model.predict_proba(input_data)
            confidence = np.max(pred_proba) * 100
            
            mapping = st.session_state.get("preprocess_info", {}).get("target_mapping", {})
            hasil_status = mapping.get(pred_index, "Tidak Diketahui").lower()
            
            st.markdown("---")
            st.markdown("""
                <h3 style="margin-bottom: 16px;">Hasil Analisis AI</h3>
            """, unsafe_allow_html=True)
            
            # --- RANGKUMAN ---
            st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
                    padding: 20px 24px;
                    border-radius: 12px;
                    border-left: 4px solid #3B82F6;
                    margin-bottom: 24px;
                ">
                    <p style="margin: 0; color: #1E40AF;">
                        Hasil Analisis AI menunjukkan, bayi berkelamin <b>{jk_input}</b> dengan usia <b>{umur} bulan</b> 
                        dan tinggi badan <b>{tb} cm</b> masuk dalam kategori:
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # 4. TAMPILAN HASIL
            
            # KONDISI 1: AMAN
            if "normal" in hasil_status or "tinggi" in hasil_status:
                st.markdown(f"""
                    <div class="result-success">
                        <h2 style="margin: 0 0 12px 0; color: #065F46 !important;">
                            ✓ Status Gizi: {hasil_status.upper()}
                        </h2>
                        <p style="margin: 0; color: #047857;">
                            Model yakin <b>{confidence:.1f}%</b> dengan keputusan ini.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                    <div style="
                        background: white;
                        padding: 24px;
                        border-radius: 16px;
                        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                        border: 1px solid rgba(16, 185, 129, 0.2);
                        margin-top: 20px;
                    ">
                        <h4 style="color: #047857; margin: 0 0 12px 0;">Kabar Baik!</h4>
                        <p style="color: #374151; margin: 0 0 12px 0;">Pertumbuhan anak sesuai dengan usianya.</p>
                        <ul style="color: #4B5563; margin: 0; padding-left: 20px;">
                            <li>Tetap pertahankan pemberian gizi seimbang.</li>
                            <li>Pantau terus setiap bulan di Posyandu.</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

            # KONDISI 2: BAHAYA
            elif "stunted" in hasil_status:
                st.markdown(f"""
                    <div class="result-danger">
                        <h2 style="margin: 0 0 12px 0; color: #7F1D1D !important;">
                            ⚠ Status Gizi: {hasil_status.upper()}
                        </h2>
                        <p style="margin: 0; color: #991B1B;">
                            Model memprediksi risiko ini dengan tingkat keyakinan <b>{confidence:.1f}%</b>.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                # FITUR MITIGASI
                st.markdown("""
                    <h3 style="margin: 32px 0 16px 0; color: #047857;">Rencana Mitigasi (Saran Tindakan)</h3>
                """, unsafe_allow_html=True)
                
                mitigasi_text = ""
                
                if umur < 6:
                    mitigasi_text = """
                    <ul style="color: #374151; line-height: 1.8;">
                        <li><b>Fokus ASI Eksklusif:</b> Jangan berikan makanan tambahan apapun.</li>
                        <li><b>Cek Perlekatan:</b> Konsultasikan ke konselor laktasi jika bayi sulit menyusu.</li>
                        <li><b>Ibu Menyusui:</b> Ibu wajib makan protein tinggi (telur, ikan, daging).</li>
                    </ul>
                    """
                elif 6 <= umur <= 23:
                    mitigasi_text = """
                    <ul style="color: #374151; line-height: 1.8;">
                        <li><b>Protein Hewani Wajib:</b> Setiap kali makan harus ada telur/ikan/ayam.</li>
                        <li><b>Cek Porsi:</b> Pastikan porsi MPASI ditingkatkan sesuai umur.</li>
                        <li><b>Lemak Tambahan:</b> Tambahkan minyak kelapa/santan/margarin pada MPASI.</li>
                    </ul>
                    """
                else:
                    mitigasi_text = """
                    <ul style="color: #374151; line-height: 1.8;">
                        <li><b>Kejar Tumbuh (Catch-up):</b> Anak butuh kalori ekstra padat gizi.</li>
                        <li><b>Susu Tambahan:</b> Konsultasikan ke dokter untuk susu tinggi kalori (PKMK) jika perlu.</li>
                        <li><b>Stimulasi Hormon:</b> Pastikan anak tidur sebelum jam 9 malam (Hormon pertumbuhan bekerja saat tidur).</li>
                    </ul>
                    """

                st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
                        padding: 24px;
                        border-radius: 16px;
                        border-left: 5px solid #F59E0B;
                        margin-bottom: 20px;
                    ">
                        <h4 style="color: #92400E; margin: 0 0 12px 0;">
                            Saran Khusus untuk Usia {umur} Bulan:
                        </h4>
                        {mitigasi_text}
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                    <div style="
                        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
                        padding: 20px 24px;
                        border-radius: 12px;
                        border-left: 4px solid #3B82F6;
                    ">
                        <p style="margin: 0; color: #1E40AF;">
                            <b>Rujukan:</b> Segera bawa buku KIA dan anak ke Puskesmas terdekat 
                            untuk pengukuran ulang dan validasi tenaga medis.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

            # 5. TRANSPARANSI DATA
            with st.expander("📊 Lihat Detail Probabilitas Algoritma"):
                st.write("Skor kemungkinan untuk setiap kategori:")
                
                if mapping:
                    labels = [mapping[i] for i in range(len(mapping))]
                    probs_df = pd.DataFrame(pred_proba, columns=labels)
                    st.bar_chart(probs_df.T)
                else:
                    st.write("Mapping label tidak ditemukan.")

        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {e}")
            st.info("Tips: Pastikan model sudah dilatih dengan data yang benar di menu 'Data Analysis'.")