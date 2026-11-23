//npm install react-router-dom


import React, { useState } from 'react';

import {
  BrowserRouter,
  Routes,
  Route,
  useNavigate
} from 'react-router-dom';

function Login() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const login = () => {

    if (username === 'Admin' && password === 'Pass123') {
      alert('Valid Login');
      navigate('/home');
    } else {
      alert('Unauthorized Access');
    }

  };

  return (
    <div>
      <h2>Login Form</h2>

      <input
        placeholder="Username"
        onChange={e => setUsername(e.target.value)}
      />

      <br /><br />

      <input
        type="password"
        placeholder="Password"
        onChange={e => setPassword(e.target.value)}
      />

      <br /><br />

      <button onClick={login}>Login</button>
    </div>
  );
}

function Home() {
  return <h2>Welcome Admin</h2>;
}

function App() {
  return (
    <BrowserRouter>

      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route
          path="*"
          element={<h2>404 Error, Page Not Found</h2>}
        />
      </Routes>

    </BrowserRouter>
  );
}

export default App;
