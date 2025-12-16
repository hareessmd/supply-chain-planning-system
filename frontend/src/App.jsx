import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [health, setHealth] = useState("unknown");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((res) => res.json())
      .then((data) => setHealth(data.status))
      .catch(() => setHealth("error"));
  }, []);

  return (
    <div className="app-container">
      <div className="sidebar">
        <h2>SC Planning</h2>
        <div className="nav-item">Dashboard</div>
        <div className="nav-item">Integration</div>
        <div className="nav-item">Forecasting</div>
        <div className="nav-item">Supply Planning</div>
      </div>
      <div className="content">
        <h1>Dashboard</h1>
        <p>Backend health: {health}</p>
      </div>
    </div>
  );
}

export default App;