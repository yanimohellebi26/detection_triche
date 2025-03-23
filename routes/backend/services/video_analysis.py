import cv2
import mediapipe as mp

# Initialisation de Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def analyze_video(file_path):
    """Analyse la vidéo et détecte les mouvements suspects."""
    
    cap = cv2.VideoCapture(file_path)
    
    if not cap.isOpened():
        return {"error": "Impossible d'ouvrir la vidéo"}

    frame_count = 0
    suspicious_movements = 0

    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # Fin de la vidéo

            frame_count += 1
            
            # Convertir en RGB pour Mediapipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(rgb_frame)

            # Vérifier si un visage est détecté
            if results.detections:
                for detection in results.detections:
                    # Dessiner les repères sur le visage
                    mp_drawing.draw_detection(frame, detection)

                    # Détecter les mouvements suspects (ex : regard qui bouge rapidement)
                    bbox = detection.location_data.relative_bounding_box
                    if bbox.width > 0.5:  # Si le visage est trop proche, possible triche
                        suspicious_movements += 1

    cap.release()

    return {
        "total_frames": frame_count,
        "suspicious_movements": suspicious_movements,
        "alert": suspicious_movements > 10  # Si plus de 10 mouvements suspects, alerte
    }
