from fastapi import FastAPI
from fastapi.params import Depends

from db_conexiones import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from models import tarea
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/tareas")
async def crear_nueva_tarea(tarea_data: tarea, session:AsyncSession = Depends(get_session)):
    session.add(tarea_data)
    await session.commit()
    await session.refresh(tarea_data)
    return tarea_data