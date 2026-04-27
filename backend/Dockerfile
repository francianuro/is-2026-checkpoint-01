# 1. Imagen slim con versión fija (buena práctica obligatoria)
FROM python:3.12-slim 
WORKDIR /app

# 2. Copiar requirements PRIMERO para aprovechar caché de 
# capas de Docker (Buena práctica obligatoria)
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar código de la aplicación
COPY app.py .

# 4. Definir usuario no-root (Buena práctica obligatoria)
RUN groupadd -r appuser && \ 
    useradd -r -g appuser -s /bin/false appuser

# Asignar permisos y cambiar a usuario no-root
RUN chown -R appuser:appuser /app USER appuser 

EXPOSE 5000

# Ejecutar con Gunicorn (production-ready) en el puerto 
# 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
