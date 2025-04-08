# Proyecto de Gestión de Suscripciones

Este proyecto es una prueba tecnica aplicación web para la gestión de suscripciones, con funcionalidades de login, registro y control de suscripciones. Está desarrollada con **React** y utiliza **TailwindCSS** para el estilo. Los usuarios pueden registrarse, iniciar sesión, ver sus suscripciones actuales y agregar o cancelar suscripciones.

## Funcionalidades

* **Login de usuario**: Permite a los usuarios ingresar a la aplicación con su correo electrónico y contraseña.
* **Registro de usuario**: Permite a los usuarios crear una nueva cuenta con su nombre, apellido, correo electrónico y contraseña.
* **Gestión de suscripciones**: Los usuarios pueden ver sus suscripciones activas, agregar nuevas y cancelar suscripciones existentes.
* **Cierre de sesión**: Los usuarios pueden cerrar sesión en la aplicación.

## Tecnologías utilizadas

* **React**: Librería de JavaScript para la construcción de interfaces de usuario.
* **TailwindCSS**: Framework CSS para estilos rápidos y responsivos.
* **Tanstack Router**: Para la navegación entre las páginas de la aplicación.
* **LocalStorage**: Para mantener la sesión activa del usuario.
* **TypeScript**: Para mejorar la seguridad y escalabilidad del código.

## Páginas

1. **LoginPage**: Página para iniciar sesión con el correo electrónico y la contraseña.
2. **RegisterPage**: Página para registrar un nuevo usuario.
3. **SubscriptionsPage**: Página para visualizar, agregar o cancelar suscripciones del usuario logueado.

## Servicios

* **AuthService**: Un servicio que maneja la autenticación, incluyendo login y registro.

* **SubscriptionService**: Un servicio para menajar las suscripciones.

## Modelos

* **UserBase**: Información básica del usuario (nombre, apellido, correo).
* **User**: Extiende de `UserBase`, incluyendo el `id` del usuario.
* **UserCreate**: Información necesaria para crear un nuevo usuario (nombre, apellido, correo, contraseña).
* **Subscription**: Modelo de suscripción con información sobre el plan, fechas y estado de la suscripción.
* **SubscriptionCreate**: Información necesaria para crear una nueva suscripción (plan y periodo).

## Instalación

Para empezar a trabajar con la aplicación, sigue estos pasos:

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/gestion-suscripciones.git
cd gestion-suscripciones
```

2. Instala las dependencias:

```bash
npm install
```

3. Inicia el servidor de desarrollo:

```bash
npm run dev
```

## Rutas de la aplicación

* `/login`: Página de inicio de sesión.
* `/register`: Página de registro de usuario.
* `/subscriptions`: Página de gestión de suscripciones del usuario.

## Detalles del Proyecto

* **Login y Registro**: Los usuarios pueden iniciar sesión con su correo y contraseña o registrarse con su nombre, correo y una nueva contraseña.
* **Gestión de suscripciones**: Los usuarios logueados pueden ver sus suscripciones activas, agregar nuevas suscripciones seleccionando un plan y periodo (mensual o anual), y cancelar suscripciones existentes.
* **Autenticación**: La sesión del usuario se guarda en `localStorage` para mantener al usuario autenticado entre recargas de página.