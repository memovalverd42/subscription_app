FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc netcat-openbsd && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# NUEVO: Copiar el script entrypoint.sh
COPY ./entrypoint.sh .
# NUEVO: Cambiar los saltos de línea de Windows a Unix (por si se está ejecutando en Windows)
RUN sed -i 's/\r$//g'  ./entrypoint.sh
# NUEVO: Dar permisos de ejecución al script
RUN chmod +x ./entrypoint.sh && ls -l ./entrypoint.sh

COPY . .

# NUEVO: Ejecutar el script entrypoint.sh al iniciar el contenedor
ENTRYPOINT ["bash", "./entrypoint.sh"]