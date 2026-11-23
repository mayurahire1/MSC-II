
import React, { useState } from 'react';

function App() {

  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [result, setResult] = useState('');

  const calculate = (op) => {

    let x = Number(a);
    let y = Number(b);

    if (a === '' || b === '') {
      setResult('Enter both numbers');
      return;
    }

    if (op === '+') {
      setResult(x + y);
    }

    if (op === '-') {
      setResult(x - y);
    }

    if (op === '*') {
      setResult(x * y);
    }

    if (op === '/') {
      setResult(y === 0 ? 'Cannot divide by zero' : x / y);
    }
  };

  return (
    <div>
      <h2>Calculator</h2>

      <input
        type="number"
        placeholder="First Number"
        value={a}
        onChange={e => setA(e.target.value)}
      />

      <br /><br />

      <input
        type="number"
        placeholder="Second Number"
        value={b}
        onChange={e => setB(e.target.value)}
      />

      <br /><br />

      <button onClick={() => calculate('+')}>+</button>

      <button onClick={() => calculate('-')}>-</button>

      <button onClick={() => calculate('*')}>*</button>

      <button onClick={() => calculate('/')}>/</button>

      <h3>Result: {result}</h3>

    </div>
  );
}

export default App;
