import json
from helper import get_bmi, get_bmi_category, get_total_overweight_people

def test_get_bmi():
    assert get_bmi(75,1.75)==42.9

def test_get_bmi_category():
    assert get_bmi_category(42.9) == ('Very Severely Obese','Very High Risk')
    assert get_bmi_category(38.5) == ('Severely Obese','High Risk')
    assert get_bmi_category(33.2) == ('Moderately Obese','Medium Risk')
    assert get_bmi_category(27.7) == ('OverWeight','Enhanced Risk')
    assert get_bmi_category(22.8) == ('Normal Weight','Low Risk')
    assert get_bmi_category(2.4) == ('UnderWeight','Malnutrition Risk')

def test_get_total_overweight_people():
    file = open('data/test_overweight1.json')
    input_data = json.load(file)
    assert get_total_overweight_people(input_data) == 2
    file = open('data/test_overweight2.json')
    input_data = json.load(file)
    assert get_total_overweight_people(input_data) == 8