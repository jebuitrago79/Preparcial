from models import Tarea
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from typing import Optional

async def crear_tarea(nueva_tarea: Tarea, session: AsyncSession):
    session.add(nueva_tarea)
    await session.commit()
    await session.refresh(nueva_tarea)
    return nueva_tarea
