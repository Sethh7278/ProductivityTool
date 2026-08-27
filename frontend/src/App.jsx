import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [tasks, setTasks] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0)
  const [newTaskName, setTaskName] = useState("")
  const [deleteTaskID, setDeleteTaskID] = useState()
  const [updateTaskID, setUpdateTaskID] = useState()
  const [error, setError] = useState(null)
  const [status, setStatus] = useState('typing')
  const [taskComplete, setTaskComplete] = useState()


  // This takes the value from the input, and sets state of the Taskname to the event
  const handleTextareaChange = (e) => {
    setTaskName(e.target.value);
  }

  const handleDeleteTaskID = (e) => {
    setDeleteTaskID(e.target.value);
  }


  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("http://localhost:8000/Create-Task",{
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: newTaskName,
        complete: false
      })
  })
  }

    const handleTaskUpdate = (e) =>{
      setUpdateTaskID(e.target.value)
    } 

    const handleUpdate = (e) => {
      e.preventDefault
      fetch("http://localhost:8000/tasks/" + updateTaskID, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          "complete":taskComplete
        })
      })
    }


    const completed = (event) =>{
      event.preventDefault();
      setTaskComplete(true)
    }

    const incomplete = (event) =>{
      event.preventDefault();
      setTaskComplete(false)
    }
  // Creating a function for the button that changes each task individually
  const nextTask = () => {
    if((currentIndex + 1) > (tasks.length - 1)){
      setCurrentIndex(0);
    }else {
      setCurrentIndex(prevTask => prevTask + 1);
    }

  }

  // Using an if statement so the user cant go below the lowest task
  const previousTask = () => {
    if ((currentIndex  - 1) < 0){
      setCurrentIndex(0);
    }
    else{
    setCurrentIndex(prevTask => prevTask - 1);
    
  }}

    const handleDelete = (event) => {
      event.preventDefault();
      fetch("http://localhost:8000/Delete-Task/" + deleteTaskID,{
        method: 'delete'
      })
    }

    


  useEffect(() => {
    fetch("http://localhost:8000/tasks")
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setTasks(data);
      });
  }, []);


  const taskItems = tasks.map(task => <li key={task.id}>{task.name} </li>)

  const individualTask = tasks[currentIndex]

  return (

    
    <>
      <section id="center">
        <div className="hero">
        </div>
        <div>
          <h1>AI Productivity App</h1>
        
        </div>




        <div>
          <h1>Create</h1>
            <h2>Create a new Task</h2>
            <form onSubmit={handleSubmit}>
            <input
            value={newTaskName} 
            onChange={handleTextareaChange}
            /><br/>
            <button>Submit</button>
            </form>
            <br/>
            <p>{newTaskName}</p>
        </div>

        <div>
          <h1>Read</h1>
          <h2>Tasks to complete</h2>  
          {tasks &&<h3> <ul>{taskItems}</ul></h3>}
          {individualTask && <h2>{currentIndex}<br/> 
            {individualTask.name} {individualTask.id} <br/> {individualTask.complete ? "Complete" : "Incomplete"}
            </h2>}
            <button onClick={nextTask}> Next Task</button>
            <button onClick={previousTask}>Previous task</button>
        </div>
            <br/>

        <div>
          <h1>Update</h1>
          <h2>Update a Task</h2>
          <p>{taskComplete ? "Complete" : "Incomplete"}</p>
          <form onSubmit={handleUpdate}>
          <input
          value={updateTaskID}
          onChange={handleTaskUpdate}
          placeholder='Enter Task ID'
          ></input><br/>
          <button onClick={completed}>Completed</button><button onClick={incomplete}>Incomplete</button><br/>
          <button type='submit'>Update Task</button>
          
          </form>
        </div><br/>





        <div>
          <h1>Delete</h1>
          <form onSubmit={handleDelete}>
            <input
            value={deleteTaskID}
            onChange={handleDeleteTaskID}
            placeholder='Enter Task ID'>
            </input><br/>
            <button>Delete</button>
          </form>
          <p>{deleteTaskID}</p>
        </div>
      </section>
    </>
  )
}

export default App
