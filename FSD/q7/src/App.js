
import React, { useState } from 'react';

function App() {

  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  const addTask = () => {

    if (task.trim() !== '') {
      setTasks([...tasks, task]);
      setTask('');
    }

  };

  const deleteTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  return (
    <div>
      <h2>TODO List</h2>

      <input
        value={task}
        onChange={e => setTask(e.target.value)}
        placeholder="Enter Task"
      />

      <button onClick={addTask}>Add</button>

      {tasks.map((t, index) => (
        <p key={index}>
          {t}

          <button onClick={() => deleteTask(index)}>
            Delete
          </button>
        </p>
      ))}

    </div>
  );
}

export default App;
