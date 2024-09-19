import {useState, useEffect} from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import HomePage from './pages/HomePage';
import Navbar from './components/Navbar';
import AsideMenu from './components/AsideMenu';
import { jwtDecode } from "jwt-decode"; // descodificar el token


function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false); // Estado de autenticación
    const [userName, setUserName] = useState(''); // Nombre del usuario, puedes ajustarlo según tu lógica

    useEffect(() => {
        const token = localStorage.getItem('access_token');
        if (token) {
            const decodedToken = jwtDecode(token);
            setIsLoggedIn(true);
            setUserName(decodedToken.username); // Asegúrate de que el token contenga el campo 'username'
            console.log(decodedToken)
        } else {
            console.log("El token no contiene el campo 'username'")
        }
    }, []);


    const handleLogout = () => {
        setIsLoggedIn(false);
        localStorage.removeItem('access_token'); // Elimina el token al cerrar sesión
    };

    return (
        <Router>
        <div className="flex h-screen">
            <div>
            <AsideMenu isLoggedIn={isLoggedIn} userName={userName} handleLogout={handleLogout} />
            </div>
            
            <div className="flex flex-col flex-grow">
            <Navbar />
                
                <main className="flex-grow overflow-y-auto">
                    <Routes>
                        <Route path="/homepage" element={<HomePage />} />
                        {/* <Route path="/register" element={<Register />} /> */}
                        <Route path="/login" element={<Login setIsLoggedIn={setIsLoggedIn} setUserName={setUserName} />} />
                        {/* <Route path="/dashboard" element={<Dashboard />} /> */}
                        <Route path="/" element={<Navigate to="/homepage" />} /> {/* Redirigir a homepage por defecto */}
                    </Routes>
                </main>
            </div>
        </div>
    </Router>
    );
}

export default App;