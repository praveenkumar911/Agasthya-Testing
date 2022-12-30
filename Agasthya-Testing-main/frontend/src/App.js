
import React from "react"
import Questions from "./pages/components/question";
import Answers from "./pages/components/answer";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/login"
import Navbar from "./pages/components/navBar";

function App() {
  return (
      <Router>
        <Navbar />
        <Routes>
          <Route path="/answers" element={<Answers />} />
          <Route path="/questions" element={<Questions/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="*" element={<> not found</>} />
        </Routes>
    
    </Router>
  );
}

export default App;