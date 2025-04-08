import { createFileRoute, redirect } from '@tanstack/react-router'
import { LoginPage } from '../pages/LoginPage';
import { isLoggedIn } from '../utilities/is-logged-in';



export const Route = createFileRoute('/login')({
  component: LoginPage,
  beforeLoad: async () => {
    if (isLoggedIn()) {
      throw redirect({
        to: '/',
      })
    }
  }
});

