from flask import Flask, request, jsonify, send_from_directory
import subprocess
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Get the current directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
machine_learning_dir = os.path.join(script_dir, '..', 'Machine Learning')
safe_zone_model_path = os.path.join(machine_learning_dir, 'safeZoneModel.py')

@app.route('/predict', methods=['POST'])
def predict_crime():
    try:
        input_data = request.json
        print("Input Data:", input_data)

        userGender = input_data.get('gender')
        userAgeLevel = input_data.get('ageLevel')
        userAreaName = input_data.get('areaName')

        # Created subprocess to capture the output or error from the safeZone model
        process = subprocess.Popen(

        # progamme name (python), program path(safeZoneModelPath) are the fixed arguments
        # gender, Age, Area are the variable arguments
        ['python', safe_zone_model_path, userGender, userAgeLevel, userAreaName], 

        # capture the standard output (stdout or any print()statement) of the script
        stdout=subprocess.PIPE, 

        # capture the error in any ocured in the script
        stderr=subprocess.PIPE
        )

        # capture the output and the error of the after ruuning the subprocess
        out, err = process.communicate()

        if process.returncode == 0:
            output = out.decode('utf-8')
            print("Subprocess Output:", output)

            # the output will look something like this:
            # "Calculated Crime Predictions:\nViolent crimes: 25.00%\nSexual crime: 15.00%\nRobbery/Theft: 30.00%\nFraud/Scam: 10.00%\nLess offensive crimes: 20.00%\nSafety Index: 70.00\n"


            try:
                # created a dictionary to store the result
                output_dict = {"success": True}

                # Extract the calculated crime predictions from the output string
                calculated_crime_predictions = {}
                for line in output.split('\n'):
                    if line.startswith('Calculated Crime Predictions:'):
                        continue
                    elif ':' in line:
                        crime, prob = line.split(':')
                        calculated_crime_predictions[crime.strip()] = float(prob.strip().replace('%', ''))

                # Include the calculated crime predictions in the response
                output_dict["calculatedCrimePredictions"] = calculated_crime_predictions


                return jsonify(output_dict)
            except Exception as parse_error:
                return jsonify({"success": False, "error": f"Failed to parse output: {str(parse_error)}"})
        else:
            # If the subprocess returned an error, return the error as a string
            return jsonify({"success": False, "error": err.decode('utf-8')})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)