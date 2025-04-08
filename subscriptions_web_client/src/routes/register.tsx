import { createFileRoute, redirect } from '@tanstack/react-router'
import { isLoggedIn } from '../utilities/is-logged-in';
import { RegisterPage } from '../pages/RegisterPage';



export const Route = createFileRoute('/register')({
  component: RegisterPage,
  beforeLoad: async () => {
    if (isLoggedIn()) {
      throw redirect({
        to: '/',
      })
    }
  }
});

