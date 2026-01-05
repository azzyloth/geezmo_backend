# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Geezmo Gadgets API")

# CORS config so your React frontend can connect
origins = ["http://localhost:3000"]  # React dev server

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Geezmo Gadgets API!"}

from app.db.database import engine
from app.models import product, user  # Import all models

# Create tables in DB
product.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)


from app.api.routes import router
app.include_router(router)

from app.api import auth
app.include_router(auth.router)