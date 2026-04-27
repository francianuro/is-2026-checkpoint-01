# 1. Imagen slim con versión fija (buena práctica obligatoria)
FROM python:3.12.4-slim 
WORKDIR /app

# 2. Crear usuario no-root ants de copiar archivos (Buena práctica obligatoria)
RUN groupadd -r appuser && useradd -r -g appuser -s /bin/false appuser

# 3. Copiar requirements PRIMERO para aprovechar caché de 
# capas de Docker (Buena práctica obligatoria)
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar código de la aplicación con permisos
COPY --chown=appuser:appuser app.py .


# 5. Cambiar a usuario no-root para la ejecución 
USER appuser 

EXPOSE 5000

# Ejecutar con Gunicorn (production-ready) en el puerto 
# 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
