// npm install react-router-dom

import React, { useState } from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from 'react-router-dom';

function Home() {
  return <h2>Welcome to Protected Page</h2>;
}

function Login() {
  return <h2>Please Login First</h2>;
}

function App() {
  const [auth, setAuth] = useState(false);

  return (
    <BrowserRouter>

      <button onClick={() => setAuth(!auth)}>
        {auth ? "Logout" : "Login"}
      </button>

      <Routes>

        <Route
          path="/Home"
          element={
            auth ? <Home /> : <Navigate to="/login" />
          }
        />

        <Route
          path="/login"
          element={
            auth ? <Navigate to="/Home" /> : <Login />
          }
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
