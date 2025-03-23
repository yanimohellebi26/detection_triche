from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np
from services.video_analysis import analyze_video

router = APIRouter()

@router.post("/analyze_video/")
async def analyze_video(file: UploadFile = File(...)):
    """Analyse une vidéo uploadée et retourne la détection de mouvement"""
    contents = await file.read()
    np_video = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(np_video, cv2.IMREAD_COLOR)

    if frame is None:
        return {"error": "Invalid video format"}

    processed_frame = analyze_video(frame)
    _, encoded_image = cv2.imencode(".jpg", processed_frame)
    
    return {"message": "Face detected", "image": encoded_image.tobytes()}
