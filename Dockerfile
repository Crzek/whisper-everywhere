FROM python:3.9.18-slim-bullseye
RUN apt-get update && apt-get upgrade -y \
    && apt install -y ffmpeg

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install -U openai-whisper
RUN echo "Todo instalado"


CMD [ "/bin/bash" ]