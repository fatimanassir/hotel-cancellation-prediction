import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1. CONFIGURACIÓN DE PÁGINA (DEBE IR AQUÍ, SOLAMENTE UNA VEZ)
st.set_page_config(page_title="Fatima´s Hotels | Revenue Management", layout="wide")

# 2. CSS PARA INTERFAZ DE HOTEL DE LUJO
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
    .stApp { background-color: #F8F9FA; }
    .header-hotel {
        background-color: #1A2634;
        padding: 20px;
        border-radius: 0px 0px 15px 15px;
        color: #D4AF37;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .header-hotel h1 {
        font-family: 'Playfair Display', serif;
        margin: 0;
        letter-spacing: 2px;
        color: #D4AF37 !important;
    }
    h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #1A2634;
        border-bottom: 1px solid #D4AF37;
        padding-bottom: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1A2634;
        color: #D4AF37;
        border: 1px solid #D4AF37;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        text-transform: uppercase;
        padding: 15px;
    }
    .stButton>button:hover {
        background-color: #D4AF37;
        color: #1A2634;
    }
    </style>
    
    <div class="header-hotel">
        <h1>FATIMA´S HOTELS</h1>
        <p style="margin:0; font-size: 0.8rem; letter-spacing: 3px;">REVENUE MANAGEMENT & PREDICTIVE ANALYTICS</p>
    </div>
    """, unsafe_allow_html=True)

# 3. CARGA DE MODELOS
@st.cache_resource
def load_assets():
    with open('modelo_final_hotel.pkl', 'rb') as f:
        modelo = pickle.load(f)
    with open('escalador_hotel.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('columnas_modelo_final_hotel.pkl', 'rb') as f:
        columnas = pickle.load(f)
    return modelo, scaler, columnas

modelo, scaler, columnas = load_assets()

# 4. CUERPO DE LA APP
st.markdown("### 📋 Gestión de Reservas")
st.write("Introduzca los datos de la reserva para evaluar el riesgo de cancelación.")

with st.form("reserva_form"):
    st.subheader("Variables Críticas")
    col1, col2 = st.columns(2)
    
    with col1:
        room_changed = st.selectbox("¿Se ha cambiado la habitación?", [0, 1], 
                                    help="Indica si la habitación asignada es diferente a la reservada.")
        parking = st.selectbox("¿Requiere plaza de parking?", [0, 1])
        customer_type = st.selectbox("Tipo de Cliente", ["Transient", "Contract", "Group", "Transient-Party"])
        deposit = st.selectbox("Tipo de Depósito", ["No Deposit", "Non Refund", "Refundable"])

    with col2:
        lead_time = st.slider("Antelación (Lead Time)", 0, 365, 30)
        special_req = st.number_input("Peticiones Especiales", 0, 5, 0)
        adr = st.number_input("Precio Medio (ADR)", 0.0, 500.0, 100.0)
        prev_cancel = st.number_input("Cancelaciones Previas", 0, 20, 0)

    submit = st.form_submit_button("Analizar Riesgo de Estancia")

# 5. LÓGICA DE PREDICCIÓN
if submit:
    input_data = {col: [0] for col in columnas}
    input_data['room_changed'] = [room_changed]
    input_data['required_car_parking_spaces'] = [parking]
    input_data['lead_time'] = [lead_time]
    input_data['adr'] = [adr]
    input_data['total_of_special_requests'] = [special_req]
    input_data['had_prev_cancellations'] = [prev_cancel]
    
    if f'customer_type_{customer_type}' in columnas:
        input_data[f'customer_type_{customer_type}'] = [1]
    if f'deposit_type_{deposit}' in columnas:
        input_data[f'deposit_type_{deposit}'] = [1]
    
    df_input = pd.DataFrame(input_data)[columnas]
    df_scaled = scaler.transform(df_input)
    prob = modelo.predict_proba(df_scaled)[0][1]
    
    st.divider()
    if prob > 0.5:
        st.error(f"### ⚠️ RIESGO ALTO: {prob*100:.2f}% de probabilidad de cancelación")
    else:
        st.success(f"### ✅ RIESGO BAJO: {prob*100:.2f}% de probabilidad de cancelación")