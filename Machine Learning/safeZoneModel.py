import json
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the new dataset
dataset_path = 'C:\\Users\\avnee\\OneDrive\\Desktop\\webd\\SafeZone\\Database\\Safe-ZoneDB.csv'
data = pd.read_csv(dataset_path)

# Select relevant columns
data = data[['Gender', 'Age Level', 'Area Name', 'Crime Category', 'Crime Level']]

# Encode categorical variables
le_gender = LabelEncoder()
le_gender.fit(data['Gender'].unique())
le_area = LabelEncoder()
le_area.fit(data['Area Name'].unique())
data['Gender'] = le_gender.transform(data['Gender'])
data['Area Name'] = le_area.transform(data['Area Name'])

# Split the data into features (X) and target variable (y)
X = data[['Gender', 'Area Name', 'Age Level']]
y = data['Crime Category']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Check if the expected number of command-line arguments is provided
if len(sys.argv) != 4:
    print("Usage: python safeZoneModel.py <userGender> <userAgeLevel> <userAreaName>")
    sys.exit(1)

# Access command-line arguments
userGender = sys.argv[1]
userAgeLevel = sys.argv[2]
userAreaName = sys.argv[3]

# Create DataFrame with user input
new_data = pd.DataFrame({
    'Gender': [userGender],
    'Age Level': [userAgeLevel],
    'Area Name': [userAreaName]
})

# Encode categorical variables for new data
gender_input = new_data['Gender'].iloc[0]
area_input = new_data['Area Name'].iloc[0]
age_input = int(new_data['Age Level'].iloc[0])

# Check if the input values are present in the training data, otherwise use default values
gender_encoded = le_gender.transform([gender_input])[0] if gender_input in le_gender.classes_ else le_gender.transform(['M'])[0]
area_encoded = le_area.transform([area_input])[0] if area_input in le_area.classes_ else le_area.transform(['Gomti nagar'])[0]

# Handle 'Age Level' input
if 0 <= age_input <= 10:
    age_encoded = age_input
else:
    age_encoded = 0 if age_input < 0 else 10

# Update the new_data with encoded values
new_data['Gender'] = gender_encoded
new_data['Area Name'] = area_encoded
new_data['Age Level'] = age_encoded

# Predict probabilities for each class
prediction_probabilities = model.predict_proba(new_data[['Gender', 'Area Name', 'Age Level']])

# Ensure that each class has at least a 1% chance
min_probability = 0.01
prediction_probabilities[0] = [max(prob, min_probability) for prob in prediction_probabilities[0]]

# Normalize the probabilities
normalized_probabilities = prediction_probabilities[0] / sum(prediction_probabilities[0])

# Print the calculated crime predictions
calculated_crime_predictions = {crime: prob for crime, prob in zip(model.classes_, normalized_probabilities)}
print("Calculated Crime Predictions:")

for crime, prob in calculated_crime_predictions.items():
    print(f"{crime}: {prob * 100:.2f}%")

# Create variables for each calculated crime
calculated_Violent_crimes = round(calculated_crime_predictions['Violent crimes'] * 100, 2)
calculated_Sexual_crime = round(calculated_crime_predictions['Sexual crime']*100,2)
calculated_Robbery_Theft = round(calculated_crime_predictions['Robbery/Theft']*100,2)
calculated_Fraud_Scam = round(calculated_crime_predictions['Fraud/Scam']*100,2)
calculated_Less_offensive_crimes = round(calculated_crime_predictions['Less offensive crimes']*100,2)

# Create a pie chart for each crime category
plt.figure(figsize=(10, 5))
plt.pie(normalized_probabilities * 100, labels=model.classes_, autopct='%1.1f%%', startangle=140)
plt.title('Percentage Chance of Each Crime Category')

# Show the crime % plot
plt.show()

# Calculate safety index based on adjusted crime predictions
safety_index = 100 - (0.75 * (calculated_Violent_crimes + calculated_Sexual_crime) +
                     0.50 * calculated_Robbery_Theft +
                     0.25 * (calculated_Fraud_Scam + calculated_Less_offensive_crimes))

# Print the safety index
print(f'Safety Index: {safety_index:.2f}')

# Create a pie chart for safety percentages
plt.figure(figsize=(6, 6))
safety_labels = ['Safe', 'Unsafe']
plt.pie([safety_index, 100-safety_index], labels=safety_labels, autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
plt.title('Safety Index')

# Show the plot
plt.show()

# Assess the safety level based on the safety index
if safety_index > 75:
    print("It is safe to travel through this area.")
elif safety_index > 50:
    print("Exercise caution while traveling through this area.")
else:
    print("It is highly unsafe to travel through this area.")