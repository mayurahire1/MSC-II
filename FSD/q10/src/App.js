
import React, { useState } from 'react';

function App() {

  const [num, setNum] = useState('');
  const [result, setResult] = useState('');

  const calculate = () => {

    if (num.trim() === '' || !/^\d+$/.test(num)) {
      setResult('Invalid Number');
      return;
    }

    let sum = 0;

    for (let digit of num) {
      sum = sum + Number(digit);
    }

    setResult('Sum of Digits = ' + sum);
  };

  return (
    <div>
      <h2>Number Validation</h2>

      <input
        value={num}
        onChange={e => setNum(e.target.value)}
        placeholder="Enter Number"
      />

      <button onClick={calculate}>Calculate</button>

      <h3>{result}</h3>
    </div>
  );
}

export default App;
