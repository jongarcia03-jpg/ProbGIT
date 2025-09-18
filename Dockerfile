# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos al contenedor
COPY clima.py .
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el script
CMD ["python", "clima.py"]
