def get_bmi(weight, height):
    return round((weight/height),1)

def get_bmi_category(bmi_value):
    if bmi_value<=18.4:
        return 'UnderWeight','Malnutrition Risk'
    elif bmi_value<=24.9:
        return 'Normal Weight','Low Risk'
    elif bmi_value<=29.9:
        return 'OverWeight','Enhanced Risk'
    elif bmi_value<=34.9:
        return 'Moderately Obese','Medium Risk'
    elif bmi_value<=39.9:
        return 'Severely Obese','High Risk'
    else:
        return 'Very Severely Obese','Very High Risk'

def get_total_overweight_people(bmi_json):
    return sum([1 for i in bmi_json if i['BMICategory'] == 'OverWeight'])
