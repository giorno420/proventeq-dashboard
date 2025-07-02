import streamlit as st
import matplotlib.pyplot as plt
from datetime import date
import plotly.express as px

# Page config
st.set_page_config(page_title="My Streamlit App", layout="centered")

page = st.sidebar.radio("Navigate to:", ["Questions", "ESG Dashboard"])

if page == "Questions":


    # Title and header
    st.title("ESG Questions")

    #General Questions
    st.header("Company 🏢")

    name = st.text_input("Name of the organisation:")
    Registration_options = st.selectbox("where was the organisation registered?",["Choose a country","United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"])
    Date_of_Foundation = st.date_input("Select the date the company was created:",value=date.today())
    Location_of_HQ = st.selectbox("Where is the location of the organisation's headquarters?",["Choose a country","United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"])

    #Environmental Questions
    st.header("Environment 🌲")

    st.session_state.fossil_fuels = st.radio("Does the organisation have any involvement with fossil fuels?", ["Yes","No"],)
    st.session_state.energy_consumption = st.number_input("What is the company's annual energy consumption(kWh)?")
    st.session_state.waste = st.number_input("What is the company's annual waste generation(kg)?")
    st.session_state.recycle = st.number_input("How much is recycled per year(kg)?")
    st.session_state.Carbon_Emissions = st.number_input("What is the total annual carbon emissions for this company(tonnes)?")

    #Social Questions
    st.header("Social 🤝")

    st.session_state.Employees = st.number_input("Total number of employees?")
    st.session_state.F_Employees = st.number_input("Total number of female and non-binary employees?")
    st.session_state.Training_Hours = st.number_input("Total individual employee training hours per year?")
    st.session_state.Outreach = st.radio("Does the organisation have any outreach programs?", ["Yes","No"],)
    st.session_state.Volunteer_Hours = st.number_input("Total individual employee volunteer hours per year?")

    #Governance Questions
    st.header("Governance ⚖️")

    st.session_state.Risk_management = st.radio("Is there a risk management process in place?", ["Yes","No"],)
    st.session_state.Cybersecurity = st.radio("Is there a cybersecurity policy?", ["Yes","No"],)
    st.session_state.Whistleblower = st.radio("Is there a whistle-blower policy?", ["Yes","No"],)

elif page == "ESG Dashboard":
    
    # Title and header
    st.title("ESG Dashboard")

    st.header("Environment 🌲")

    energy_consumption = st.session_state.get("energy_consumption", None)

    if energy_consumption is None:
        st.warning("Please fill out the 'Questions' page first.")
    else:
        labels = ["Energy Consumption (This Company)", "General Energy Consumption"]
        values = [energy_consumption, 500000]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color=["red", "yellow"])
        ax.set_ylabel("Energy consumption (kWh)")
        ax.set_title("Consumption")

        st.pyplot(fig)

    waste = st.session_state.get("waste", None)
    recycle = st.session_state.get("recycle", None)

    if waste is None or recycle is None :
        st.warning("Please fill out the 'Questions' page first.")
    else:
        df = px.data.tips()
        fig2 = px.pie(df, values='tip', names='day')
        st.plotly_chart(fig2)



