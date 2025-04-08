import { createFileRoute } from "@tanstack/react-router";
import { SubscriptionsPage } from "../../pages/SubscriptionsPage";

export const Route = createFileRoute("/_layout/subscriptions")({
  component: SubscriptionsPage,
});
