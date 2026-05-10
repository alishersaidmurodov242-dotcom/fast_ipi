from fastapi import FastAPI
from .routers import posts, users, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
# ← models.Base.metadata.create_all(bind=engine)  O'CHIRILDI!

app = FastAPI(
    title="Blog API",
    description="FastAPI + PostgreSQL + JWT + Alembic + CORS",
    version="5.0.0"
)

origins = [
    "http://localhost:3000",      # React development
    "http://localhost:5173",      # Vite development
    "http://localhost:8080",      # Vue development
    "https://mening-saytim.com",  # Production frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list, # .env faylidan o'qilgan manzillar
    allow_credentials=True,       # Cookie va token uchun
    allow_methods=["*"],          # GET, POST, PUT, DELETE...
    allow_headers=["*"],   # Authorization, Content-Type...
)
# 

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {
        "xabar": "Blog API",
        "version": "5.0.0",
    }

# Health check — deploy platformalar uchun
@app.get("/health")
def health_check():
    return {"status": "ok"}