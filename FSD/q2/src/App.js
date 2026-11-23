
import React, { useState, useEffect } from 'react';

function App() {

  const [users, setUsers] = useState([]);

  useEffect(() => {

    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then(data => setUsers(data));

  }, []);

  return (
    <div>
      <h2>User List</h2>

      {users.map(user => (
        <p key={user.id}>
          {user.name} - {user.email}
        </p>
      ))}

    </div>
  );
}

export default App;
