CREATE DATABASE IF NOT EXISTS epik;
USE epik;

CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    profesor VARCHAR(100),
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT
);

-- Crear el usuario epik-user
CREATE USER IF NOT EXISTS 'epik-user'@'localhost' IDENTIFIED BY 'epik-pass';

-- permisos a la bd
GRANT ALL PRIVILEGES ON epik.* TO 'epik-user'@'localhost';

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;
