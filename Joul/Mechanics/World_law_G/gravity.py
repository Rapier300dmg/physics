import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_gravity():
    st.title("🌌 Гравитация және Бүкіл әлемдік тартылыс заңы")

    st.markdown("""
    Формулалар:
    F = G * (m₁ m₂) / r²  
    F = mg
    """)

    # --- ПАРАМЕТРЫ ---
    st.sidebar.header("Физикалық параметрлер")

    m1 = st.sidebar.number_input("m1 (кг)", min_value=1.0, value=1e6, format="%.1e")
    m2 = st.sidebar.number_input("m2 (кг)", min_value=1.0, value=1e6, format="%.1e")
    r = st.sidebar.number_input("r (м)", min_value=0.1, value=10.0)

    m_body = st.sidebar.number_input("m (кг)", min_value=0.1, value=70.0)
    g = st.sidebar.slider("g (м/с²)", 0.0, 30.0, 9.8)

    G = 6.674e-11

    # --- РАСЧЁТ ---
    F_grav = G * (m1 * m2) / (r**2)
    F_weight = m_body * g

    r_range = np.linspace(1, 100, 200)
    F_r = G * (m1 * m2) / (r_range**2)

    m_range = np.linspace(1, 1e7, 100)
    F_m = G * (m_range * m2) / (r**2)

    g_range = np.linspace(0, 30, 100)
    F_g = m_body * g_range

    # --- ГРАФИКИ ---
    fig = make_subplots(rows=2, cols=2)

    fig.add_trace(go.Scatter(x=r_range, y=F_r), row=1, col=1)
    fig.add_trace(go.Scatter(x=m_range, y=F_m), row=1, col=2)
    fig.add_trace(go.Scatter(x=g_range, y=F_g), row=2, col=1)

    st.plotly_chart(fig, use_container_width=True)

    # --- ВИЗУАЛИЗАЦИЯ ---
    st.subheader("🎬 Тартылыс")

    size1 = np.log10(m1) * 5
    size2 = np.log10(m2) * 5

    fig_anim = go.Figure()
    fig_anim.add_trace(go.Scatter(
        x=[-r/2, r/2], y=[0, 0],
        mode="markers",
        marker=dict(size=[size1, size2])
    ))

    st.plotly_chart(fig_anim, use_container_width=True)

    # --- ИТОГ ---
    c1, c2 = st.columns(2)
    c1.metric("F_grav", f"{F_grav:.4f} Н")
    c2.metric("F_weight", f"{F_weight:.2f} Н")