import streamlit as st
import matplotlib.pyplot as plt
from datetime import date


if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): 
    st.session_state.page += 1
def go_back(): 
    st.session_state.page = 0
def restart():
    st.session_state.clear()
    st.session_state.page = 0

def find_index(lst, val):
    try:
        return lst.index(val)
    except Exception:
        return None

def plot_x_scale(value, benchmark):
    st.markdown("▼: Your score")
    st.write("┃: Benchmark score")
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.scatter([benchmark], [0.1], color='olivedrab', s=80, marker='|')
    ax.scatter([value], [0.1], color='black', s=80, marker='v')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(False)
    ax.set_xlabel("Score (0-100)")
    for i, spine in enumerate(ax.spines.values()):
        if i == 2: continue
        spine.set_visible(False)
                
    st.pyplot(fig) 
    

empty = st.empty()

st.set_page_config(page_title="ESG Survey", layout="centered")

if st.session_state.page == 0:

    # Title and header
    with empty.container():
        st.title("ESG Questions")

        #General Questions
        st.header("Company 🏢")

        st.session_state.name = st.text_input("Name of the organisation:",value = st.session_state.get("name",None))
        st.session_state.registration_location = st.selectbox("where was the organisation registered?",["United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"], index=find_index(["United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"], st.session_state.get("registration_location", None)))
        st.session_state.foundation_date = st.date_input("Select the date the company was created:",value= st.session_state.get("foundation_date", date.today()))
        st.session_state.location = st.selectbox("Where is the location of the organisation's headquarters?",["United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"], index=find_index(["United Kingdom", "USA", "France", "Germany", "India", "Australia", "Japan"], st.session_state.get("location", None)))


        #Environmental Questions
        st.header("Environment 🌲")

        st.session_state.fossil_fuels = st.radio("Does the organisation have any involvement with fossil fuels?", ["Yes","No"], index=0 if st.session_state.get("fossil_fuels", None) == "Yes" else (1 if st.session_state.get("fossil_fuels", None) == "No" else None))
        st.session_state.energy_consumption = st.number_input("What is the company's annual energy consumption(kWh)?",value = st.session_state.get("energy_consumption",None))
        st.session_state.waste = st.number_input("What is the company's annual waste generation(kg)?", value = st.session_state.get("waste",None))
        st.session_state.recycle = st.number_input("How much is recycled per year(kg)?", value = st.session_state.get("recycle",None))
        st.session_state.carbon_emissions = st.number_input("What is the total annual carbon emissions for this company(tonnes)?",value = st.session_state.get("carbon_emissions",None))

        #Social Questions
        st.header("Social 🤝")

        st.session_state.employees = st.number_input("Total number of employees?",value = st.session_state.get("employees",None))
        st.session_state.female_employees = st.number_input("Total number of female and non-binary employees?",value = st.session_state.get("female_employees",None))
        st.session_state.outreach = st.radio("Does the organisation have any outreach programs?", ["Yes","No"], index=0 if st.session_state.get("outreach", None) == "Yes" else (1 if st.session_state.get("outreach", None) == "No" else None))
        st.session_state.volunteer_hours = st.number_input("Total volunteer/outreach hours per year?",value = st.session_state.get("volunteer_hours",None))

        #Governance Questions
        st.header("Governance ⚖️")

        
        st.session_state.risk_management = st.radio("Is there a risk management process in place?", ["Yes","No"], index=0 if st.session_state.get("risk_management", None) == "Yes" else (1 if st.session_state.get("risk_management", None) == "No" else None))
        st.session_state.cybersecurity = st.radio("Is there a cybersecurity policy?", ["Yes","No"], index=0 if st.session_state.get("cybersecurity", None) == "Yes" else (1 if st.session_state.get("cybersecurity", None) == "No" else None))
        st.session_state.whistleblower = st.radio("Is there a whistle-blower policy?", ["Yes","No"], index=0 if st.session_state.get("whistleblower", None) == "Yes" else (1 if st.session_state.get("whistleblower", None) == "No" else None))

        st.button("Submit", on_click=nextpage, disabled=(st.session_state.page > 3))

elif st.session_state.page == 1:
    
    with empty.container():
        st.title("ESG Dashboard")

        name = st.session_state.get("name", None)
        energy_consumption = st.session_state.get("energy_consumption", None)
        fossil_fuels = st.session_state.get("fossil_fuels", None)
        outreach = st.session_state.get("outreach", None)
        volunteer_hours = st.session_state.get("volunteer_hours", None)
        waste = st.session_state.get("waste", None)
        recycle = st.session_state.get("recycle", None)
        carbon_emissions = st.session_state.get("carbon_emissions", None)
        employees = st.session_state.get("employees", None)
        female_employees = st.session_state.get("female_employees", None)

        done = True
        for val in st.session_state.values():
            if val is None:
                done = False
                break

        if not done:
            st.warning("Some fields are not filled in yet.")

        elif employees is not None and female_employees is not None:
            if female_employees > employees:
                st.warning("Female employees cannot be more than total employees.")
        
        elif waste is not None and recycle is not None:
            if recycle > waste:
                st.warning("Recycled waste cannot be greater than total waste generated")
            
        else:

            st.header("Environment 🌲")

            tab1, tab2, tab3 = st.tabs(["Energy Consumption", "Waste Management", "Carbon Emissions"])

            with tab1:
                labels = [f"Energy Consumption {name}", "General Energy Consumption"]
                values = [energy_consumption, 500000]
                consumptionFig, consumptionAx = plt.subplots()
                consumptionAx.bar(labels, values, color=["olivedrab" if energy_consumption < 500000 else "firebrick", "olivedrab"])
                consumptionAx.set_ylabel("Energy consumption (kWh)")
                consumptionAx.set_title("Consumption")
                st.pyplot(consumptionFig)

            with tab2:
                
                wasteFig, wasteAx = plt.subplots(figsize=(4, 4))
                wasteAx.pie([recycle, waste - recycle], labels=["Waste recycled", "Waste thrown"], colors=["olivedrab", "firebrick"], radius=0.8, autopct='%.0f%%', textprops={'size': 'smaller'})
                st.pyplot(wasteFig)

            with tab3:
                emissionsFig, emissionsAx = plt.subplots(figsize=(6, 4))
                emissionsAx.bar([name, "General"], [carbon_emissions, 500], color=["olivedrab" if carbon_emissions < 1000 else "firebrick", "olivedrab"])
                emissionsAx.set_ylabel("Carbon Emissions (tonnes)")
                emissionsAx.set_title("Carbon Emissions")
                st.pyplot(emissionsFig)

            st.header("Social 🤝")

            genderFig, genderAx = plt.subplots(figsize=(4, 4))
            genderAx.pie([employees - female_employees, female_employees], labels=["Male employees", "Female/Nonbinary employees"], colors=["cornflowerblue", "darkorange"], radius=0.8, autopct='%.0f%%', textprops={'size': 'smaller'})
            st.pyplot(genderFig)

            # ivh stands for individual volunteer hours
            ivh = st.session_state.get('volunteer_hours', 0) / employees
            st.write(f"20 hours per year is a good benchmark for yearly outreach hours, and you have {ivh} hours per employee, which is **{"above" if ivh >= 20 else "below"}** the benchmark. {"Well done!" if ivh >= 20 else ""}")

            employee_ratio = (female_employees / employees) * 100
            does_outreach = 30 if outreach == "Yes" else 0

            environmental_score = (25 if fossil_fuels == "Yes" else 0) + ((100*(1-((energy_consumption/500000) if energy_consumption > 500000 else 1)))*0.20) + ((100*(1-(waste/50000)))*0.15) + ((100*(recycle/35000))*0.15) + ((100*(1-((carbon_emissions/600) if carbon_emissions < 600 else 1)))*0.25)
            governance_score = [st.session_state.get("risk_management", None), st.session_state.get("cybersecurity", None), st.session_state.get("whistleblower", None)].count("Yes") * (100/3)
            social_score = does_outreach + ((employee_ratio/50))*0.40 + (((volunteer_hours/20) if volunteer_hours < 20 else 1)*100)*0.30


            st.header("Overall Results")
            tab4, tab5, tab6 = st.tabs(["Environment", "Social", "Governance"])
            with tab4:
                plot_x_scale(environmental_score, 38)
            with tab5:
                plot_x_scale(social_score, 56)
            with tab6:
                plot_x_scale(governance_score, 44)

        st.button("Go back", on_click=go_back, disabled=(st.session_state.page > 3))
        st.button("Restart", on_click=restart, disabled=(st.session_state.page > 3))
