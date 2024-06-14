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
pasta_rostos = "frames-haar"

aplicar_haar(pasta_frames, pasta_rostos)

def frames_video(pasta_rostos, video_haar, fps=30):
    frames = [os.path.join(pasta_rostos, f) for f in sorted(os.listdir(pasta_rostos)) if f.endswith('.jpg')]

    frame = cv2.imread(frames[0])
    altura, largura, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_haar, fourcc, fps, (largura, altura))

    for frame_path in frames:
        frame = cv2.imread(frame_path)
        video_writer.write(frame)

    video_writer.release()
    print(f"Vídeo compilado com sucesso!")

video_haar = "video/video_haar.mp4"

frames_video(pasta_rostos, video_haar)