from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.company_routes import router as company_router
from routes.application_routes import router as app_router

app = FastAPI()
app.include_router(user_router)
app.include_router(company_router)
app.include_router(app_router)