import axios from "axios";
import { Session } from "../models/user-models";
import { getEnvVariables } from "../utilities";

const { VITE_API_URL } = getEnvVariables();

const api = axios.create({
  baseURL: VITE_API_URL,
});

api.interceptors.request.use((config) => {
  const sessionData = localStorage.getItem("session");
  const session: Session = JSON.parse(sessionData || "{}");

  if (
    window.location.pathname !== "/login" &&
    window.location.pathname !== "/register"
  ) {
    config.headers.Authorization = `bearer ${session.token.access_token}`;
  }

  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (
      [401, 403].includes(error.response?.status) &&
      window.location.pathname !== "/login" &&
      window.location.pathname !== "/register"
    ) {
      localStorage.removeItem("session");
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);

export default api;
