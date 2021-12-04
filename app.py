import json
from os import write
from helper import get_bmi, get_bmi_category, get_total_overweight_people

def read_file(json_file):

    # Opening JSON file
    file = open(json_file)
    
    # convert JSON object into a dictionary
    input_data = json.load(file)
    
    # Closing file as we have saved data in variable 'data'
    file.close()

    # Iterating through the list and calculating 'BMI', 'BMI Category' and 'Health Risk'
    for item in input_data:
        
        # Converting Height into Meters
        HeightMeter = (item['HeightCm']/100)
        # Adding BMI value in the dictionary
        item['BMI'] = get_bmi(item['WeightKg'], HeightMeter)
        # Adding BMI Category and Health Risk in the dictionary
        item['BMICategory'], item['HealthRisk'] = get_bmi_category(item['BMI'])

    print(input_data)

    # Calculate total number of 'overweight' people in dictionary
    print('\nTotal Number of Overweight People = ' + str(get_total_overweight_people(input_data)) + '\n')

    return input_data

def write_file(dictionary):
    with open('data/result.json', 'w') as fp:
        json.dump(dictionary, fp, indent=1)

if __name__ == '__main__':

    file_path = 'data/data.json'

    bmi_dictionary = read_file(file_path)

    write_file(bmi_dictionary)