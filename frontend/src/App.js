import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home/Home';
import Result from './Result/Result';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/safeZone" element={<Home />} />
        <Route path="/safeZone/result" element={<Result />} />
      </Routes>
    </Router>
  );
}

export default App;
