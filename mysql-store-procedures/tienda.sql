-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

-- Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100)
);

-- Tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    stock INT,
    precio DECIMAL(10,2)
);

-- Tabla de pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    cantidad INT,
    total DECIMAL(10,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Tabla de auditoría
CREATE TABLE IF NOT EXISTS auditoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Procedimiento para insertar cliente
DELIMITER //
CREATE PROCEDURE InsertarCliente(IN nombre VARCHAR(100), IN correo VARCHAR(100))
BEGIN
    INSERT INTO clientes(nombre, correo) VALUES(nombre, correo);
END //
DELIMITER ;

-- Procedimiento para realizar venta con validación de stock
DELIMITER //
CREATE PROCEDURE RealizarVenta(
    IN p_cliente_id INT,
    IN p_producto_id INT,
    IN p_cantidad INT
)
BEGIN
    DECLARE p_precio DECIMAL(10,2);
    DECLARE p_stock INT;

    START TRANSACTION;
    SELECT stock, precio INTO p_stock, p_precio FROM productos WHERE id = p_producto_id FOR UPDATE;

    IF p_stock >= p_cantidad THEN
        UPDATE productos SET stock = stock - p_cantidad WHERE id = p_producto_id;
        INSERT INTO pedidos(cliente_id, producto_id, cantidad, total)
        VALUES(p_cliente_id, p_producto_id, p_cantidad, p_cantidad * p_precio);
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END //
DELIMITER ;

-- Trigger para registrar auditoría en eliminación de pedidos
DELIMITER //
CREATE TRIGGER AuditoriaBorradoPedido
AFTER DELETE ON pedidos
FOR EACH ROW
BEGIN
    INSERT INTO auditoria(pedido_id) VALUES(OLD.id);
END //
DELIMITER ;

-- Insertar productos de ejemplo
INSERT INTO productos (nombre, stock, precio) VALUES
('Bicicleta de montaña', 10, 1200.00),
('Bicicleta de ruta', 5, 1800.00),
('Cascos de ciclismo', 20, 150.00),
('Guantes MTB', 30, 45.00),
('Luces LED para bicicleta', 25, 60.00);