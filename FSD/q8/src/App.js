
import React, { useState } from 'react';

function App() {

  const [status, setStatus] = useState(false);

  return (
    <div>
      <h2>Toggle Button</h2>

      <button
        onClick={() => setStatus(!status)}
        style={{
          backgroundColor: status ? 'green' : 'red',
          color: 'white',
          padding: '10px'
        }}
      >
        {status ? 'ON' : 'OFF'}
      </button>

    </div>
  );
}

export default App;
