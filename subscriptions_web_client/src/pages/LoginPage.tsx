import { useState } from 'react';
import { AuthService } from '../services/AuthService';
import { useNavigate } from '@tanstack/react-router';

export const LoginPage = () => {

  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError('');

    try {
      const session = await AuthService.login(email, password);
      localStorage.setItem("session", JSON.stringify(session));
      navigate({ to: "/" });
      alert('Login exitoso');
    } catch (error) {
      console.error('Error al iniciar sesión:', error);
      setError('Error al iniciar sesión. Verifica tus credenciales.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-2xl shadow-md w-full max-w-sm">
        <h2 className="text-2xl font-bold mb-6 text-center">Iniciar sesión</h2>
        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label className="block text-gray-700 mb-1" htmlFor="email">Correo electrónico</label>
            <input
              type="email"
              id="email"
              className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="tucorreo@ejemplo.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-1" htmlFor="password">Contraseña</label>
            <input
              type="password"
              id="password"
              className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700 transition-colors"
          >
            Ingresar
          </button>
        </form>

        {/* Botón de redirección a registro */}
        <div className="mt-4 text-center">
          <p className="text-sm text-gray-600">¿No tienes cuenta?</p>
          <button
            onClick={() => navigate({to: '/register'})} // Redirige a la página de registro
            className="text-blue-600 hover:underline"
          >
            Crear cuenta
          </button>
        </div>
      </div>
    </div>
  );
};
