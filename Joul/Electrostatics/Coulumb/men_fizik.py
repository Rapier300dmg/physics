# men_fizik.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def show_coulomb():
    st.title("⚡ Кулон заңы: Интерактивті визуализация")
    st.markdown("""
    Бұл бағдарлама **Python** тілінде жазылған. Сол жақтағы параметрлерді өзгерту арқылы 
    зарядтардың өзара әрекеттесуін бақылай аласыз.
    """)

    st.sidebar.header("Физикалық шамалар")
    q1 = st.sidebar.slider("1-заряд (q1), мкКл:", -10.0, 10.0, 5.0)
    q2 = st.sidebar.slider("2-заряд (q2), мкКл:", -10.0, 10.0, 5.0)
    r = st.sidebar.slider("Арақашықтық (r), метр:", 1.0, 20.0, 5.0)

    k = 8.99e9
    force = k * (abs(q1)*1e-6 * abs(q2)*1e-6) / (r**2)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📍 Зарядтардың кеңістіктегі орны")
        fig_positions = go.Figure()
        fig_positions.add_trace(go.Scatter(
            x=[-r/2], y=[0],
            mode="markers+text",
            marker=dict(size=abs(q1)*5+15, color="red" if q1 > 0 else "blue", line=dict(width=2, color='black')),
            text=[f"q1 = {q1}μC"], textposition="top center"
        ))
        fig_positions.add_trace(go.Scatter(
            x=[r/2], y=[0],
            mode="markers+text",
            marker=dict(size=abs(q2)*5+15, color="red" if q2 > 0 else "blue", line=dict(width=2, color='black')),
            text=[f"q2 = {q2}μC"], textposition="top center"
        ))
        fig_positions.add_shape(type="line", x0=-r/2, y0=0, x1=r/2, y1=0, line=dict(color="Gray", dash="dash"))
        fig_positions.update_layout(
            xaxis=dict(range=[-15, 15], title="Қашықтық (м)"),
            yaxis=dict(range=[-5, 5], visible=False),
            height=400, showlegend=False, template="plotly_white"
        )
        st.plotly_chart(fig_positions, use_container_width=True)

    with col2:
        st.subheader("📈 Күштің қашықтыққа тәуелділігі")
        r_range = np.linspace(1, 25, 100)
        f_range = k * (abs(q1)*1e-6 * abs(q2)*1e-6) / (r_range**2)
        fig_graph = go.Figure()
        fig_graph.add_trace(go.Scatter(x=r_range, y=f_range, line=dict(color='green', width=3)))
        fig_graph.add_trace(go.Scatter(
            x=[r], y=[force], mode="markers",
            marker=dict(color="black", size=12, symbol="circle")
        ))
        fig_graph.update_layout(
            xaxis_title="r (метр)", yaxis_title="Күш F (Ньютон)",
            height=400, template="plotly_white"
        )
        st.plotly_chart(fig_graph, use_container_width=True)

    st.info(f"💡 Есептелген өзара әрекеттесу күші: **{force:.4f} Ньютон**")
