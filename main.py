from fastapi import FastAPI, Depends
from db_conexiones import get_session, crear_tablas
from models import Tarea
from Opetations import crear_tarea
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/tareas")
async def endpoint_crear_tarea(tarea_data: Tarea, session: AsyncSession = Depends(get_session)):
    nueva_tarea = Tarea(
        nombre=tarea_data.nombre,
        descripcion=tarea_data.descripcion,
        estado=tarea_data.estado,
        usuario_id=tarea_data.usuario_id,
        creacion=datetime.now(),   # Aquí el servidor genera la fecha
        modificacion=None
    )
    session.add(nueva_tarea)
    await session.commit()
    await session.refresh(nueva_tarea)
    return nueva_tarea
