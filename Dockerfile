# Primera Etapa: Instalación de dependencias y construcción del entorno
FROM python:3.9.18-slim-bullseye AS builder

# Actualizamos el sistema
RUN apt-get update && apt-get upgrade -y \
    && apt install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copiamos el archivo de requisitos e instalamos las dependencias
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -U openai-whisper

# Segunda Etapa: Imagen final más ligera
FROM python:3.9.18-slim-bullseye

# Instalar solo ffmpeg en la imagen final
RUN apt-get update && apt-get upgrade -y \
    && apt install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Configuramos el directorio de trabajo
WORKDIR /usr/src/app

# Copiamos los paquetes instalados de la primera etapa
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

#COPY . .

# Punto de entrada de la imagen final
CMD [ "/bin/bash" ]

