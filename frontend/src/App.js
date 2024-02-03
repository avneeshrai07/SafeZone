import { useState, useEffect } from 'react';
import {BrowserRouter,Router,Routes,Route} from 'react-router-dom'
import './App.css';
import Home from './Home/Home';
import Result from './Result/Result';

function App() {
  const [predictionResult, setPredictionResult] = useState(null);

  const handlePredict = async (data) => {
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
  
      const result = await response.json();
  
      console.log("Response from server:", result);
  
      if (result.success) {
        console.log("Prediction Result State (before update):", predictionResult);
        setPredictionResult(result.calculatedCrimePredictions);
        console.log("Prediction Result State (after update):", result.calculatedCrimePredictions);
      } else {
        throw new Error(result.error || 'Invalid response');
      }
    } catch (error) {
      console.error('Prediction failed:', error);
      throw new Error(error.message || 'Failed to fetch');
    }

    <Router>
      <Routes>
        <Route path="/safeZone" element={<Home/>}></Route>
        <Route path="/safeZone/result" element={<Result/>}></Route>
      </Routes>    
    </Router>

  };
  return (
    <div className="App">
      <Home onPredict={handlePredict} predictionResult={predictionResult} />
    </div>
  );
}

export default App;
