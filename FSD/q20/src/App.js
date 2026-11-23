// npm install react-router-dom


import React from 'react';

import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  useParams
} from 'react-router-dom';

// // Home Component
// function Home() {
//   return (
//     <div>
//       <h2>Login Successful</h2>

//       <h3>User List</h3>

//       <Link to="/user/101">View User 101</Link>
//       <br /><br />

//       <Link to="/user/102">View User 102</Link>
//       <br /><br />

//       <Link to="/user/103">View User 103</Link>
//     </div>
//   );
// }

// User Component
function User() {

  const { id } = useParams();

  const users = {
    101: {
      name: "Mayur"
    },

    102: {
      name: "Vivek"
    },

    103: {
      name: "Mangesh"
    }
  };

  const user = users[id];

  return (
    <div>
      <h2>User Details</h2>

      {user ? (
        <div>
          <p>User ID: {id}</p>
          <p>Name: {user.name}</p>
        </div>
      ) : (
        <h3>User Not Found</h3>
      )}

      <br />

      <Link to="/">Go Home</Link>
    </div>
  );
}

function App() {

  return (
    <BrowserRouter>

      <Routes>

        {/* <Route path="/" element={<Home />} /> */}

        <Route path="/user/:id" element={<User />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;