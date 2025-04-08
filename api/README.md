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

* Python 3.8+
* PostgreSQL 12+
* pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/api-gestion-suscripciones.git
cd api-gestion-suscripciones
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

## Estructura del Proyecto

```
api/
├── alembic/
│   └── versions/
├── app/
│   ├── crud/
│   │   ├── user.py
│   │   └── subscription.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   └── subscription.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── subscription.py
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   └── subscriptions.py
│   │   └── api.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   └── main.py
├── tests/
├── .env
├── alembic.ini
└── requirements.txt
```

## Endpoints de la API

### Autenticación

* **POST** `/api/auth/register`: Registra un nuevo usuario
  * Body: `{ "email": "usuario@ejemplo.com", "password": "contraseña", "first_name": "Nombre", "last_name": "Apellido" }`

* **POST** `/api/auth/login`: Inicia sesión de usuario
  * Body: `{ "email": "usuario@ejemplo.com", "password": "contraseña" }`
  * Retorna: Token JWT

* **POST** `/api/auth/logout`: Cierra la sesión (invalida el token)
  * Headers: `Authorization: Bearer {token}`

### Usuarios

* **GET** `/api/users/me`: Obtiene información del usuario actual
  * Headers: `Authorization: Bearer {token}`

* **PUT** `/api/users/me`: Actualiza información del usuario actual
  * Headers: `Authorization: Bearer {token}`
  * Body: `{ "first_name": "Nombre", "last_name": "Apellido", "email": "usuario@ejemplo.com" }`

### Suscripciones

* **GET** `/api/subscriptions/`: Lista todas las suscripciones del usuario actual
  * Headers: `Authorization: Bearer {token}`

* **POST** `/api/subscriptions/`: Crea una nueva suscripción
  * Headers: `Authorization: Bearer {token}`
  * Body: `{ "plan": "premium", "period": "monthly" }`

* **GET** `/api/subscriptions/{subscription_id}`: Obtiene detalles de una suscripción específica
  * Headers: `Authorization: Bearer {token}`

* **DELETE** `/api/subscriptions/{subscription_id}`: Cancela una suscripción existente
  * Headers: `Authorization: Bearer {token}`

## Modelos de Base de Datos

### User
- id (UUID): Identificador único
- email (String): Correo electrónico (único)
- first_name (String): Nombre
- last_name (String): Apellido
- hashed_password (String): Contraseña hasheada
- is_active (Boolean): Indica si el usuario está activo
- created_at (DateTime): Fecha de creación
- updated_at (DateTime): Fecha de última actualización

### Subscription
- id (UUID): Identificador único
- user_id (UUID): Relación con el usuario
- plan (String): Tipo de plan (básico, premium, etc.)
- period (String): Periodo de cobro (mensual, anual)
- start_date (Date): Fecha de inicio
- end_date (Date): Fecha de finalización
- is_active (Boolean): Indica si la suscripción está activa
- created_at (DateTime): Fecha de creación
- updated_at (DateTime): Fecha de última actualización

## Esquemas (Pydantic)

Los esquemas definen la estructura de los datos para las solicitudes y respuestas API:

- UserBase: Esquema base con email, first_name y last_name
- UserCreate: Extiende UserBase con password
- User: Esquema completo del usuario para respuestas
- SubscriptionBase: Esquema base con plan y period
- SubscriptionCreate: Igual que SubscriptionBase
- Subscription: Esquema completo de suscripción para respuestas

## Autenticación y Seguridad

La API utiliza JWT (JSON Web Tokens) para la autenticación. Cada solicitud a endpoints protegidos debe incluir un token válido en el encabezado `Authorization`.

Las contraseñas se almacenan hasheadas utilizando algoritmos seguros.

## Testing

Para ejecutar los tests:

```bash
pytest
```

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
