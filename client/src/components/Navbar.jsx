import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div className="bg-gray-800 text-white p-4 flex justify-between">
      <Link to="/dashboard">DevTrack</Link>

      {token && (
        <button onClick={logout} className="bg-red-500 px-3 py-1 rounded">
          Logout
        </button>
      )}
    </div>
  );
}
