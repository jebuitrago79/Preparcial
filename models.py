from typing import  Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datatime import datetime
from enum import Enum
from pydantic import ConfigDict

class Estadotarea(str, Enum):
    pendiente = "Pendiente"
    en_ejecucion = "En ejecucion"
    realizado = "Realizado"
    cancelada = "Cancelada"

class EstadoUsuario(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    eliminado = "Eliminado"

class usuario(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, min_length=2, max_length=50)
    email: str = Field(index=True, min_length=2, max_length=50)
    estado: EstadoUsuario = Field(default=EstadoUsuario.activo)
    premiun: bool = Field(default=False)


class tarea(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre : str = Field(min_length=3, max_length=40)
    descripción: str =Field(min_length=3, max_length=40)
    creacion : Optional[datetime] = Field(default_factory=datetime.now)
    modificacion : Optional[datetime] = Field(default=None)
    estado: Estadotarea = Field(default=Estadotarea.pendiente)
    usuario_id : int = Field(foreign_key="usuario.id")



