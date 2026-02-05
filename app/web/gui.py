from fastapi import FastAPI

from app.web.routes import router

app = FastAPI(title="OpenManus GUI")
app.include_router(router)
