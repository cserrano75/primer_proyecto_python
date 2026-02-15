from flask import Flask, jsonify, request
# Importamos la función que ya habías escrito en app.py
from app import calcular_precio_final

app = Flask(__name__)

# Definimos la "Ruta" (Endpoint)
@app.route('/descuento', methods=['GET'])
def servicio_descuento():
    # Obtenemos los datos de la URL (ej: ?precio=100&desc=15)
    precio = request.args.get('precio', type=float)
    descuento = request.args.get('desc', type=float)

    if precio is None or descuento is None:
        return jsonify({"error": "Faltan parámetros precio o desc"}), 400

    resultado = calcular_precio_final(precio, descuento)
    
    # Devolvemos un JSON (el estándar moderno de comunicación)
    return jsonify({
        "precio_original": precio,
        "descuento_aplicado": descuento,
        "precio_final": resultado
    })

if __name__ == '__main__':
    # Iniciamos el servidor en el puerto 5000
    app.run(debug=True)