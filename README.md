# Jornada de Almuerzo Gratis API

## Resumen

La Jornada de Almuerzo Gratis API es una API REST desarrollada en Python con el framework FastAPI. Está diseñada para resolver el problema de llevar un conteo de las personas que reciben comida gratis.

La API cuenta con 7 métodos que ayudan en el manejo de datos y el conteo de personas, incluyendo funcionalidades CRUD, obtención de personas por ID, correo electrónico, nombre, y más. Estos métodos están listos para conectarse a una base de datos o frontend.

## Librerías y Frameworks

### Librerías

- **Pydantic:** Utilizado para definir modelos de datos que validan solicitudes y respuestas en las API.

- **Typing:** Mejora la legibilidad del código y proporciona información adicional sobre los tipos de datos.

### Frameworks

- **FastAPI:** Un moderno framework de Python utilizado para consumir APIs, conocido por su alto rendimiento.

## Pasos para Montar la Aplicación

### Windows

1. Tener instalado Python.
2. Utilizar Visual Studio Code o cualquier editor de código preferido.
3. Instalar FastAPI.
4. Instalar Uvicorn.

## Estructura del Proyecto

Jornada de almuerzo gratis/
├── pycache/
├── JornadaAlmuerzo-env/
├── Models/
│ ├── pycache/
│ └── Jornada.py
├── Routers/
│ ├── pycache/
│ ├── init.py
│ └── JornadaRouter.py
└── Main/

## URLs de Acciones

1. Clona el proyecto y ábrelo.
2. Verifica la instalación de FastAPI con el comando "pip show fastapi".
3. Verifica la instalación de Uvicorn con el comando "uvicorn --version".
4. Para ejecutar el proyecto, entra en tu carpeta virtual (`venv`) y escribe el comando: uvicorn main:app --reload
5. Copia la dirección proporcionada en la consola y pégala en tu navegador.
6. Para acceder a la documentación, agrega "/docs" a la dirección (por ejemplo, http://localhost:8000/docs).
