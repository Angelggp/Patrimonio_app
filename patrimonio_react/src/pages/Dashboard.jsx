import React from 'react';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('access_token'); // Eliminar el token de acceso
        navigate('/login'); // Redirigir a la página de inicio de sesión
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-3xl mb-4">Bienvenido al Dashboard</h1>
            <p className="mb-4">Has iniciado sesión exitosamente.</p>
            <button onClick={handleLogout} className="bg-red-500 text-white p-2">Cerrar Sesión</button>
        </div>
    );
};

export default Dashboard;