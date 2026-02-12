import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api";

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    email: "",
    password: ""
  });

  const submit = async () => {
    const { data } = await API.post("/auth/login", form);
    localStorage.setItem("token", data.token);
    navigate("/dashboard");
  };

  return (
    <div className="p-10 max-w-md mx-auto">
      <h1 className="text-2xl mb-4">Login</h1>

      <input
        className="border p-2 w-full mb-2"
        placeholder="Email"
        onChange={(e) => setForm({ ...form, email: e.target.value })}
      />
      <input
        type="password"
        className="border p-2 w-full mb-2"
        placeholder="Password"
        onChange={(e) => setForm({ ...form, password: e.target.value })}
      />

      <button
        onClick={submit}
        className="bg-green-500 text-white px-4 py-2 w-full"
      >
        Login
      </button>
    </div>
  );
}
