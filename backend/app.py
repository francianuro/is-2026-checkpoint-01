import os from flask
import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError, ProgrammingError

app = Flask(__name__)

# Credenciales SIEMPRE desde variables de entorno
DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    raise ValueError("Faltan variables de entorno de la base de datos (.env)")

def get_db_connection(): return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/api/health", methods=["GET"])
def health():
    """Docker usa este endpoint para el HEALTHCHECK"""
    return jsonify({"status": "active", "service":
    "backend"})

@app.route("/api/team", methods=["GET"])
def get_team():
    """Devuelve la lista de integrantes leyendo la tabla
    members""" conn = None try:
        conn = get_db_connection() with conn.cursor() as
        cur:
            cur.execute("SELECT nombre, apellido, legajo,
            feature, servicio, estado FROM members ORDER BY
            id;") rows = cur.fetchall()

        team = [
            {
                "nombre": r[0],
                "apellido": r[1],
                "legajo": r[2], l
                "feature": r[3],
                "servicio": r[4],
                "estado": r[5]
            } for r in rows
        ] return jsonify(team) except OperationalError as
    e:
        return jsonify({"error": "Database connection
        failed", "details": str(e)}), 500
    except ProgrammingError as e: return jsonify({"error":
        "Query error", "details": str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.route("/api/info", methods=["GET"])
def info():
    """Metadata del servicio"""
    return jsonify({
        "service": "TeamBoard Backend",
        "version": "1.0.0",
        "stack": ["Python 3.12-slim", "Flask", "psycopg2",
        "PostgreSQL 16-alpine"],
        "port": 5000,
        "endpoints": ["/api/health", "/api/team", "/api/info"]
    })

# Soporte para ejecución local (Gunicorn ignora este bloque 
# en producción)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
