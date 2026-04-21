import streamlit as st
import numpy as np
import plotly.graph_objects as go

def show_atom_model():
    st.title("⚛️ Резерфордтың атом моделі")
    st.markdown("""
    Резерфорд моделі бойынша атом оң зарядталған ядродан және оны айнала қозғалатын электрондардан тұрады.
    """)

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
    with col_ctrl1:
        protons = st.number_input("Протондар саны (Z):", min_value=1, max_value=10, value=1)
    with col_ctrl2:
        neutrons = st.number_input("Нейтрондар саны (N):", min_value=0, max_value=12, value=0)
    with col_ctrl3:
        electrons = st.number_input("Электрондар саны (e):", min_value=0, max_value=10, value=1)

    elements = {
        1: "Сутегі (H)", 2: "Гелий (He)", 3: "Литий (Li)", 4: "Бериллий (Be)", 5: "Бор (B)",
        6: "Көміртек (C)", 7: "Азот (N)", 8: "Оттегі (O)", 9: "Фтор (F)", 10: "Неон (Ne)"
    }
    
    element_name = elements.get(protons, "Белгісіз элемент")
    mass_number = protons + neutrons
    charge = protons - electrons
    charge_text = "Бейтарап" if charge == 0 else (f"Оң ион (+{charge})" if charge > 0 else f"Теріс ион ({charge})")

    st.subheader(f"🔬 Модель: {element_name}")
    
    inf1, inf2, inf3 = st.columns(3)
    inf1.metric("Элемент", element_name)
    inf2.metric("Массалық сан (A)", mass_number)
    inf3.metric("Заряды", charge_text)
    
    fig_atom = go.Figure()

    # Ядро
    for i in range(protons):
        fig_atom.add_trace(go.Scatter(x=[np.random.uniform(-0.3, 0.3)], y=[np.random.uniform(-0.3, 0.3)],
                                     mode="markers", marker=dict(size=15, color="red"), showlegend=False))
    for i in range(neutrons):
        fig_atom.add_trace(go.Scatter(x=[np.random.uniform(-0.3, 0.3)], y=[np.random.uniform(-0.3, 0.3)],
                                     mode="markers", marker=dict(size=15, color="gray"), showlegend=False))

    # Орбиталар
    t = np.linspace(0, 2*np.pi, 100)
    orbits = [2, 4, 6] 
    for i in range(electrons):
        idx = 0 if i < 2 else (1 if i < 8 else 2)
        r = orbits[idx]
        angle = (2 * np.pi / (2 if idx==0 else 6)) * (i % 8)
        fig_atom.add_trace(go.Scatter(x=r*np.cos(t), y=r*np.sin(t), mode="lines", 
                                     line=dict(color="silver", width=1, dash="dot"), showlegend=False))
        fig_atom.add_trace(go.Scatter(x=[r*np.cos(angle)], y=[r*np.sin(angle)], mode="markers", 
                                     marker=dict(size=10, color="blue"), showlegend=False))

    fig_atom.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), width=600, height=600, template="plotly_white")
    st.plotly_chart(fig_atom, use_container_width=True)