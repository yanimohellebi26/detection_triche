# Détection de Triche Académique

Application de **détection de triche** dans les travaux académiques combinant analyse audio, vidéo et comportementale, avec une interface React.

## Fonctionnalités

- Détection de triche via analyse audio (`audio_analysis.py`, `audio_training.py`)
- Analyse vidéo comportementale (`video.py`, `video_analysis.py`)
- Interface web React + Vite
- Tests unitaires (Jest / `index.test.js`)

## Structure

```
├── main.py                  # Point d'entrée backend Python
├── audio.py                 # Capture et analyse audio
├── audio_analysis.py        # Modèle de détection audio
├── audio_training.py        # Entraînement modèle audio
├── video.py                 # Capture vidéo
├── video_analysis.py        # Analyse comportementale vidéo
├── preprocess.py            # Prétraitement des données
├── logger.py                # Logging des sessions
├── main.jsx / App.jsx       # Interface React
├── VideoUpload.jsx          # Composant upload vidéo
└── exploration.ipynb        # Notebook d'exploration
```

## Installation

```bash
# Backend Python
pip install -r requirements.txt   # (si présent)

# Frontend React
npm install
npm run dev
```

## Technologies

`Python` · `React` · `Vite` · `OpenCV` · Audio ML · Comportementale IA
