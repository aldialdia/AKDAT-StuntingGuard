import streamlit as st
import pandas as pd
import numpy as np

def show_prediction():
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🔍 Prediksi & Mitigasi Stunting</h1>", unsafe_allow_html=True)

    # 1. CEK MODEL SUDAH ADA BELUM
    model = st.session_state.get("model")
    
    if model is None:
        st.warning("⚠️ Model AI belum dilatih. Silakan pergi ke menu 'Data Analysis' dan klik 'Mulai Latih Model' dulu.")
        if st.button("← Ke Data Analysis"):
            st.session_state["page"] = "Data Analysis"
            st.rerun()
        return

    # Keterangan
    st.markdown("""
    <div class='info-box'>
        Masukkan data balita di bawah ini. Sistem akan memprediksi status gizi dan 
        memberikan <b>Rekomendasi Mitigasi</b> jika terdeteksi risiko.
    </div>
    """, unsafe_allow_html=True)

    # 2. FORM INPUT DATA (User Friendly)
    with st.form("prediksi_form"):
        st.subheader("Data Balita")
        col1, col2 = st.columns(2)
        
        with col1:
            umur = st.number_input("Umur (bulan)", min_value=0, max_value=60, value=12, help="Usia anak dalam bulan (0-60).")
            jk_input = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        
        with col2:
            tb = st.number_input("Tinggi Badan (cm)", min_value=30.0, max_value=120.0, value=75.0, step=0.1)

        # Tombol Submit Besar
        submitted = st.form_submit_button("🔍 Cek Status Gizi Sekarang", type="primary", use_container_width=True)

    # 3. LOGIKA PREDIKSI (Hanya jalan kalau tombol ditekan)
    if submitted:
        # a. Persiapkan Data Input agar sesuai format Training
        # Ingat! Di helpers.py: Laki-laki=0, Perempuan=1
        jk_encoded = 0 if jk_input == "Laki-laki" else 1
        
        # Buat DataFrame Input (Nama kolom HARUS SAMA PERSIS dengan dataset asli)
        input_data = pd.DataFrame([[umur, jk_encoded, tb]], 
                                columns=["Umur (bulan)", "Jenis Kelamin", "Tinggi Badan (cm)"])
        
        # b. Lakukan Prediksi
        try:
            # Prediksi Kelas (0, 1, 2, dst)
            pred_index = model.predict(input_data)[0]
            
            # Prediksi Probabilitas (Seberapa yakin modelnya?)
            pred_proba = model.predict_proba(input_data)
            confidence = np.max(pred_proba) * 100  # Ambil skor tertinggi
            
            # c. Terjemahkan Kode Angka kembali ke Teks (Normal/Stunted)
            # Ambil mapping dari session state
            mapping = st.session_state.get("preprocess_info", {}).get("target_mapping", {})
            
            # Hasil Teks Akhir
            hasil_status = mapping.get(pred_index, "Tidak Diketahui").lower()
            
            st.markdown("---")
            st.subheader("📋 Hasil Analisis AI")
            
            # --- TAMBAHAN KALIMAT RANGKUMAN (SESUAI REQUEST) ---
            st.info(f"ℹ️ Hasil Analisis AI menunjukkan, bayi berkelamin **{jk_input}** dengan usia **{umur}** bulan dan tinggi badan **{tb}** cm masuk dalam kategori:")

            # 4. TAMPILAN HASIL (Dynamic UI)
            
            # KONDISI 1: AMAN (Normal / Tinggi)
            if "normal" in hasil_status or "tinggi" in hasil_status:
                st.success(f"✅ **Status Gizi: {hasil_status.upper()}**")
                st.write(f"Model yakin **{confidence:.1f}%** dengan keputusan ini.")
                
                st.markdown("""
                <div style="background-color: #d4edda; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; color: #155724;">
                    <b>Kabar Baik!</b> Pertumbuhan anak sesuai dengan usianya.
                    <ul>
                        <li>Tetap pertahankan pemberian gizi seimbang.</li>
                        <li>Pantau terus setiap bulan di Posyandu.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            # KONDISI 2: BAHAYA (Stunted / Severely Stunted)
            elif "stunted" in hasil_status: # Menangkap 'stunted' dan 'severely stunted'
                st.error(f"⚠️ **Status Gizi: {hasil_status.upper()}**")
                st.write(f"Model memprediksi risiko ini dengan tingkat keyakinan **{confidence:.1f}%**.")
                
                # --- FITUR MITIGASI (Saran Tindakan) ---
                st.markdown("### 🛡️ Rencana Mitigasi (Saran Tindakan)")
                
                mitigasi_text = ""
                
                # Logika Mitigasi Berdasarkan Umur (Personalized Advice)
                if umur < 6:
                    mitigasi_text = """
                    1. **Fokus ASI Eksklusif:** Jangan berikan makanan tambahan apapun.
                    2. **Cek Perlekatan:** Konsultasikan ke konselor laktasi jika bayi sulit menyusu.
                    3. **Ibu Menyusui:** Ibu wajib makan protein tinggi (telur, ikan, daging).
                    """
                elif 6 <= umur <= 23:
                    mitigasi_text = """
                    1. **Protein Hewani Wajib:** Setiap kali makan harus ada telur/ikan/ayam.
                    2. **Cek Porsi:** Pastikan porsi MPASI ditingkatkan sesuai umur.
                    3. **Lemak Tambahan:** Tambahkan minyak kelapa/santan/margarin pada MPASI.
                    """
                else: # Umur > 2 tahun
                    mitigasi_text = """
                    1. **Kejar Tumbuh (Catch-up):** Anak butuh kalori ekstra padat gizi.
                    2. **Susu Tambahan:** Konsultasikan ke dokter untuk susu tinggi kalori (PKMK) jika perlu.
                    3. **Stimulasi Hormon:** Pastikan anak tidur sebelum jam 9 malam (Hormon pertumbuhan bekerja saat tidur).
                    """

                st.warning(f"**Saran Khusus untuk Usia {umur} Bulan:**\n{mitigasi_text}")
                
                st.info("ℹ️ **Rujukan:** Segera bawa buku KIA dan anak ke Puskesmas terdekat untuk pengukuran ulang dan validasi tenaga medis.")

            # 5. TRANSPARANSI DATA (Opsional)
            with st.expander("🔍 Lihat Detail Probabilitas Algoritma"):
                st.write("Skor kemungkinan untuk setiap kategori:")
                
                # Menggunakan mapping yang benar untuk label kolom
                if mapping:
                    labels = [mapping[i] for i in range(len(mapping))]
                    probs_df = pd.DataFrame(pred_proba, columns=labels)
                    st.bar_chart(probs_df.T)
                else:
                    st.write("Mapping label tidak ditemukan.")

        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {e}")
            st.info("Tips: Pastikan model sudah dilatih dengan data yang benar di menu 'Data Analysis'.")