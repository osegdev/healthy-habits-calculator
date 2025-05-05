# Imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install pip-tools && \
    pip-compile requirements.in -o requirements.txt && \
    pip-compile dev-requirements.in -o dev-requirements.txt && \
    pip install -r requirements.txt -r dev-requirements.txt

# Comando por defecto al correr el contenedor
CMD ["python", "main.py"]