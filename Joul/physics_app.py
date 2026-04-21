import streamlit as st

# --- ИМПОРТТАР ---
from Mechanics.Force_Impulse.force_impulse import show_force_impulse
from Mechanics.Kinematics.kinematics import show_kinematics
from Mechanics.Work_Power_Energy.work_energy import show_work_energy
from Mechanics.World_law_G.gravity import show_gravity

from Electrostatics.Coulumb.men_fizik import show_coulomb
from Electrostatics.Electrocondensator.electrocondensator import show_condensator
from Electrostatics.Energy_of_charge.charge import show_energy
from Electrostatics.Joule.joule import show_joule

from Quant_and_Atom.Model_atom.atom import show_atom_model
from Quant_and_Atom.Photoeffect.foto import show_photoeffect

from Thermodynamics.Heat_process.heat import show_heat_processes
from Thermodynamics.Klaiperon.mend_klai import show_mend_klai 
from Thermodynamics.MKT.mkt import show_mkt  # Жаңа импорт

# --- НАСТРОЙКА ---
st.set_page_config(page_title="Physics Interactive App", layout="wide")

st.sidebar.title("📚 Физика курсы")
main = st.sidebar.selectbox(
    "Бөлімді таңдаңыз:",
    ["Басты бет", "Механика", "Электростатика", "Термодинамика", "Кванттық физика"]
)

# --- ЛОГИКА ---
if main == "Басты бет":
    st.title("🚀 Интерактивті Физика")
    st.write("Мәзірден керекті бөлімді таңдап, зерттеуді бастаңыз.")

elif main == "Механика":
    sub = st.sidebar.radio("Тақырып:", ["Күш және импульс", "Кинематика", "Жұмыс және энергия", "Бүкіләлемдік тартылыс заңы"])
    if sub == "Күш және импульс": show_force_impulse()
    elif sub == "Kinematics": show_kinematics()
    elif sub == "Жұмыс және энергия": show_work_energy()
    elif sub == "Бүкіләлемдік тартылыс заңы": show_gravity()

elif main == "Электростатика":
    sub = st.sidebar.radio("Тақырып:", ["Кулон заңы", "Электроконденсатор", "Заряд энергиясы", "Джоуль-Ленц заңы"])
    if sub == "Кулон заңы": show_coulomb()
    elif sub == "Электроконденсатор": show_condensator()
    elif sub == "Заряд энергиясы": show_energy()
    elif sub == "Джоуль-Ленц заңы": show_joule()

elif main == "Термодинамика":
    sub = st.sidebar.radio("Тақырып:", ["Жылулық процестер", "Клапейрон-Менделеев заңы", "МКТ"]) # МКТ қосылды
    if sub == "Жылулық процестер": show_heat_processes()
    elif sub == "Клапейрон-Менделеев заңы": show_mend_klai()
    elif sub == "МКТ": show_mkt() # Функция шақырылады

elif main == "Кванттық физика":
    sub = st.sidebar.radio("Тақырып:", ["Атом моделі", "Фотоэффект"])
    if sub == "Атом моделі": show_atom_model()
    elif sub == "Фотоэффект": show_photoeffect()