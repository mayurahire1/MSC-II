
import React, { useState } from 'react';

function App() {

  const [str, setStr] = useState('');

  return (
    <div>
      <h2>String Operations</h2>

      <input
        type="text"
        placeholder="Enter String"
        onChange={e => setStr(e.target.value)}
      />

      <h3>Uppercase: {str.toUpperCase()}</h3>

      <h3>Lowercase: {str.toLowerCase()}</h3>

      <h3>Length: {str.length}</h3>

      <h3>Reverse: {str.split('').reverse().join('')}</h3>

    </div>
  );
}

export default App;