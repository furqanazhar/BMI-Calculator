# BMI Calculator
This application calculates BMI by reading an input json file (`data/data.json`) of people with their respective weights and heights.

Below is the output result:
1. BMI Values, BMI Category and Health Risk (added in output json file in path `data/result.json`)
2. Total number of overweight people

# Tested Environment
Windows 11\
Visual Studio Code\
Python 3.8.8

# Unit Testing

Run below command in windows shell to perform unit testing
```bash
pytest test_app.py
```

Output is shown in console which contains below information:
1. Total number of tests
2. Total number of tests passed
3. Total number of tests failed
4. Total execution time

# Execution

1. Run build.exe file located in root folder of project to run application
2. After .exe file gets finished, go to `data/result.json` to find output file

# How to generate .exe file of a python script
Run below command in windows shell to run updated .exe file in case you make any changes in scripts
```bash
pip install pyinstaller
pyinstaller --onefile --name build app.py
```
3rd argument 'build' here is the filename of generated exe. You can name it anything. 
4th argument app.py is the main python script file name whose exe needs to be generated
