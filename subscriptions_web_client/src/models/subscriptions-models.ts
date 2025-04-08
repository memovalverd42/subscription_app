export type Period = "monthly" | "yearly";

export type Plan = "free" | "basic" | "premium";

export type Status = "active" | "inactive" | "canceled";

export interface Subscription {
  id: number;
  user_id: number;
  plan: Plan;
  status: Status;
  start_date: string;
  end_date: string;
}

export interface SubscriptionCreate {
  plan: Plan;
  period: Period;
}
