import api from "../api/api";
import { Period, Plan, Subscription } from "../models/subscriptions-models";

export class SubscriptionService {
  static async getSubscriptions(): Promise<Subscription[]> {
    try {
      const response = await api.get("/subscription");
      return response.data;
    } catch (error) {
      console.error("Failed to fetch subscriptions:", error);
      throw new Error("Failed to fetch subscriptions");
    }
  }

  static async cancelSubscription(plan: Plan): Promise<void> {
    try {
      await api.put(`/subscription/cancel?plan=${plan}`);
    } catch (error) {
      console.error("Failed to cancel subscription:", error);
      throw new Error("Failed to cancel subscription");
    }
  }

  static async subscribe(plan: Plan, period: Period): Promise<Subscription> {
    try {
      const response = await api.post("/subscription/subscribe", {
        plan,
        period,
      });
      return response.data;
    } catch (error) {
      console.error("Subscription failed:", error);
      throw new Error("Subscription failed");
    }
  }
}
