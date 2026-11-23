
import React, { useState } from 'react';

function Counter(props) {

  const [count, setCount] = useState(props.initial);

  return (
    <div>
      <h2>Count: {count}</h2>

      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>

      <button onClick={() => setCount(count - 1)}>
        Decrement
      </button>
    </div>
  );
}

function App() {
  return (
    <div>
      <Counter initial={0} />
    </div>
  );
}

export default App;
