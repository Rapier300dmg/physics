import streamlit as st
import numpy as np
import plotly.graph_objects as go

def show_kinematics():
    st.title("📐 Кинематика")

    st.markdown("Равнопеременное движение")
    st.latex(r"s = v_0 t + \frac{a t^2}{2}")

    # параметры
    st.sidebar.header("Параметрлер")

    v0 = st.sidebar.number_input("Бастапқы жылдамдық v₀ (м/с)", value=0.0)
    a = st.sidebar.number_input("Үдеу a (м/с²)", value=2.0)
    t_max = st.sidebar.slider("Уақыт (сек)", 1, 20, 10)

    # расчёты
    t = np.linspace(0, t_max, 100)
    s = v0 * t + (a * t**2) / 2
    v = v0 + a * t

    # графики
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Жол S(t)")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=t, y=s))
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Жылдамдық V(t)")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=t, y=v))
        st.plotly_chart(fig2, use_container_width=True)

    # итог
    st.metric("Соңғы жылдамдық", f"{v[-1]:.2f} м/с")
    st.metric("Жүрілген жол", f"{s[-1]:.2f} м")