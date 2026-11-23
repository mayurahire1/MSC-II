// npm install react-router-dom

import React from 'react';

import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from 'react-router-dom';

function Home() {
  return <h2>Welcome to Home Page</h2>;
}

function About() {
  return <h2>About Us</h2>;
}

function Contact() {
  return (
    <div>
      <h2>Contact Us</h2>

      <form>
        <input type="text" placeholder="Enter Name" required />

        <br /><br />

        <input type="email" placeholder="Enter Email" required />

        <br /><br />

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>

      <Link to="/">Home</Link> |
      <Link to="/about">About</Link> |
      <Link to="/contact">Contact</Link>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="*" element={<h2>404 Page Not Found</h2>} />
      </Routes>

    </BrowserRouter>
  );
}

export default App;
