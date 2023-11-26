from fastapi import FastAPI
from Routers.JornadaRouter import Router as Almuerzo_Router

app = FastAPI()

#Llamamos el Router que creamos para la clase main
app.include_router(Almuerzo_Router)
