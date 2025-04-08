export const isLoggedIn = () => {
  return localStorage.getItem("session") !== null;
};