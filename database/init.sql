CREATE TABLE IF NOT EXISTS members {
    id SERIAL PRIMARY KEY,
    nombre varchar(30) NOT NULL,
    apellido varchar(30) NOT NULL,
    legajo varchar(15) UNIQUE NOT NULL,
    feature TEXT,
    servicio TEXT,
    estado VARCHAR(20) DEFAULT 'activo'
};

INSERT INTO  miembros (nombre,apellido,legajo,feature,servicio,estado) VALUES
('Francina','Ruaro', '33278', 'feature01','coordinador/a del grupo','activo'),    
('Facundo','Pierrard', '31487', 'feature02','Frontend','activo'),        
('Ernesto Helvio','Ardenghi', '15446', 'feature03','Backend','activo'),    
('Cesar Antonio','Huari', '32533', 'feature04','Base de datos','activo')
