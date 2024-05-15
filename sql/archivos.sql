CREATE TABLE Archivos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    extension TEXT NOT NULL,
    tamaño_KB INTEGER,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);