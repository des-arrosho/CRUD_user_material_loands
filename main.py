from fastapi import FastAPI
from routes.usersRoutes import user
from routes.materials import material_router
from routes.loands import loands_router

app = FastAPI(
    title="Prestamos Coppel Jesus Arroyo",
    description="API de prueba para registrar de prestamos Coopel"
)

app.include_router(user)
app.include_router(material_router)
app.include_router(loands_router)