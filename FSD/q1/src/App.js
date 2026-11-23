
import React from 'react';

function App() {

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form Submitted");
  };

  return (
    <div>
      <h2>Login Form</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          placeholder="Username"
          onInput={(e) => console.log(e.target.value)}
          // onChange={(e) => console.log(e.target.value)}
        />

        <br /><br />

        <input
          type="password"
          placeholder="Password"
          onInput={(e) => console.log(e.target.value)}
          // onChange={(e) => console.log(e.target.value)}
        />

        <br /><br />

        <button type="submit">Login</button>

      </form>
    </div>
  );
}

export default App;
