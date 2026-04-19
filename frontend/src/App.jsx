import { useState } from "react";
import axios from "axios";
import Header from "./components/Header";
import Form from "./components/Form";
import OutputBox from "./components/OutputBox";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    topic: "",
    genre: "Drama",
    mood: "Emotional",
    scene_length: "Medium",
  });

  const [scene, setScene] = useState("");
  const [retrievedContext, setRetrievedContext] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleGenerate = async () => {
    if (!formData.topic.trim()) {
      setError("Please enter a topic first.");
      setScene("");
      setRetrievedContext("");
      return;
    }

    setLoading(true);
    setError("");
    setScene("");
    setRetrievedContext("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/generate",
        formData
      );

      if (response.data.error) {
        setError(response.data.error);
      } else {
        setScene(response.data.scene || "");
        setRetrievedContext(response.data.retrieved_context || "");
      }
    } catch (err) {
      setError("Failed to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <Header />

      <Form
        formData={formData}
        handleChange={handleChange}
        handleGenerate={handleGenerate}
        loading={loading}
      />

      <OutputBox title="Error" content={error} isError={true} />
      <OutputBox title="Retrieved Context" content={retrievedContext} />
      <OutputBox title="Generated Scene" content={scene} />
    </div>
  );
}

export default App;