# Proyecto de Gestión de Suscripciones (Prueba Tecnica)

Este es un proyecto web que permite a los usuarios gestionar sus suscripciones. Consta de dos partes: el **Frontend** (interfaz de usuario) y la **API** (backend para manejar la lógica de negocios). Está diseñado para permitir a los usuarios registrarse, iniciar sesión, visualizar sus suscripciones, agregar nuevas suscripciones y cancelarlas.

## Funcionalidades

### Frontend (React + TailwindCSS)
* **Login de usuario**: Permite a los usuarios iniciar sesión con correo electrónico y contraseña.
* **Registro de usuario**: Los usuarios pueden registrarse con nombre, apellido, correo electrónico y contraseña.
* **Gestión de suscripciones**: Los usuarios pueden ver sus suscripciones, agregar nuevas suscripciones y cancelarlas.
* **Cierre de sesión**: Los usuarios pueden cerrar sesión y salir de la aplicación.

### API (Python + FastAPI)
* **Autenticación**: Los usuarios pueden registrarse y autenticar sus credenciales (login).
* **Gestión de suscripciones**: La API maneja la creación, visualización y cancelación de suscripciones de los usuarios.
* **Modelo de datos**: Manejo de usuarios y suscripciones con base de datos.

## Tecnologías utilizadas

### Frontend:
* **React**: Para la construcción de interfaces de usuario.
* **TailwindCSS**: Framework CSS para diseño responsivo y rápido.
* **React Router**: Para la navegación entre páginas.
* **Axios**: Para realizar peticiones HTTP al backend.
* **TypeScript**: Para proporcionar seguridad de tipo y escalabilidad.

### Backend:
* **Python**: Para la ejecución del servidor.
* **FastAPI**: Framework para construir la API RESTful.
* **JWT (JSON Web Tokens)**: Para la autenticación y manejo de sesiones.
* **SQLALCHEMY**: ORM para interactuar con la base de datos (posiblemente MySQL o PostgreSQL).

## URLs de Producción

* **API**: `https://subscriptions-api.valver.site/docs` - Los usuarios pueden ver sus suscripciones, agregar nuevas suscripciones y cancelarlas.
* **Frontend**: `https://vermillion-tarsier-c30eeb.netlify.app/login` - Los usuarios pueden cerrar sesión, iniciar sesión y gestionar todas sus suscripciones a través de la interfaz web.




