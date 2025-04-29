from models import tarea
from sqlmodel import select
from typing import Optional
from db_conexiones import get_session

async def crear_tarea(nueva_tarea:tarea,session):
    session.add(nueva_tarea)
    await session.commit()
    await session.refresh(nueva_tarea)
    return nueva_tarea