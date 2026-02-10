import { useState } from "react";

export default function Integration() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  function handleFileChange(event) {
    // event.target.files is a list of files chosen by the user
    const file = event.target.files[0];
    setSelectedFile(file);
    setMessage("");
  }

  async function handleUpload() {
    if (!selectedFile) {
      setMessage("Please select a CSV file first.");
      return;
    }

    setLoading(true);
    setMessage("");

    try {
      // FormData is the standard way to send files in a POST request
      const formData = new FormData();
      formData.append("file", selectedFile); // "file" must match FastAPI parameter name

      const response = await fetch(
        "http://127.0.0.1:8000/integration/sales-orders/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        // backend returned error
        setMessage("Upload failed: " + JSON.stringify(data));
      } else {
        setMessage(
          `Upload success. Rows inserted: ${data.rows_inserted}, Batch: ${data.load_batch_id}`
        );
      }
    } catch (err) {
      setMessage("Upload failed: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h1>Integration</h1>
      <h2>Upload Sales Orders CSV</h2>

      <input type="file" accept=".csv" onChange={handleFileChange} />

      <div style={{ marginTop: "12px" }}>
        <button onClick={handleUpload} disabled={loading}>
          {loading ? "Uploading..." : "Upload Sales Orders"}
        </button>
      </div>

      <p style={{ marginTop: "12px" }}>{message}</p>
    </div>
  );
}