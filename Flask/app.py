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

        # Use subprocess.PIPE to capture the output
        process = subprocess.Popen(['python', safe_zone_model_path, userGender, userAgeLevel, userAreaName], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        if process.returncode == 0:
            output = out.decode('utf-8')
            print("Subprocess Output:", output)

            try:
                # Parse the output string and create a dictionary
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

                # ... (other relevant information)

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
