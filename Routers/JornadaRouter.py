from fastapi import APIRouter
from Models.Jornada import Almuerzo
from fastapi.responses import RedirectResponse

#Creamos un Router para poder transportar los metodos a la clase Main
Router = APIRouter()



#Esta es la lista que usaremos para prueba de los medotos
Personas = [
{
  "id": 1,  
  "Nombres": "Josue",
  "Apellidos": "Navarro Peralta",
  "Telefono": 987654321,
  "Correo": "correo@example.com",
  "Edad": 20,
  "Direccion": "Santo Domingo, Rep. Dom",
  "ComidaEntregada": False,
  "Observacion": "No Comio"
},

{
  "id": 2,  
  "Nombres": "Ada",
  "Apellidos": "Matos",
  "Telefono": 123456789,
  "Correo": "correo2@example.com",
  "Edad": 19,
  "Direccion": "Santo Domingo, Rep. Dom",
  "ComidaEntregada": True,
  "Observacion": "Paso a recoger su comida media hora despues de la entrega"
},

{
  "id": 3,  
  "Nombres": "Carlos",
  "Apellidos": "Peralta",
  "Telefono": 127654321,
  "Correo": "correo123@example.com",
  "Edad": 10,
  "Direccion": "Santo Domingo, Rep. Dom",
  "ComidaEntregada": False,
  "Observacion": "No Comio"
}
]

@Router.get("/")
def redigir_docs():
    return RedirectResponse(url="/docs")


#Obtener Todas las Personas dentro de la LISTA
@Router.get("/Almuerzo")
def mostrar_Personas():
    return Personas

#Agregar Personas a la LISTA
@Router.post("/Almuerzo")
def insertar_Personas(almuerzo: Almuerzo):
    Personas.append(almuerzo)
    return Personas


#Editar Persona de la LISTA
@Router.put("/Almuerzo/{id}")
def Actualizar_Persona(id: int, almuerzo: Almuerzo):
    for index, item in enumerate(Personas):
        if item["id"] == id:
            almuerzo_dict = almuerzo.dict()
            Personas[index].update(almuerzo_dict)
            Personas[index]["Nombres"] = almuerzo.Nombres
            Personas[index]["Apellidos"] = almuerzo.Apellidos
            Personas[index]["Telefono"] = almuerzo.Telefono
            Personas[index]["Edad"] = almuerzo.Edad
            Personas[index]["Direccion"] = almuerzo.Direccion
            Personas[index]["ComidaEntregada"] = almuerzo.ComidaEntregada
            Personas[index]["Observacion"] = almuerzo.Observacion
    return  Personas

        

#Eliminar Personas de la LISTA
@Router.delete("/Almuerzo/{id}")
def Eliminar_Persona(id: int):
    for index, item in enumerate(Personas):
        if item["id"] == id:
            Personas.pop(index)
        return Personas
            
#Obtener persona por mayor
@Router.get("/Almuerzo/edad-Mayor")
def Obtener_Personasedad():
   personas_mayores_de_edad = [item for item in Personas if item["Edad"] >= 18]
   return personas_mayores_de_edad

#Obtener persona por menor
@Router.get("/Almuerzo/edad-Menor")
def Obtener_Personasedad():
   personas_Menores_de_edad = [item for item in Personas if item["Edad"] <= 18]
   return personas_Menores_de_edad

#Ordenar Personas Alfabeticamente
@Router.get("/Almuerzo/ordenar-por-nombre")
def obtener_personas_ordenadas_por_nombre():
    personas_ordenadas = sorted(Personas, key=lambda x: x["Nombres"])
    return personas_ordenadas

#Obtener persona por ID
@Router.get("/Almuerzo{id}")
def Obtener_PersonasId(id: int):
   return list(filter(lambda item: item['id'] == id, Personas))


#Obtener persona por Correo
@Router.get("/Almuerzo/{Correo}")
def Obtener_PersonasCorreo(Correo: str):
    return list(filter(lambda item: item['Correo'] == Correo, Personas))

#Obtener persona por su Nombre
@Router.get("/Almuerzo/nombre/{Nombres}")
def Obtener_PersonasNombre(Nombres: str):
    return list(filter(lambda item: item['Nombres'] == Nombres, Personas))