import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import API from "../api";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale);

export default function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const fetchProjects = async () => {
    const { data } = await API.get("/projects");
    setProjects(data);
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  const createProject = async () => {
    await API.post("/projects", { name, description });
    fetchProjects();
  };

  const chartData = {
    labels: projects.map((p) => p.name),
    datasets: [
      {
        label: "Projects",
        data: projects.map(() => 1),
        backgroundColor: "rgba(54, 162, 235, 0.6)"
      }
    ]
  };

  return (
    <div className="p-10">
      <h1 className="text-2xl mb-4">Dashboard</h1>

      <div className="mb-6">
        <input
          className="border p-2 mr-2"
          placeholder="Project Name"
          onChange={(e) => setName(e.target.value)}
        />
        <input
          className="border p-2 mr-2"
          placeholder="Description"
          onChange={(e) => setDescription(e.target.value)}
        />
        <button
          onClick={createProject}
          className="bg-blue-500 text-white px-3 py-2"
        >
          Add Project
        </button>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {projects.map((p) => (
          <Link
            key={p._id}
            to={`/projects/${p._id}`}
            className="border p-4 hover:bg-gray-100"
          >
            <h2 className="font-bold">{p.name}</h2>
            <p>{p.description}</p>
          </Link>
        ))}
      </div>

      <div className="mt-10">
        <Bar data={chartData} />
      </div>
    </div>
  );
}
