/* =====================================================
   SISTEMA: SISMARL-JAL
   Base de Datos: sis_marl_jal
   Motor: MySQL 8+
   Autor: Proyecto Académico Seguridad en Software
   ===================================================== */

DROP DATABASE IF EXISTS sis_marl_jal;
CREATE DATABASE sis_marl_jal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sis_marl_jal;

-- =====================================================
-- TABLA: roles
-- =====================================================

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT NOT NULL
);

INSERT INTO roles (nombre, descripcion) VALUES
('Administrador', 'Acceso total al sistema'),
('Supervisor', 'Supervisión operativa'),
('Operador', 'Operador de unidad logística');

-- =====================================================
-- TABLA: usuarios
-- =====================================================

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    intentos_fallidos INT DEFAULT 0,
    bloqueado BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

-- Usuarios iniciales (hash simulado)
INSERT INTO usuarios (nombre, correo, password_hash, rol_id) VALUES
('Administrador General', 'admin@sismarl.com', '$2b$12$hashsimuladoadmin', 1),
('Supervisor Zona Industrial', 'supervisor@sismarl.com', '$2b$12$hashsimuladosup', 2);

-- Generación de 18 operadores adicionales (20 usuarios totales)
INSERT INTO usuarios (nombre, correo, password_hash, rol_id)
SELECT 
    CONCAT('Operador ', n),
    CONCAT('operador', n, '@sismarl.com'),
    '$2b$12$hashsimuladooperador',
    3
FROM (
    SELECT 1 n UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
    UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
    UNION SELECT 11 UNION SELECT 12 UNION SELECT 13 UNION SELECT 14 UNION SELECT 15
    UNION SELECT 16 UNION SELECT 17 UNION SELECT 18
) numeros;

-- =====================================================
-- TABLA: vehiculos
-- =====================================================

CREATE TABLE vehiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(15) NOT NULL UNIQUE,
    modelo VARCHAR(100) NOT NULL,
    capacidad_kg INT NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 20 vehículos
INSERT INTO vehiculos (placa, modelo, capacidad_kg) VALUES
('JAL-1001','Freightliner M2',8000),
('JAL-1002','Kenworth T370',10000),
('JAL-1003','Isuzu NPR',5000),
('JAL-1004','Hino 500',12000),
('JAL-1005','International MV',9000),
('JAL-1006','Freightliner M2',8000),
('JAL-1007','Kenworth T370',10000),
('JAL-1008','Isuzu NPR',5000),
('JAL-1009','Hino 500',12000),
('JAL-1010','International MV',9000),
('JAL-1011','Freightliner M2',8000),
('JAL-1012','Kenworth T370',10000),
('JAL-1013','Isuzu NPR',5000),
('JAL-1014','Hino 500',12000),
('JAL-1015','International MV',9000),
('JAL-1016','Freightliner M2',8000),
('JAL-1017','Kenworth T370',10000),
('JAL-1018','Isuzu NPR',5000),
('JAL-1019','Hino 500',12000),
('JAL-1020','International MV',9000);

-- =====================================================
-- TABLA: rutas
-- =====================================================

CREATE TABLE rutas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origen VARCHAR(150) NOT NULL,
    destino VARCHAR(150) NOT NULL,
    distancia_km DECIMAL(6,2) NOT NULL,
    riesgo_estimado VARCHAR(20),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 20 rutas reales en ZMG
INSERT INTO rutas (origen, destino, distancia_km, riesgo_estimado) VALUES
('Zona Industrial Guadalajara','Tlaquepaque Centro',12.5,'BAJO'),
('El Salto Parque Industrial','Zapopan Centro',28.4,'MEDIO'),
('Periférico Sur','Tonalá Centro',18.2,'MEDIO'),
('Guadalajara Centro','Tlajomulco',35.1,'ALTO'),
('Zapopan Centro','El Salto',30.7,'MEDIO'),
('Tlaquepaque','Periférico Norte',22.0,'BAJO'),
('Zona Industrial','Colotlán Centro',210.5,'ALTO'),
('Zapopan','Puerto Vallarta',320.0,'ALTO'),
('Guadalajara','Lagos de Moreno',185.3,'MEDIO'),
('El Salto','Tonalá',19.7,'MEDIO'),
('Tlaquepaque','Tlajomulco',25.0,'MEDIO'),
('Periférico Norte','Zapopan Industrial',15.0,'BAJO'),
('Guadalajara Centro','Zapopan Andares',14.2,'BAJO'),
('Zona Industrial','Aeropuerto GDL',8.4,'MEDIO'),
('Aeropuerto GDL','Tlajomulco',20.0,'MEDIO'),
('Tonalá','Guadalajara Centro',17.3,'MEDIO'),
('Zapopan','Tlaquepaque',21.4,'MEDIO'),
('El Salto','Zona Industrial',9.8,'BAJO'),
('Periférico Sur','Zapopan',23.6,'MEDIO'),
('Tlajomulco','Puerto Vallarta',310.0,'ALTO');

-- =====================================================
-- TABLA: eventos
-- =====================================================

CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehiculo_id INT NOT NULL,
    ruta_id INT NOT NULL,
    tipo_evento VARCHAR(50) NOT NULL,
    descripcion TEXT,
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id),
    FOREIGN KEY (ruta_id) REFERENCES rutas(id)
);

-- 40 eventos operativos
INSERT INTO eventos (vehiculo_id, ruta_id, tipo_evento, descripcion)
SELECT 
    FLOOR(1 + (RAND()*20)),
    FLOOR(1 + (RAND()*20)),
    'INICIO_RUTA',
    'Inicio normal de operación'
FROM information_schema.tables
LIMIT 20;

INSERT INTO eventos (vehiculo_id, ruta_id, tipo_evento, descripcion)
SELECT 
    FLOOR(1 + (RAND()*20)),
    FLOOR(1 + (RAND()*20)),
    'DESVIACION',
    'Desviación detectada fuera de ruta'
FROM information_schema.tables
LIMIT 10;

INSERT INTO eventos (vehiculo_id, ruta_id, tipo_evento, descripcion)
SELECT 
    FLOOR(1 + (RAND()*20)),
    FLOOR(1 + (RAND()*20)),
    'FINALIZACION',
    'Ruta completada correctamente'
FROM information_schema.tables
LIMIT 10;

-- =====================================================
-- TABLA: logs_seguridad
-- =====================================================

CREATE TABLE logs_seguridad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    accion VARCHAR(100),
    ip_origen VARCHAR(45),
    descripcion TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- 20 logs de ejemplo
INSERT INTO logs_seguridad (usuario_id, accion, ip_origen, descripcion)
SELECT 
    FLOOR(1 + (RAND()*20)),
    'LOGIN_EXITOSO',
    CONCAT('192.168.1.', FLOOR(1 + (RAND()*100))),
    'Acceso correcto al sistema'
FROM information_schema.tables
LIMIT 10;

INSERT INTO logs_seguridad (usuario_id, accion, ip_origen, descripcion)
SELECT 
    FLOOR(1 + (RAND()*20)),
    'LOGIN_FALLIDO',
    CONCAT('192.168.1.', FLOOR(1 + (RAND()*100))),
    'Intento fallido de autenticación'
FROM information_schema.tables
LIMIT 10;
