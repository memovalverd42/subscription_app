import api from "../api/api";
import { Session, UserCreate } from "../models/user-models";

export class AuthService {
  static async login(email: string, password: string): Promise<Session> {
    try {
      const response = await api.post("/users/login", {
        email,
        password,
      });
      return response.data;
    } catch (error) {
      console.error("Login failed:", error);
      throw new Error("Login failed");
    }
  }

  static async register(user: UserCreate): Promise<Session> {
    try {
      const response = await api.post("/users", user);
      return response.data;
    } catch (error) {
      console.error("Registration failed:", error);
      throw new Error("Registration failed");
    }
  }
}
