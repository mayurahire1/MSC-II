
import React, { useState } from 'react';

function App() {

  const [status, setStatus] = useState(false);

  return (
    <div>
      <h2>Toggle Button</h2>

      <button onClick={() => setStatus(!status)}>
        {status ? "ON" : "OFF"}
      </button>

    </div>
  );
}

export default App;
