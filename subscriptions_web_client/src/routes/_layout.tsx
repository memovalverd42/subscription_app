import { createFileRoute, Outlet, redirect } from '@tanstack/react-router';
import { isLoggedIn } from '../utilities/is-logged-in';
import { BaseLayout } from '../layout/BaseLayout';

export const Route = createFileRoute('/_layout')({
  component: Layout,
  beforeLoad: async () => {
    if (!isLoggedIn()) {
      throw redirect({
        to: '/login',
      });
    }
  }
});

function Layout() {

  return (
    <BaseLayout>
      <Outlet />
    </BaseLayout>
  );
}
