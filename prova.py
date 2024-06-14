import cv2
import os

def extraindo_frames(video, pasta_frames):
    video = cv2.VideoCapture("video/la-cabra.mp4")

    contador = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        nome_frames = os.path.join(pasta_frames, f"frame_{contador:04d}.jpg")
        cv2.imwrite(nome_frames, frame)
        contador += 1

    video.release()
    print(f"{contador} frames foram extraídos!")

caminho_video = "video/la-cabra.mp4"
pasta_frames = "frames-og"

extraindo_frames(caminho_video, pasta_frames)

import cv2
import os

def aplicar_haar(pasta_frames, pasta_rostos):
    haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    for nome_frames in os.listdir(pasta_frames):
        frame_path = os.path.join(pasta_frames, nome_frames)
        frame = cv2.imread(frame_path)

        if frame is None:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(25, 25))

        if len(faces) > 0:
            output_frame_path = os.path.join(pasta_rostos, nome_frames)
            cv2.imwrite(output_frame_path, frame)

    print("Detecção completa!")

pasta_frames = "frames-og"
pasta_rostos = "frames_haar"

aplicar_haar(pasta_frames, pasta_rostos)