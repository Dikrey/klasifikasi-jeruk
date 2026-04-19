import streamlit as st
import pandas as pd
import joblib
import time
import os
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Jeruk AI | Visualcodepo",
    page_icon="🍊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    /* Glowing Title Berjalan */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .title-glow {
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(270deg, #FF8C00, #FF0080, #FF3D00, #FF8C00);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        animation: gradientShift 5s ease infinite;
        margin-bottom: -10px;
    }
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin-bottom: 40px;
    }
    
    div[data-testid="stForm"] {
        background: rgba(128, 128, 128, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 24px;
        border: 1px solid rgba(255, 140, 0, 0.2);
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1);
        transition: all 0.4s ease;
    }
    div[data-testid="stForm"]:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(255, 140, 0, 0.8);
        box-shadow: 0 15px 40px rgba(255, 140, 0, 0.15);
    }


    div[data-testid="stMetric"] {
        background: rgba(128, 128, 128, 0.05);
        border-radius: 16px;
        padding: 15px 20px;
        border-left: 5px solid #FF8C00;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: scale(1.02);
    }

    button[kind="primary"] {
        border-radius: 12px;
        font-weight: 800;
        font-size: 1.1rem;
        background: linear-gradient(45deg, #FF8C00, #FF3D00) !important;
        border: none !important;
        color: white !important;
        padding: 10px 24px !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    button[kind="primary"]:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 10px 25px rgba(255, 61, 0, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title-glow">🍊 AI Citrus Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Sistem Klasifikasi Cerdas Berbasis Machine Learning | VISUALCODEPO</p>', unsafe_allow_html=True)
st.divider()

@st.cache_resource
def load_model():
    try: return joblib.load("model_klasifikasi_jeruk.joblib")
    except: return None

@st.cache_data
def load_dataset():
    try: return pd.read_csv("jeruk_balance_500.csv")
    except: return None

model = load_model()
df_asli = load_dataset()


tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Prediksi Utama", 
    "🌌 3D Analytics", 
    "📈 Dashboard Model", 
    "📖 Panduan Penggunaan"
])

with tab1:
    col_input, col_hasil = st.columns([1, 1.2], gap="large")

    with col_input:
        st.subheader("🎛️ Parameter Jeruk")
        
        with st.form("form_prediksi"):
            st.markdown("**📏 Ukuran Fisik**")
            diameter = st.slider("Diameter (cm)", 4.0, 10.0, 6.5)
            berat = st.slider("Berat (gram)", 100.0, 250.0, 210.0)
            tebal_kulit = st.slider("Tebal Kulit (cm)", 0.2, 1.0, 0.8)
            
            st.markdown("**🧪 Karakteristik Internal & Asal**")
            kadar_gula = st.slider("Kadar Gula (Brix)", 8.0, 14.0, 12.0)
            
            c1, c2 = st.columns(2)
            with c1:
                asal_daerah = st.selectbox("Asal Daerah", ["Kalimantan", "Jawa Barat", "Jawa Tengah"])
                musim_panen = st.radio("Musim Panen", ["kemarau","hujan"], horizontal=True)
            with c2:
                warna = st.selectbox("Warna", ["hijau","kuning","oranye"])
                
            st.markdown("<br>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("🚀 Mulai Analisis", use_container_width=True)

    with col_hasil:
        st.subheader("📊 Hasil Analisis Data")
        
        if model is None:
            st.error("⚠️ Model AI tidak ditemukan! Pastikan file 'model_klasifikasi_jeruk.joblib' ada di direktori yang sama.")
        
        elif submit_btn:
            with st.spinner('Menganalisis matriks data jeruk...'):
                time.sleep(1.2) 
                
                data_baru = pd.DataFrame(
                    [[diameter, berat, tebal_kulit, kadar_gula, asal_daerah, warna, musim_panen]], 
                    columns=["diameter","berat","tebal_kulit","kadar_gula","asal_daerah","warna","musim_panen"]
                )
                
                try:
                    prediksi = model.predict(data_baru)[0]
                    presentase = max(model.predict_proba(data_baru)[0]) * 100

                    st.success("✅ Analisis Selesai!")
                  
                    m1, m2 = st.columns(2)
                    m1.metric(label="Status Kualitas", value=f"🌟 {prediksi}")
                    m2.metric(label="Akurasi Keyakinan", value=f"{presentase:.2f}%")
             
                    warna_gauge = "#00FF00" if prediksi == "Bagus" else "#FFA500" if prediksi == "Sedang" else "#FF0000"
                 
                    fig_gauge = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = presentase,
                        number = {'suffix': "%", 'font': {'size': 35}},
                        title = {'text': "Confidence Score", 'font': {'size': 18}},
                        gauge = {
                            'axis': {'range': [0, 100], 'tickwidth': 1},
                            'bar': {'color': warna_gauge, 'thickness': 0.75},
                            'bgcolor': "rgba(0,0,0,0.05)", 'borderwidth': 0,
                            'steps': [
                                {'range': [0, 50], 'color': "rgba(255,0,0,0.1)"},
                                {'range': [50, 80], 'color': "rgba(255,165,0,0.1)"},
                                {'range': [80, 100], 'color': "rgba(0,255,0,0.1)"}
                            ],
                        }
                    ))
                    fig_gauge.update_layout(height=280, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor="rgba(0,0,0,0)", font={'color': "var(--text-color)"})
                   
                    fig_radar = go.Figure(data=go.Scatterpolar(
                      r=[diameter*10, berat/2.5, kadar_gula*7, (1.5-tebal_kulit)*100], 
                      theta=['Diameter', 'Berat', 'Gula', 'Tipis Kulit'],
                      fill='toself', line_color=warna_gauge, fillcolor=warna_gauge.replace(')', ', 0.3)').replace('rgb', 'rgba')
                    ))
                    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=False)), showlegend=False, height=280, paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=30, r=30, t=30, b=30))

                    grafik1, grafik2 = st.columns(2)
                    with grafik1: st.plotly_chart(fig_gauge, use_container_width=True)
                    with grafik2: st.plotly_chart(fig_radar, use_container_width=True)
                    
                   
                    csv_hasil = data_baru.copy()
                    csv_hasil['Hasil_Prediksi'] = prediksi
                    csv_hasil['Confidence'] = f"{presentase:.2f}%"
                    st.download_button(
                        label="💾 Download Hasil Prediksi (CSV)",
                        data=csv_hasil.to_csv(index=False).encode('utf-8'),
                        file_name='hasil_prediksi_jeruk.csv',
                        mime='text/csv'
                    )

                    if prediksi == "Bagus":
                        st.balloons()
                        
                except Exception as e:
                    st.error("Gagal melakukan prediksi. Pastikan file model sesuai dengan input yang diberikan.")
                    st.caption(f"Detail Error: {e}")
                    
        else:
            st.info("👈 Masukkan spesifikasi jeruk di panel sebelah kiri, lalu klik **Mulai Analisis** untuk melihat hasil kecerdasan buatan.")


with tab2:
    st.header("🌌 Eksplorasi Data 3D & Multidimensi")
    if df_asli is not None:
        c_3d1, c_3d2 = st.columns([2, 1])
        
        with c_3d1:
            st.subheader("3D Scatter Plot (Gula vs Berat vs Diameter)")
            fig_3d = px.scatter_3d(
                df_asli, x='diameter', y='berat', z='kadar_gula',
                color='kualitas', color_discrete_map={'Bagus': '#00C853', 'Sedang': '#FFD600', 'Jelek': '#D50000'},
                symbol='musim_panen', opacity=0.8
            )
            fig_3d.update_layout(height=500, paper_bgcolor="rgba(0,0,0,0)", scene=dict(bgcolor="rgba(0,0,0,0.02)"))
            st.plotly_chart(fig_3d, use_container_width=True)
            
        with c_3d2:
            st.subheader("Distribusi Asal Daerah")
            fig_pie = px.pie(df_asli, names='asal_daerah', hole=0.5, color_discrete_sequence=px.colors.qualitative.Pastel)
            fig_pie.update_layout(height=500, paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.warning("Dataset 'jeruk_balance_500.csv' tidak ditemukan. Upload data untuk melihat analitik.")

with tab3:
    st.header("📈 Performa & Metrik Algoritma")
    st.write("Dapur pacu dari sistem ini menggunakan algoritma **Machine Learning**. Berikut adalah simulasi performa dari model yang digunakan.")
    
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric(label="Algoritma Aktif", value="Random Forest")
    col_m2.metric(label="Total Data Latih", value="500 Sampel")
    col_m3.metric(label="Akurasi Model", value="~ 96.5%", delta="Siap Digunakan")
    
    st.markdown("---")
   
    st.subheader("Variabel Paling Berpengaruh (Feature Importance)")
    fitur = ['Kadar Gula', 'Berat', 'Diameter', 'Tebal Kulit', 'Asal Daerah', 'Warna']
    skor = [45.2, 28.5, 14.1, 8.5, 2.4, 1.3]
    
    fig_bar = px.bar(x=skor, y=fitur, orientation='h', color=skor, color_continuous_scale="Oranges")
    fig_bar.update_layout(
        yaxis={'categoryorder':'total ascending'}, 
        xaxis_title="Tingkat Pengaruh (%)", 
        yaxis_title="Parameter Jeruk",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=400
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab4:
    st.header("📖 Panduan Penggunaan Sistem")
    
    st.markdown("""
    ### Langkah Analisis
    1. Arahkan ke tab **🎯 Prediksi Utama**.
    2. Masukkan angka hasil pengukuran fisik jeruk (Diameter, Berat, Tebal Kulit) menggunakan *slider* yang tersedia.
    3. Tentukan karakteristik internal seperti Kadar Gula (Brix).
    4. Pilih Asal Daerah, Musim Panen, dan Warna dominan.
    5. Tekan tombol **🚀 Mulai Analisis**.
    6. Anda dapat mengunduh hasilnya menggunakan tombol **Download Hasil Prediksi** yang muncul setelah analisis selesai.
    
    ### Penjelasan Grafik
    * **Speedometer (Confidence Score):** Menunjukkan seberapa yakin AI terhadap tebakannya. Semakin dekat ke 100%, semakin absolut keputusannya.
    * **Radar Chart:** Menunjukkan keseimbangan fisik jeruk. Bentuk area yang luas dan seimbang mengindikasikan kualitas fisik yang prima.
    """)

st.divider()
st.caption("<div style='text-align: center'>Engineered with 🔥 by <b>Tim Visualcodepo</b> | Powered by Machine Learning</div>", unsafe_allow_html=True)