import streamlit as st
import numpy as np
import plotly.graph_objects as go

def show_mend_klai():
    st.title("⚛️ Клапейрон-Менделеев заңы")
    st.markdown("""
    Идеал газ күйінің теңдеуі газдың негізгі параметрлері (қысым, көлем, температура) арасындағы байланысты көрсетеді.
    
    Формула: $$PV = \\frac{m}{M}RT$$
    """)

    # Константалар
    R = 8.31 

    st.sidebar.header("Газ параметрлері")
    gas_type = st.sidebar.selectbox("Газ түрі:", ["Оттегі (O₂)", "Сутегі (H₂)", "Гелий (He)", "Азот (N₂)"])
    molar_masses = {"Оттегі (O₂)": 0.032, "Сутегі (H₂)": 0.002, "Гелий (He)": 0.004, "Азот (N₂)": 0.028}
    M = molar_masses[gas_type]

    m = st.sidebar.number_input("Газ массасы (m), кг:", min_value=0.01, value=0.032, step=0.01)
    T_cels = st.sidebar.slider("Температура (T), °C:", -100, 500, 25)
    T_kelvin = T_cels + 273.15
    V = st.sidebar.slider("Көлем (V), м³:", 0.01, 0.5, 0.1)

    nu = m / M
    P = (nu * R * T_kelvin) / V

    col1, col2, col3 = st.columns(3)
    col1.metric("Зат мөлшері (ν)", f"{nu:.2f} моль")
    col2.metric("Температура (T)", f"{T_kelvin:.2f} К")
    col3.metric("Қысым (P)", f"{P/1000:.2f} кПа")

    # График
    v_range = np.linspace(0.01, 1.0, 100)
    p_v_relation = (nu * R * T_kelvin) / v_range 
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=v_range, y=p_v_relation / 1000, name="Изотерма", line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=[V], y=[P/1000], mode="markers", marker=dict(size=12, color="red")))
    
    fig.update_layout(xaxis_title="V (м³)", yaxis_title="P (кПа)", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)