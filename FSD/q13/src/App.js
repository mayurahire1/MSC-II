// npm install @reduxjs/toolkit react-redux

// File 1 : counterSlice.js
// File 2 : store.js
// File 3 : App.js
// File 4 : index.js

import React from 'react';

import { useSelector, useDispatch } from 'react-redux';

import { increment, decrement } from './counterSlice';

function App() {

  const count = useSelector(state => state.counter.count);

  const dispatch = useDispatch();

  return (
    <div>
      <h2>Counter: {count}</h2>

      <button onClick={() => dispatch(increment())}>
        Increment
      </button>

      <button onClick={() => dispatch(decrement())}>
        Decrement
      </button>

    </div>
  );
}

export default App;
