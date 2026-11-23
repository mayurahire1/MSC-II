// npm install redux react-redux

// File 1 : store.js
// File 2 : App.js
// File 3 : index.js


import React from 'react';

import { useSelector, useDispatch } from 'react-redux';

function App() {

  const count = useSelector(state => state.count);

  const dispatch = useDispatch();

  return (
    <div>
      <h2>Counter: {count}</h2>

      <button
        onClick={() => dispatch({ type: 'INCREMENT' })}
      >
        Increment
      </button>

      <button
        onClick={() => dispatch({ type: 'DECREMENT' })}
      >
        Decrement
      </button>

    </div>
  );
}

export default App;
