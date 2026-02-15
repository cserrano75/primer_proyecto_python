import sqlite3

def inicializar_db():
    # Se conecta al archivo 'historial.db' (lo crea si no existe)
    conexion = sqlite3.connect('historial.db')
    cursor = conexion.cursor()
    
    # Creamos la tabla (SQL puro, igual que en Java o VB6)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            precio REAL,
            descuento REAL,
            resultado REAL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conexion.commit()
    conexion.close()

def guardar_consulta(precio, descuento, resultado):
    conexion = sqlite3.connect('historial.db')
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO consultas (precio, descuento, resultado) VALUES (?, ?, ?)",
        (precio, descuento, resultado)
    )
    conexion.commit()
    conexion.close()