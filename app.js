import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [courses, setCourses] = useState(["COMP 110", "MATH233", "PHYS119"]);
  const [results, setResults] = useState([]);

  const handleGenerate = async () => {
    const res = await axios.post("http://localhost:8000/generate", {
      courses: courses,
      start_time: "8AM",
      end_time: "5PM"
    });
    setResults(res.data.schedules);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Schedule Generator</h2>
      <button onClick={handleGenerate}>Generate Schedules</button>

      {results.map((r, idx) => (
        <div key={idx} style={{ marginTop: 20 }}>
          <h4>Schedule #{idx + 1} (Avg Rating: {r.average_rating.toFixed(2)})</h4>
          <ul>
            {r.schedule.map((c, i) => (
              <li key={i}>{c.course} – {c.time} – ★ {c.rating}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default App;
