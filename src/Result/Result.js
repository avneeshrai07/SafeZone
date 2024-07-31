import React from 'react';
import './result.css';
const Result = ({ result }) => {
  console.log("Result in Result.js:", result);

  if (!result) {
    return <p>No result available</p>;
  }
  
  // Create variables for predicted crime types
  let predictedFraudScam, predictedLessOffensiveCrimes, predictedModelAccuracy,
    predictedRobberyTheft, predictedSafetyIndex, predictedSexualCrime, predictedViolentCrimes;

  // Log the structure of the result object
  console.log("Structure of Result Object:", JSON.stringify(result, null, 2));

  // Assign values using Object.entries
  Object.entries(result).forEach(([key, value]) => {
    switch (key) {
      case 'Fraud/Scam':
        predictedFraudScam = value;
        break;
      case 'Less offensive crimes':
        predictedLessOffensiveCrimes = value;
        break;
      case 'Model Accuracy':
        predictedModelAccuracy = value;
        break;
      case 'Robbery/Theft':
        predictedRobberyTheft = value;
        break;
      case 'Safety Index':
        predictedSafetyIndex = value;
        break;
      case 'Sexual crime':
        predictedSexualCrime = value;
        break;
      case 'Violent crimes':
        predictedViolentCrimes = value;
        break;
      default:
        break;
    }
  });

  console.log("Predicted Fraud/Scam:", predictedFraudScam);
  console.log("Predicted Less Offensive Crimes:", predictedLessOffensiveCrimes);
  console.log("Predicted Model Accuracy:", predictedModelAccuracy);
  console.log("Predicted Robbery/Theft:", predictedRobberyTheft);
  console.log("Predicted Safety Index:", predictedSafetyIndex);
  console.log("Predicted Sexual Crime:", predictedSexualCrime);
  console.log("Predicted Violent Crimes:", predictedViolentCrimes);

  return (
    <div className='result'>
      <h1>Crime Prediction Result</h1>
      
          <div className='resultsPrint'>
            <p className='accuracy'>Model Accuracy: {predictedModelAccuracy}%</p>
            <p className='sexual'>Sexual Crime: {predictedSexualCrime}%</p>
            <p className='violent'>Violent Crimes: {predictedViolentCrimes}%</p>
            <p className='robberyTheft'>Robbery/Theft: {predictedRobberyTheft}%</p>
            <p className='fraudScam'>Fraud/Scam: {predictedFraudScam}%</p>
            <p className='lessoffensive'>Less Offensive Crimes: {predictedLessOffensiveCrimes}%</p>
            <p className='safety'>Safety Level: {predictedSafetyIndex}%</p>
            
        </div>
      
    </div>
  );
};

export default Result;
