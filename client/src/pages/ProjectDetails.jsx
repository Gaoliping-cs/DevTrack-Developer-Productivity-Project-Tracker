import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import API from "../api";

export default function ProjectDetails() {
  const { id } = useParams();
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const fetchTasks = async () => {
    const { data } = await API.get(`/tasks/${id}`);
    setTasks(data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const createTask = async () => {
    await API.post("/tasks", { title, projectId: id });
    setTitle("");
    fetchTasks();
  };

  const toggleTask = async (taskId, completed) => {
    await API.put(`/tasks/${taskId}`, { completed: !completed });
    fetchTasks();
  };

  return (
    <div className="p-10">
      <h1 className="text-xl mb-4">Project Tasks</h1>

      <div className="mb-4">
        <input
          className="border p-2 mr-2"
          placeholder="New Task"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button
          onClick={createTask}
          className="bg-blue-500 text-white px-3 py-2"
        >
          Add
        </button>
      </div>

      {tasks.map((task) => (
        <div
          key={task._id}
          className="border p-3 mb-2 flex justify-between"
        >
          <span
            onClick={() => toggleTask(task._id, task.completed)}
            className={task.completed ? "line-through cursor-pointer" : "cursor-pointer"}
          >
            {task.title}
          </span>
        </div>
      ))}
    </div>
  );
}
