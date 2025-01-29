import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} exact />
          // Add other routes here
        </Routes>
      </div>
    </Router>
  );
}

export default App;
