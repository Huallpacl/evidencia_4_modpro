-- Creación de la tabla color
CREATE TABLE color (
  id INT PRIMARY KEY, 
  nombre VARCHAR(20)
);

-- Creación de la tabla descripcion
CREATE TABLE descripcion (
  id INT PRIMARY KEY, 
  texto VARCHAR(200)
);

-- Creación de la tabla licuadoras con claves foráneas
CREATE TABLE licuadoras (
  id VARCHAR(25) PRIMARY KEY, 
  id_color INT DEFAULT NULL, 
  id_desc INT DEFAULT NULL, 
  vel_max INT,
  FOREIGN KEY (id_color) REFERENCES color(id),
  FOREIGN KEY (id_desc) REFERENCES descripcion(id)
);

-- Inserción de los colores
INSERT INTO color (id, nombre) 
VALUES 
  (1, 'azul'), 
  (2, 'rojo'), 
  (3, 'blanco'), 
  (4, 'plateado'), 
  (5, 'negro');

-- Inserción de las descripciones
INSERT INTO descripcion (id, texto) 
VALUES 
  (
    1, 'Modelo básico. Jarra de acrílico, disponible en 3 colores. 3 velocidades.'
  ), 
  (
    2, 'Modelo turbo. Jarra de acrílico, disponible en 2 colores. 4 velocidades.'
  ), 
  (
    3, 'Modelo deluxe. Jarra de vidrio. Disponible en 2 colores. 4 velocidades.'
  );

-- CARGA DE DATOS en la tabla licuadoras
INSERT INTO licuadoras (id, id_color, id_desc, vel_max) 
VALUES 
  ('Ak07', 1, 1, 3), 
  ('Ak08', 2, 1, 3), 
  ('Ak09', 3, 1, 3), 
  ('Ak17', 3, 2, 4), 
  ('Ak18', 5, 2, 4), 
  ('Ak27', 4, 3, 4), 
  ('Ak28', 5, 3, 4);

-- Consultas SELECT
-- 1. Seleccionar todas las licuadoras con su color y descripción
SELECT * 
FROM licuadoras;

-- 2. Seleccionar los nombres de los colores disponibles
SELECT nombre 
FROM color;

-- 3. Seleccionar las descripciones de los modelos de licuadoras
SELECT texto 
FROM descripcion;

-- 4. Seleccionar las licuadoras que tienen 4 velocidades
SELECT id, vel_max 
FROM licuadoras 
WHERE vel_max = 4;

-- 5. Seleccionar las licuadoras cuyo color es el 'negro'
SELECT id 
FROM licuadoras 
WHERE id_color = (SELECT id FROM color WHERE nombre = 'negro');
