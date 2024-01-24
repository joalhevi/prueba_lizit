from fastapi import FastAPI
from config.database import engine, Base
from middleware.error_handler import ErrorHandler
from routers.items import items_router

app = FastAPI()
app.title = 'prueba_lizit'
app.version = '0.0.1'
app.add_middleware(ErrorHandler)
app.include_router(items_router)

# inicializar base de datos
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Server ok"}
