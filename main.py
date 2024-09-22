import whisper
import os

# folder videos
media_path = "media/"
# lista de archivos en la carpeta media
archivos = os.listdir(media_path)


model = whisper.load_model("base")


result = model.transcribe(media_path + archivos[0])
print("------ transcribe ------\n")
print(result["text"])
