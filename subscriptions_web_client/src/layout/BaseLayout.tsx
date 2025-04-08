import { ReactNode } from "@tanstack/react-router";

export const BaseLayout = ({ children }: { children: ReactNode }) => {
  return <main>{children}</main>;
};
