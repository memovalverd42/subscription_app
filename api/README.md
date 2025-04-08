# API de Gestión de Suscripciones

Esta API proporciona los servicios backend para la gestión de suscripciones de usuarios. Está desarrollada con **FastAPI** y utiliza **PostgreSQL** como base de datos con **SQLAlchemy** como ORM.

## Tecnologías Utilizadas

* **Python**: Lenguaje de programación principal
* **FastAPI**: Framework web de alto rendimiento para crear APIs
* **PostgreSQL**: Sistema de gestión de bases de datos relacional
* **SQLAlchemy**: ORM (Object Relational Mapper) para Python
* **Pydantic**: Validación de datos y configuración de settings
* **JWT**: JSON Web Tokens para autenticación
* **Alembic**: Para migraciones de base de datos

## Requisitos

* Python 3.12+
* PostgreSQL 12+
* pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/memovalverd42/subscription_app
cd subscription_app
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno en un archivo `.env`:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_db
SECRET_KEY=tu_clave_secreta_para_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Ejecuta las migraciones:

```bash
alembic upgrade head
```

6. Inicia el servidor:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`.

## Endpoints de la API

### Autenticación

* **POST** `/users`: Registra un nuevo usuario
  * Body: `{ "email": "usuario@ejemplo.com", "password": "contraseña", "first_name": "Nombre", "last_name": "Apellido" }`

* **POST** `/users/login`: Inicia sesión de usuario
  * Body: `{ "email": "usuario@ejemplo.com", "password": "contraseña" }`
  * Retorna: Token JWT

### Suscripciones

* **GET** `/subscriptions`: Lista todas las suscripciones del usuario actual
  * Headers: `Authorization: Bearer {token}`

* **POST** `/subscriptions/subscribe`: Crea una nueva suscripción
  * Headers: `Authorization: Bearer {token}`
  * Body: `{ "plan": "premium", "period": "monthly" }`

* **PUT** `/subscriptions/cancel`: Obtiene detalles de una suscripción específica
  * Headers: `Authorization: Bearer {token}`

## Autenticación y Seguridad

La API utiliza JWT (JSON Web Tokens) para la autenticación. Cada solicitud a endpoints protegidos debe incluir un token válido en el encabezado `Authorization`.

Las contraseñas se almacenan hasheadas utilizando algoritmos seguros.

## Documentación de la API

FastAPI genera automáticamente documentación interactiva:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Despliegue

### Docker

Se incluye un Dockerfile y docker-compose.yml para facilitar el despliegue:

```bash
docker-compose up -d
```
