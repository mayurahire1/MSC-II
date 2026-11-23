
import React from 'react';

function App() {

  const movies = [
    '3 Idiots',
    'Dangal',
    'Chhichhore',
    'PK',
    'Drishyam',
    'Bahubali',
    'KGF',
    'Pushpa',
    '12th Fail',
    'Shershaah'
  ];

  return (
    <div>

      <h2>My Favorite Movies</h2>

      <ul>
        {movies.map((movie, index) => (
          <li key={index}>
            {movie}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default App;
