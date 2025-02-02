from fastapi import FastAPI
from routes.usersRoutes import user

app = FastAPI(
    title="Prestamos Amauri S.A de C.V",
    description="API de prueba para registrar de prestamo de material educativo"
)

app.include_router(user)