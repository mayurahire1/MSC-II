
import React, { useState, useEffect } from 'react';

function App() {

  const [users, setUsers] = useState([]);

  useEffect(() => {

    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(data => setUsers(data));

  }, []);

  return (
    <div>
      <h2>User Details</h2>

      {users.map(user => (
        <div key={user.id}>
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
        </div>
      ))}

    </div>
  );
}

export default App;
