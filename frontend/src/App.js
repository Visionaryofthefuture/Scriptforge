import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [question, setQuestion] = useState(null);

  const fetchQuestion = () => {
    fetch('http://127.0.0.1:8000/questions/1')
      .then(response => response.json())
      .then(data => setQuestion(data))
      .catch(error => console.error("Error fetching question:", error));
  };

  useEffect(() => {
    fetchQuestion();
  }, []);

  return (
    <div className="App">
      <h1> Question Details </h1>
      {question ? (
        <div>
          <h2>Difficulty: {question.difficulty}</h2>
          <h3>Title: {question.title}</h3>
          <p>Description: {question.description}</p>
          <p>Sample Input: {question.sample_input}</p>
          <p>Sample Output: {question.sample_output}</p>
          <p>Constraints: {question.constraints}</p>
          <p>Maker: {question.maker}</p>
        </div>
      ) : (
        <p>Loading question...</p>
      )}
    </div>
  );
}

export default App;
