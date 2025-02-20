from datetime import timedelta
import whisper
import os
from dotenv import load_dotenv

env = load_dotenv()
if env:
    print("enviroment loaded", env)
# folder videos
media_path = "media/media/"
model = whisper.load_model(os.getenv("MODEL_NAME"))


def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    # return result["text"]
    return result["segments"]


def create_srt_file(segments, filename="output"):

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        # segment = f"{segmentId}\n{
        #     startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
        segment = (
            f"{segmentId}\n"
            f"{startTime} --> {endTime}\n"
            f"{text[1:] if text[0] == ' ' else text}\n\n"
        )
        srtFilename = os.path.join("media", "SrtFiles", f"{filename}.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)


def main():
    # lista de archivos en la carpeta media
    archivos = os.listdir(media_path)
    print(archivos)

    for archivo in archivos:
        path = media_path + archivo
        namefile = archivo.split(".")[0]
        print(path)
        segments = transcribe_audio(path)
        create_srt_file(segments, namefile)
        print(f"------ finish {namefile}------\n")

    # model = whisper.load_model("base")

    # result = model.transcribe(media_path + archivos[0])
    # print(result["text"])


if __name__ == '__main__':
    main()
