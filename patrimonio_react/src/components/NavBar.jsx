import { useState, useEffect } from "react";
import { Menu, LogIn, UserPlus } from "lucide-react";
import { useNavigate } from "react-router-dom";



export default function Navbar() {

    const [isNavbarFixed, setIsNavbarFixed] = useState(false);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [user, setUser] = useState({ name: "", email: "" });
    const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      setIsNavbarFixed(window.scrollY > 10);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleLogin = () => {
    setIsAuthenticated(false);
    navigate("/login");
  };

  const handleLogout = () => {
    setIsAuthenticated(true);
    res = setUser({ name: "", email: "" });
    console.log(res)
  };

  const getInitials = (name) => {
    return name
      .split(" ")
      .map((n) => n[0])
      .join("")
      .toUpperCase();
  };
  return (
    <nav
      className={`w-full bg-white transition-all duration-300 ${
        isNavbarFixed ? "fixed top-0 left-0 z-50 shadow-sm" : ""
      }`}>
      <div className="max-w-5xl mx-auto px-4">
        <div className="flex items-center justify-between h-14">
          <span className="text-lg font-semibold text-gray-800">Mi Sitio</span>
          <div className="flex items-center space-x-4">
            <div className="hidden sm:block">
              <input
                type="search"
                placeholder="Buscar..."
                className="w-40 border border-gray-300 rounded-md px-2 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            {isAuthenticated ? (
              <div className="flex items-center space-x-3">
                <div className="h-8 w-8 rounded-full bg-gray-300 flex items-center justify-center text-gray-500 font-semibold">
                  {getInitials(user.name)}
                </div>
                <button
                  className="bg-white border border-gray-300 rounded-md px-2 py-1 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  onClick={handleLogout}>
                  Salir
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <button
                  className="bg-white border border-gray-300 rounded-md px-2 py-1 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  onClick={handleLogin}>
                  <LogIn className="h-4 w-4 mr-1 inline-block" />
                  Entrar
                </button>
                <button className="bg-blue-500 text-white rounded-md px-2 py-1 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
                  <UserPlus className="h-4 w-4 mr-1 inline-block" />
                  Registro
                </button>
              </div>
            )}
            <button className="bg-white border border-gray-300 rounded-md px-2 py-1 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500 sm:hidden">
              <Menu className="h-5 w-5 inline-block" />
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}
