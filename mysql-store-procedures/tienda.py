import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='tu_password',
        database='tienda'
    )

def realizar_venta(cliente_id, producto_id, cantidad):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.callproc('RealizarVenta', (cliente_id, producto_id, cantidad))
        conn.commit()
        print("Venta procesada.")
    except Exception as e:
        print("Error en la venta:", e)
    finally:
        cursor.close()
        conn.close()

def insertar_cliente(nombre, email):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertarCliente', (nombre, email))
        conn.commit()
        print("Cliente Insertado.")
    except Exception as e:
        print("Error en la creación de cliente:", e)
    finally:
        cursor.close()
        conn.close()

insertar_cliente('Ana', 'ana@correo.com')
insertar_cliente('Juan', 'juan@correo.com')
insertar_cliente('Pedro', 'pedro@correo.com')
insertar_cliente('Pepe el toro', 'pepe@correo.com')

realizar_venta(123,321,10)