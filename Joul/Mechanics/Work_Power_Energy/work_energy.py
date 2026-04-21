import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_work_energy():
    st.title("🎾 Энергия түрлері және тәуелділіктер")

    st.markdown("""
    Формулалар:
    A = m a v t  
    E_k = mv² / 2  
    E_p = mgh
    """)

    # --- ВВОД ---
    st.divider()
    col_inp1, col_inp2, col_inp3 = st.columns(3)

    with col_inp1:
        m = st.number_input("Масса (кг)", min_value=0.1, value=2.0)
        a = st.number_input("Үдеу (м/с²)", value=2.0)

    with col_inp2:
        v = st.number_input("Жылдамдық (м/с)", value=5.0)
        h = st.number_input("Биіктік (м)", value=10.0)

    with col_inp3:
        t = st.number_input("Уақыт (с)", value=5.0)
        g = 9.8

    # --- РАСЧЁТ ---
    E_work = m * a * v * t
    E_kin = (m * v**2) / 2
    E_pot = m * g * h

    # --- АНИМАЦИЯ ---
    st.subheader("🎬 Қозғалыс")

    fig_ball = go.Figure(
        data=[go.Scatter(
            x=[0], y=[h],
            mode="markers+text",
            marker=dict(size=30, color="red"),
            text=["Доп"]
        )],
        layout=go.Layout(
            xaxis=dict(range=[-1, 1], visible=False),
            yaxis=dict(range=[0, h + 20]),
            height=300,
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="▶ Іске қосу", method="animate")]
            )]
        ),
        frames=[
            go.Frame(data=[go.Scatter(x=[0], y=[h - (h/10)*i])])
            for i in range(11)
        ]
    )

    st.plotly_chart(fig_ball, use_container_width=True)

    # --- ГРАФИКИ ---
    st.subheader("📊 Графиктер")

    m_range = np.linspace(0.1, 20, 100)
    v_range = np.linspace(0, 30, 100)
    h_range = np.linspace(0, 50, 100)

    fig = make_subplots(rows=1, cols=3)

    fig.add_trace(go.Scatter(x=m_range, y=m_range * a * v * t), row=1, col=1)
    fig.add_trace(go.Scatter(x=v_range, y=(m * v_range**2)/2), row=1, col=2)
    fig.add_trace(go.Scatter(x=h_range, y=m * g * h_range), row=1, col=3)

    st.plotly_chart(fig, use_container_width=True)

    # --- ИТОГ ---
    c1, c2, c3 = st.columns(3)

    c1.metric("Жұмыс", f"{E_work:.1f} Дж")
    c2.metric("Кинетикалық", f"{E_kin:.1f} Дж")
    c3.metric("Потенциалдық", f"{E_pot:.1f} Дж")