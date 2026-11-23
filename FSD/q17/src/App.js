
import React, { useState } from 'react';

function App() {

  const [login, setLogin] = useState(false);

  return (
    <div>

      <h2>
        {login
          ? 'Hello, Welcome in Home Page'
          : 'Please sign in first'}
      </h2>

      {login ? (

        <button onClick={() => setLogin(false)}>
          Sign Out
        </button>

      ) : (

        <button onClick={() => setLogin(true)}>
          Sign In
        </button>

      )}

    </div>
  );
}

export default App;
