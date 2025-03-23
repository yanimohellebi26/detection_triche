from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import video

app = FastAPI(
    title="Système de Détection de Triche",
    description="Analyse les vidéos pour détecter des comportements suspects pendant un examen.",
    version="1.0.0"
)

# ✅ CORS pour autoriser les appels depuis le front React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React tourne ici
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Route API principale
app.include_router(video.router, prefix="/api/video", tags=["Analyse Vidéo"])

# ✅ Route de bienvenue
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de détection de triche"}
