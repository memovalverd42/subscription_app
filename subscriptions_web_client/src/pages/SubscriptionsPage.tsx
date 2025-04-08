import { useEffect, useState } from "react";
import { SubscriptionService } from "../services/SubscriptionsService";
import { Period, Plan, Subscription } from "../models/subscriptions-models";

export const SubscriptionsPage = () => {
  const [subscriptions, setSubscriptions] = useState<Subscription[]>([]);
  const [plan, setPlan] = useState<Plan>("free");
  const [period, setPeriod] = useState<Period>("monthly");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const loadSubscriptions = async () => {
    try {
      const data = await SubscriptionService.getSubscriptions();
      setSubscriptions(data);
      setError("");
    } catch (err) {
      console.error("Error al cargar las suscripciones:", err);
      setError("Error al cargar las suscripciones");
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = async (plan: Plan) => {
    try {
      await SubscriptionService.cancelSubscription(plan);
      loadSubscriptions();
      setError("");
    } catch (err) {
      console.error("Error al cancelar la suscripción:", err);
      setError("Error al cancelar la suscripción");
    }
  };

  const handleCreate = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await SubscriptionService.subscribe(plan, period);
      loadSubscriptions();
      setError("");
    } catch (err) {
      console.error("Error al crear la suscripción:", err);
      setError("Error al crear la suscripción");
    }
  };

  useEffect(() => {
    loadSubscriptions();
  }, []);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Tus suscripciones</h2>
        <button
          onClick={() => {
            localStorage.removeItem("session");
            window.location.href = "/login";
          }}
          className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-4 py-2 rounded-xl"
        >
          Cerrar sesión
        </button>
      </div>

      {error && <p className="text-red-500 mb-4">{error}</p>}

      {loading ? (
        <p>Cargando...</p>
      ) : (
        <ul className="space-y-4 mb-8">
          {subscriptions.map((sub) => (
            <li
              key={sub.id}
              className="border rounded-xl p-4 shadow-sm flex justify-between items-center"
            >
              <div>
                <p className="font-semibold capitalize">Plan: {sub.plan}</p>
                <p className="text-sm text-gray-600">Estado: {sub.status}</p>
                <p className="text-sm text-gray-500">Desde: {sub.start_date}</p>
                <p className="text-sm text-gray-500">Hasta: {sub.end_date}</p>
              </div>
              {sub.status === "active" && (
                <button
                  onClick={() => handleCancel(sub.plan)}
                  className="bg-red-500 text-white px-4 py-2 rounded-xl hover:bg-red-600"
                >
                  Cancelar
                </button>
              )}
            </li>
          ))}
        </ul>
      )}

      <h3 className="text-xl font-semibold mb-4">Agregar nueva suscripción</h3>
      <form onSubmit={(e) => handleCreate(e)} className="space-y-4">
        <div>
          <label className="block mb-1">Plan</label>
          <select
            value={plan}
            onChange={(e) => setPlan(e.target.value as Plan)}
            className="w-full border px-3 py-2 rounded-xl"
          >
            <option value="free">Free</option>
            <option value="basic">Basic</option>
            <option value="premium">Premium</option>
          </select>
        </div>
        <div>
          <label className="block mb-1">Periodo</label>
          <select
            value={period}
            onChange={(e) => setPeriod(e.target.value as Period)}
            className="w-full border px-3 py-2 rounded-xl"
          >
            <option value="monthly">Mensual</option>
            <option value="yearly">Anual</option>
          </select>
        </div>
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700"
        >
          Suscribirse
        </button>
      </form>
    </div>
  );
};
