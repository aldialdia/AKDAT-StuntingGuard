import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
from helpers import save_model_to_file

def show_analysis():
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🤖 Analisis & Training Model</h1>", unsafe_allow_html=True)

    # 1. CEK DATA BERSIH
    if st.session_state.get("clean_df") is None:
        st.warning("⚠️ Data belum diproses. Silakan ke menu 'Preprocessing Data' dulu.")
        return
    
    df = st.session_state["clean_df"]
    info = st.session_state.get("preprocess_info", {})
    
    # --- BAGIAN 1: KONFIGURASI (Selalu Muncul) ---
    st.markdown("""
    <div class='info-box'>
        Di sini kita akan melatih algoritma <b>Decision Tree</b>. 
        Tentukan kolom mana yang jadi Target (Status Gizi) dan mana yang jadi Fitur (Umur, TB, JK).
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Pilih Kolom Target
        encoded_cols = [c for c in df.columns if "_Encoded" in c]
        if encoded_cols:
            # Gunakan key agar pilihan tidak reset saat refresh
            target_col = st.selectbox("Pilih Target (Y)", encoded_cols, index=0, key="target_select")
        else:
            st.error("Tidak ditemukan kolom Target yang sudah di-encode.")
            return

    with col2:
        # Pilih Fitur (X)
        feature_cols = [c for c in df.columns if c != target_col and "_Encoded" not in c and c != "Status Gizi"]
        selected_features = st.multiselect("Pilih Fitur (X)", feature_cols, default=feature_cols, key="feat_select")

    st.markdown("---")
    
    # Hyperparameters
    with st.expander("⚙️ Pengaturan Lanjutan (Hyperparameters)"):
        c1, c2 = st.columns(2)
        with c1:
            test_size = st.slider("Ukuran Data Test (%)", 10, 50, 20, key="test_size") / 100
        with c2:
            max_depth = st.slider("Kedalaman Pohon (Max Depth)", 1, 20, 5, key="max_depth")

    # --- BAGIAN 2: TOMBOL TRAINING ---
    # Logika: Jika tombol ditekan, Latih model DAN simpan hasilnya ke Session State
    if st.button("🚀 Mulai Latih Model", type="primary", use_container_width=True):
        
        if not selected_features:
            st.error("Mohon pilih minimal 1 fitur.")
            return

        with st.spinner("Sedang melatih Decision Tree..."):
            try:
                # Split Data
                X = df[selected_features]
                y = df[target_col]
                
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
                
                # Inisialisasi & Latih Model
                model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
                model.fit(X_train, y_train)
                
                # Prediksi untuk Evaluasi
                y_pred = model.predict(X_test)
                acc = accuracy_score(y_test, y_pred)
                
                # SIMPAN KE SESSION STATE (Supaya awet saat refresh)
                st.session_state["model"] = model
                st.session_state["features"] = selected_features
                st.session_state["acc"] = acc
                st.session_state["y_test"] = y_test
                st.session_state["y_pred"] = y_pred
                
                st.success("✅ Model Berhasil Dilatih!")
                # Kita biarkan script lanjut ke bawah untuk menampilkan hasil
                
            except Exception as e:
                st.error(f"Terjadi error saat training: {e}")

    # --- BAGIAN 3: TAMPILKAN HASIL (DI LUAR BLOK TOMBOL) ---
    # Cek: Apakah di memori sudah ada model? Jika ada, tampilkan hasilnya.
    # Ini kuncinya: Meskipun halaman refresh karena tombol download, blok ini tetap jalan
    # karena "model" masih tersimpan di session_state.
    
    if st.session_state.get("model") is not None:
        
        # Ambil data dari memory
        model = st.session_state["model"]
        acc = st.session_state["acc"]
        y_test = st.session_state["y_test"]
        y_pred = st.session_state["y_pred"]
        feats = st.session_state["features"]

        st.markdown("---")
        st.subheader("📊 Hasil Analisis")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.metric("Akurasi Model", f"{acc*100:.2f}%")
            st.caption("Seberapa tepat model menebak status gizi data uji.")
        
        with col_res2:
            st.write("**Confusion Matrix:**")
            cm = confusion_matrix(y_test, y_pred)
            
            # Label Mapping
            labels = None
            if 'target_mapping' in info:
                mapping = info['target_mapping']
                labels = [mapping[i] for i in range(len(mapping))]
            
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', 
                        xticklabels=labels if labels else "auto", 
                        yticklabels=labels if labels else "auto", ax=ax)
            st.pyplot(fig)

        # Visualisasi Pohon
        st.markdown("### 🌳 Visualisasi Pohon Keputusan")
        fig_tree, ax_tree = plt.subplots(figsize=(20, 8))
        plot_tree(model, feature_names=feats, 
                  class_names=labels if labels else None,
                  filled=True, rounded=True, fontsize=10, ax=ax_tree)
        st.pyplot(fig_tree)

        st.markdown("---")
        
        # --- BAGIAN 4: DOWNLOAD & NEXT ---
        col_dl, col_next = st.columns([1, 1])
        
        with col_dl:
            # Generate file pickle
            pkl_file = save_model_to_file(model, feats)
            
            # Tombol Download
            # Walaupun tombol ini bikin refresh, karena hasil ada di session_state,
            # tampilan tidak akan hilang.
            st.download_button(
                label="💾 Download Model (.pkl)",
                data=pkl_file,
                file_name="stunting_model.pkl",
                mime="application/octet-stream",
                use_container_width=True
            )

        with col_next:
            # Tombol Next
            if st.button("Lanjut ke Visualisasi Data 👉", use_container_width=True):
                st.session_state["page"] = "Visualisasi Data"
                st.rerun()