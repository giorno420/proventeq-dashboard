import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

 
# Page config
st.set_page_config(page_title="My Streamlit App", layout="centered")

# Title and header
st.title("ESG Dashboard")

#General Questions
st.header("Company 🏢")

name = st.text_input("Name of the organisation:")
Registration_options = st.selectbox("where was the organisation registered?",["Choose a country","United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"])
Date_of_Foundation = st.date_input("Select the date the company was created:",value=date.today())
Location_of_HQ = st.selectbox("Where is the location of the organisation's headquarters?",["Choose a country","United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"])

#Environmental Questions
st.header("Environment 🌲")

fossil_fuels = st.radio("Does the organisation have any involvement with fossil fuels?", ["Yes","No"],)
energy_consumption = st.text_input("What is the company's annual energy consumption(kWh)?")
waste = st.text_input("What is the company's annual waste generation(kg)?")
recycle = st.text_input("How much is recycled per year(kg)?")
Carbon_Emissions = st.text_input("What is the total annual carbon emissions for this company(tonnes)?")

#Social Questions
st.header("Social 🤝")

Employees = st.text_input("Total number of employees?")
F_Employees = st.text_input("Total number of female and non-binary employees?")
Training_Hours = st.text_input("Total individual employee training hours per year?")
Outreach = st.radio("Does the organisation have any outreach programs?", ["Yes","No"],)
Volunteer_Hours = st.text_input("Total individual employee volunteer hours per year?")

#Governance Questions
st.header("Governance ⚖️")

Risk_management = st.radio("Is there a risk management process in place?", ["Yes","No"],)
Cybersecurity = st.radio("Is there a cybersecurity policy?", ["Yes","No"],)
Whistleblower = st.radio("Is there a whistle-blower policy?", ["Yes","No"],)
