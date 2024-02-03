import React, { useState } from 'react';
// import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import Result from '../Result/Result';
import './home.css'

function Home({ onPredict, predictionResult }) {
  const [selectedGender, setSelectedGender] = useState('');
  const [selectedAgeLevel, setSelectedAgeLevel] = useState('');
  const [selectedArea, setSelectedArea] = useState('');
  // const navigate = useNavigate();

  const handleGenderChange = (event) => {
    setSelectedGender(event.target.value);
  };

  const handleAgeLevelChange = (event) => {
    setSelectedAgeLevel(event.target.value);
  };

  const handleAreaChange = (event) => {
    setSelectedArea(event.target.value);
  };

  const handlePredictClick = async () => {
    try {
      // navigate('/safeZone/result')
      const result = await onPredict({
        gender: selectedGender,
        ageLevel: selectedAgeLevel,
        areaName: selectedArea,
      });
      console.log("Result in Home.js:", result);
    } catch (error) {
      console.error('Error predicting crime:', error);
    }
  };
  
  return (
    <div className='Home'>
      <div className='userInputs'>
        <div className='Gender'>
          <label>Gender:</label>
          <select value={selectedGender} onChange={handleGenderChange}>
            <option value=''>Select Gender</option>
            <option value='M'>Male</option>
            <option value='F'>Female</option>
          </select>
        </div>
        <div className='AgeLevel'>
          <label>Age Level:</label>
          <select value={selectedAgeLevel} onChange={handleAgeLevelChange}>
            <option value=''>Select Your Age</option>
            <option value='0'>0 Years to 3 Years</option>
            <option value='1'>4 Years to 12 Years</option>
            <option value='2'>13 Years to 19 Years</option>
            <option value='3'>20 Years to 29 Years</option>
            <option value='4'>30 Years to 39 Years</option>
            <option value='5'>40 Years to 49 Years</option>
            <option value='6'>50 Years to 59 Years</option>
            <option value='7'>60 Years to 69 Years</option>
            <option value='8'>70 Years to 79 Years</option>
            <option value='9'>80 Years to 89 Years</option>
            <option value='10'>90 Years to 99 Years</option>
            <option value='11'>100 Years to 110 Years</option>
            <option value='12'>110+ Years </option>
          </select>
        </div>
        <div className='AreaName'>
          <label>Area Name:</label>
          <select value={selectedArea} onChange={handleAreaChange}>
          <option value=''>Select Area Name</option>
          <option value='Gomti nagar'>Gomti nagar</option>
          <option value='Amar shaheed path'>Amar shaheed path</option>
          <option value='Hazratganj'>Hazratganj</option>
          <option value='Aishbagh'>Aishbagh</option>
          <option value='Indranagar'>Indranagar</option>
          <option value='Aminaabad'>Aminaabad</option>
          <option value='Safedabad'>Safedabad</option>
          <option value='Aliganj'>Aliganj</option>
          <option value='Rajaipuram'>Rajaipuram</option>
          <option value='Aliganj'>Aliganj</option>
          <option value='kaisarbagh'>kaisarbagh</option>
          <option value='Arjunganj'>Arjunganj</option>
          <option value='Husainabad'>Husainabad</option>
          <option value='Cantonment'>Cantonment</option>
          <option value='chinhat'>chinhat</option>
          <option value='Marutipuram'>Marutipuram</option>
          <option value='Jankipuram'>Jankipuram</option>
          <option value='IIM Road'>IIM Road</option>
          <option value='Faizabaad road'>Faizabaad road</option>
          <option value='Civil Lines'>Civil Lines</option>
          <option value='Ahmamau'>Ahmamau</option>
          </select>
        </div>
      </div>
      <div className='Predict'>
        <button onClick={handlePredictClick}>Predict</button>
      </div>


      <div className="PredictionResult">
      <h3>Prediction Result:</h3>
      <Result result={predictionResult} />
      </div>



    </div>
  );
}

export default Home;
