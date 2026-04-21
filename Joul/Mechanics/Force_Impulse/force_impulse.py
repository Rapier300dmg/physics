import streamlit as st
import numpy as np
import plotly.graph_objects as go

def show_force_impulse():
    st.title("⚖️ Күш, Масса және Импульс")

    st.sidebar.header("Физикалық шамалар")

    mass = st.sidebar.number_input("Масса (кг)", min_value=0.1, value=2.0)
    accel = st.sidebar.number_input("Үдеу (м/с²)", value=3.0)
    vel = st.sidebar.number_input("Жылдамдық (м/с)", value=5.0)

    F = mass * accel
    P = mass * vel

    a_range = np.linspace(0, 10, 100)
    v_range = np.linspace(0, 20, 100)

    F_range = mass * a_range
    P_range = mass * v_range

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("F = ma")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=a_range, y=F_range))
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("P = mv")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=v_range, y=P_range))
        st.plotly_chart(fig2, use_container_width=True)

    st.metric("Күш (F)", f"{F:.2f} Н")
    st.metric("Импульс (P)", f"{P:.2f}")