from pydantic import BaseModel, Field
from typing import Optional

#Clase principal Almuerzo
class Almuerzo(BaseModel):
    id: Optional [int] = None
    Nombres: str = Field(default="nombre", min_length=3, max_length= 20 )
    Apellidos: str = Field(default="apellido", min_length=3, max_length= 20 )
    Telefono: int = Field(default=0, ge= 0)
    Correo: str = Field(default="correo")
    Edad: int = Field(default= 0, gt = 0, le = 100 )
    Direccion: str = Field(default="direccion")
    ComidaEntregada: bool = False
    Observacion: str = Field(default="observacion")
