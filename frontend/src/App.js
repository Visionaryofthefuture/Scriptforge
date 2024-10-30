import './App.css';
import Navbar from './components/navbar';
import Homepage from './components/homepage';
//import { useEffect, useState } from 'react';

function App() {
  //const [question, setQuestion] = useState(null);

  /*const fetchQuestion = () => {
    fetch('http://127.0.0.1:8000/questions/1')
      .then(response => response.json())
      .then(data => setQuestion(data))
      .catch(error => console.error("Error fetching question:", error));
  };

  useEffect(() => {
    fetchQuestion();
  }, [])
  ;
*/
  return (
    <div className="App">
      <Navbar/>
      <Homepage/>
     </div>
  );
}

export default App;
