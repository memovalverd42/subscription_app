import { useState } from "react";
import { AuthService } from "../services/AuthService";
import { UserCreate } from "../models/user-models";
import { useNavigate } from "@tanstack/react-router";

export const RegisterPage = () => {
  const navigate = useNavigate();
  const [form, setForm] = useState<UserCreate>({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const target = e.target;
    setForm({ ...form, [target.name]: target.value });
  };

  const handleRegister = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError("");
    setSuccess(false);

    try {
      await AuthService.register(form);
      setSuccess(true);
      navigate({ to: "/login" });
      alert('Registro exitoso');
    } catch (err) {
      console.error("Error al registrar el usuario:", err);
      setError("Error al registrar el usuario. Verifica los datos.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-2xl shadow-md w-full max-w-sm">
        <h2 className="text-2xl font-bold mb-6 text-center">Registro</h2>
        <form onSubmit={handleRegister}>
          <div className="mb-4">
            <label className="block text-gray-700 mb-1" htmlFor="first_name">
              Nombre
            </label>
            <input
              type="text"
              id="first_name"
              name="first_name"
              className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={form.first_name || ""}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-1" htmlFor="last_name">
              Apellido
            </label>
            <input
              type="text"
              id="last_name"
              name="last_name"
              className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={form.last_name || ""}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-1" htmlFor="email">
              Correo electrónico
            </label>
            <input
              type="email"
              id="email"
              name="email"
              className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={form.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 mb-1" htmlFor="password">
              Contraseña
            </label>
            <input
              type="password"
              id="password"
              name="password"
              className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={form.password}
              onChange={handleChange}
              required
            />
          </div>

          {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
          {success && (
            <p className="text-green-600 text-sm mb-4">Registro exitoso</p>
          )}

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700 transition-colors"
          >
            Registrarse
          </button>
        </form>

        {/* Botón de redirección al login */}
        <div className="mt-4 text-center">
          <p className="text-sm text-gray-600">
            ¿Ya tienes cuenta?{" "}
            <button
              onClick={() => navigate({ to: "/login" })} // Redirige a la página de login
              className="text-blue-600 hover:underline"
            >
              Iniciar sesión
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};
