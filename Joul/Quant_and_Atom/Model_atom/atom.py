import streamlit as st
import numpy as np
import plotly.graph_objects as go

def show_atom_model():
    st.title("⚛️ Резерфордтың атом моделі")
    st.markdown("""
    Резерфорд моделі бойынша атом оң зарядталған ядродан және оны айнала қозғалатын электрондардан тұрады.
    """)

    # 1. ЭЛЕМЕНТТЕР ТІЗІМІ (Негізгілері және автоматты генерация)
    # Барлық 118 элементтің символдары мен атаулары
    ptable = [
        "", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
        "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
        "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
        "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
        "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
        "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
        "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
        "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
        "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
        "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]

    # 2. БАСҚАРУ ПАНЕЛІ (Максимум 118-ге дейін)
    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
    with col_ctrl1:
        protons = st.number_input("Протондар саны (Z):", min_value=1, max_value=118, value=1)
    with col_ctrl2:
        # Нейтрондарды шамамен есептеу (A ≈ 2Z)
        neutrons = st.number_input("Нейтрондар саны (N):", min_value=0, max_value=200, value=int(protons*1.2))
    with col_ctrl3:
        electrons = st.number_input("Электрондар саны (e):", min_value=0, max_value=118, value=protons)

    element_symbol = ptable[protons] if protons < len(ptable) else "???"
    mass_number = protons + neutrons
    charge = protons - electrons
    charge_text = "Бейтарап" if charge == 0 else (f"Оң ион (+{charge})" if charge > 0 else f"Теріс ион ({charge})")

    st.subheader(f"🔬 Элемент: {element_symbol} (№{protons})")
    
    inf1, inf2, inf3 = st.columns(3)
    inf1.metric("Символ", element_symbol)
    inf2.metric("Масса (A)", mass_number)
    inf3.metric("Заряды", charge_text)
    
    fig_atom = go.Figure()

    # 3. ЯДРО (Протондар мен нейтрондар)
    # Көп элемент болса, ядроны бір үлкен шар ретінде көрсету тиімдірек
    if protons < 20:
        for _ in range(protons):
            fig_atom.add_trace(go.Scatter(x=[np.random.normal(0, 0.15)], y=[np.random.normal(0, 0.15)],
                                         mode="markers", marker=dict(size=10, color="red"), showlegend=False))
        for _ in range(neutrons):
            fig_atom.add_trace(go.Scatter(x=[np.random.normal(0, 0.15)], y=[np.random.normal(0, 0.15)],
                                         mode="markers", marker=dict(size=10, color="gray"), showlegend=False))
    else:
        # Ауыр элементтер үшін ядроны жинақы көрсету
        fig_atom.add_trace(go.Scatter(x=[0], y=[0], mode="markers", 
                                     marker=dict(size=40, color="red", line=dict(width=2, color="gray")), 
                                     name="Ядро", showlegend=False))

    # 4. ОРБИТАЛАР ЖӘНЕ ЭЛЕКТРОНДАР (Қабаттар бойынша)
    # Электрондық қабаттардағы макс. сыйымдылық: 2, 8, 18, 32...
    shell_capacities = [2, 8, 18, 32, 32, 18, 8] 
    t = np.linspace(0, 2*np.pi, 100)
    
    current_electron = 0
    for shell_idx, cap in enumerate(shell_capacities):
        if current_electron >= electrons: break
        
        r = (shell_idx + 1) * 2 # Орбита радиусы
        electrons_in_shell = min(electrons - current_electron, cap)
        
        # Орбита сызығы
        fig_atom.add_trace(go.Scatter(x=r*np.cos(t), y=r*np.sin(t), mode="lines", 
                                     line=dict(color="silver", width=1, dash="dot"), showlegend=False))
        
        # Электрондарды шеңбер бойымен орналастыру
        for i in range(electrons_in_shell):
            angle = (2 * np.pi / electrons_in_shell) * i
            ex = r * np.cos(angle)
            ey = r * np.sin(angle)
            fig_atom.add_trace(go.Scatter(x=[ex], y=[ey], mode="markers", 
                                         marker=dict(size=8, color="blue"), showlegend=False))
        
        current_electron += electrons_in_shell

    fig_atom.update_layout(
        xaxis=dict(visible=False, range=[-16, 16]),
        yaxis=dict(visible=False, range=[-16, 16]),
        width=700, height=700, 
        template="plotly_white",
        title=f"{element_symbol} атомының құрылымы"
    )
    st.plotly_chart(fig_atom, use_container_width=True)