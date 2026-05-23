import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [data, setData] = useState([]);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/reports/daily-sales")
      .then((response) => {
        setData(response.data);
      });

  }, []);

  const downloadReport = () => {
    window.open(
      "http://127.0.0.1:8000/reports/download"
    );
  };

  return (
    <div style={{ padding: 20 }}>

      <h1>Daily Sales Report</h1>

      <button onClick={downloadReport}>
        Download CSV
      </button>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>Category</th>
            <th>Total Quantity</th>
            <th>Total Revenue</th>
          </tr>
        </thead>

        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              <td>{row.category}</td>
              <td>{row.total_quantity}</td>
              <td>{row.total_revenue}</td>
            </tr>
          ))}
        </tbody>

      </table>
    </div>
  );
}

export default App;