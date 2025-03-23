from fastapi import FastAPI
from backend.routes import video

app = FastAPI(title="Système de Détection de Triche",
              description="Analyse les vidéos pour détecter des comportements suspects pendant un examen.",
              version="1.0.0")

# Inclure la route vidéo
app.include_router(video.router, prefix="/api/video", tags=["Analyse Vidéo"])

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de détection de triche"}
