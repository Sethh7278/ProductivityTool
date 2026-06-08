import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'




function App() {
  const [tasks, setTasks] = useState([]);
  

  useEffect(() => {
    fetch("http://localhost:8000/tasks")
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setTasks(data)
      });
  }, []);


  const taskItems = tasks.map(task => <li key={task.id}>{task.name}</li>)

  return (

    
    <>
      <section id="center">
        <div className="hero">
        </div>
        <div>
          <h1>AI Productivity App</h1>
        
        </div>
        <div>
          <h1>Tasks to complete</h1>  
          {tasks &&<h2> <ul>{taskItems}</ul></h2>}
        </div>
      </section>
    </>
  )
}

export default App
