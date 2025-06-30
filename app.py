from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Question:
    def __init__(self, question_text, name, required=True):
        self.question_text = question_text
        self.name = name
        self.required = "required" if required else ""

    def many(self, *args):
        optionshtml = ""
        for option in args:
            optionshtml += f'   <label><input type="checkbox" name="{self.name}" value="{option[1]}"> {option[0]}</label><br>\n'
        return f"""<div class="fieldset_"><fieldset>\n<legend>{self.question_text}</legend>\n{optionshtml}\n</fieldset></div>"""
    def one(self, *args):
        optionshtml = ""
        for option in args:
            optionshtml += f'<label><input type="radio" name="{self.name}" value="{option[1]}" {self.required}> {option[0]}</label><br>\n'
        return f"""<div class="fieldset_"><fieldset>\n<legend>{self.question_text}</legend>\n{optionshtml}\n</fieldset></div><br>"""
    def line(self):
        return f'<label for="{self.name}">{self.question_text}</label><br>\n<input type="text" id="{self.name}" name="{self.name}" {self.required}><br><br>\n'
    def number(self):
        return f'<label for="{self.name}">{self.question_text}</label><br>\n<input type="number" id="{self.name}" name="{self.name}" {self.required}><br><br>\n'
    def para(self):
        return f'<label for="{self.name}">{self.question_text}</label><br><textarea id="{self.name}" name="{self.name}" rows="5" cols="40"></textarea><br><br>\n'
    def date(self):
        return f"""<label for="{self.name}">{self.question_text}</label><br>\n<input type="date" id="{self.name}" name="{self.name}"><br><br>\n"""
    def dropdown(self, *args):
        optionshtml = ""
        for option in args:
            optionshtml += f'<option value="{option}">{option}</option>\n'
        return f"""<label for="{self.name}">{self.question_text}</label><br>\n<select id={self.name} name={self.name} {self.required} >{optionshtml}</select><br><br>"""


general_questions_html = f"""
{Question("What is your company name?", "company_name").line()}
{Question("Place of registration?", "place_of_registration").dropdown("UK", "Not UK")}
{Question("Date of foundation", "date_of_foundation").date()}
{Question("Current main headquarters", "current_main_headquarters").dropdown("London", "New York", "Berlin", "Other")}
{Question("Number of locations", "number_of_locations").one(("1", "1"), ("2-5", "2-5"), ("6-10", "6-10"), ("11+", "11+"))}"""

environment_questions_html = f"""
{Question("Do you have any involvement with fossil fuels?", "fossil_fuels").one(("Yes", "yes"), ("No", "no"))}
{Question("If yes, what products?", "fossil_fuels_products", required=False).para()}
{Question("What is the company's energy consumption in kWh?", "energy_consumption").number()}
{Question("How much waste does the company produce per year?", "waste_produced").number()}
{Question("How much waste does the company recycle per year?", "waste_recycled").number()}
{Question("What is the company's carbon emission in tonnes?", "carbon_emission").number()}"""

social_questions_html = f"""
{Question("What has been done to improve community engagement?", "community_engagement").para()}
{Question("Number of Employees?","no_of_employees").number()}
{Question("Number of Female/Non-Binary staff in the workplace?","gender_diversity").number()}
{Question("Number of Employee training hours per year","training_hours").number()}
{Question("Total number of volunteer hours","volunteer_hours").number()}
{Question("Number of outreach programs?","outreach_programs").number()}
"""
governance_questions_html = f"""
{Question("Is there a risk management process in place?","risk_management").one(("Yes","yes"),("No","no"))}
{Question("Is there a cybersecurity policy?","cybersecurity_policy").one(("Yes","yes"),("No","no"))}
{Question("Is there a whistleblower policy?","whistleblower policy").one(("Yes","yes"),("No","no"))}
{Question("Number of board members?","board_members").number()}
"""
 

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', generalQ=general_questions_html, environmentQ=environment_questions_html)

@app.route('/response', methods=['POST'])
def submit():
    score = 0
    values = request.form
    
    if values['fossil_fuels'] == "yes":
        score = 0
    else:
        score = 100


    return f"""
    {values}
    """

@app.route('/scores', methods=['POST'])
def scores():
    values = request.form

    return render_template(
        'scores.html', 
        energy_consumption_data=values['energy_consumption'], 
        recycled=values['waste_recycled'], 
        waste_ovr=values['waste_produced']
    )

if __name__ == '__main__':
    app.run(debug=True)

