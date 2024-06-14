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