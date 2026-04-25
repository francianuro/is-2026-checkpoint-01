CREATE TABLE IF NOT EXISTS miembros {
    id SERIAL PRIMARY KEY,
    nombre varchar(30) NOT NULL,
    apellido varchar(30) NOT NULL,
    legajo varchar(15) UNIQUE NOT NULL,
    feature TEXT,
    servicio TEXT,
    estado VARCHAR(20) DEFAULT 'activo'
};

INSERT INTO  miembros (nombre,apellido,legajo,feature,servicio,estado) VALUES
('Cesar Antonio','Huari', '32533', 'BBDD','integrante 4','activo')