from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum

class EstadoTarea(str, Enum):
    pendiente = "Pendiente"
    en_ejecucion = "En ejecucion"
    realizado = "Realizado"
    cancelada = "Cancelada"

class EstadoUsuario(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    eliminado = "Eliminado"

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"  # Opcional, pero más riguroso
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, min_length=2, max_length=50)
    email: str = Field(index=True, min_length=2, max_length=50)
    estado: EstadoUsuario = Field(default=EstadoUsuario.activo)
    premiun: bool = Field(default=False)

class Tarea(SQLModel, table=True):
    __tablename__ = "tarea"  # Opcional
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(min_length=3, max_length=40)
    descripcion: str = Field(min_length=3, max_length=40)
    creacion: Optional[datetime] = Field(default_factory=datetime.now)
    modificacion: Optional[datetime] = Field(default=None)
    estado: EstadoTarea = Field(default=EstadoTarea.pendiente)
    usuario_id: int = Field(foreign_key="usuario.id")  # La tabla usuario, no la clase Usuario

