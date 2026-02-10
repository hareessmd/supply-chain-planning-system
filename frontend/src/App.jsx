import { useEffect, useState } from "react";
import "./App.css";
import Integration from "./pages/Integration";

function App() {
  const [health, setHealth] = useState("unknown");
  const [page, setPage] = useState("dashboard");

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

        <div className="nav-item" onClick={() => setPage("dashboard")}>
          Dashboard
        </div>

        <div className="nav-item" onClick={() => setPage("integration")}>
          Integration
        </div>
      </div>

      <div className="content">
        {page === "dashboard" && (
          <>
            <h1>Dashboard</h1>
            <p>Backend health: {health}</p>
          </>
        )}

        {page === "integration" && <Integration />}
      </div>
    </div>
  );
}

export default App;