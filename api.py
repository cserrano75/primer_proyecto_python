from flask import Flask, jsonify, request
from app import calcular_precio_final
from database import inicializar_db, guardar_consulta # Importamos lo nuevo

app = Flask(__name__)

# Al arrancar la App, nos aseguramos de que la DB esté lista
inicializar_db()

@app.route('/descuento', methods=['GET'])
def servicio_descuento():
    precio = request.args.get('precio', type=float)
    descuento = request.args.get('desc', type=float)

    if precio is None or descuento is None:
        return jsonify({"error": "Faltan parámetros"}), 400

    resultado = calcular_precio_final(precio, descuento)
    
    # --- LA MAGIA NUEVA ---
    # Guardamos en la base de datos antes de responder
    guardar_consulta(precio, descuento, resultado)
    # ----------------------

    return jsonify({
        "precio_original": precio,
        "descuento_aplicado": descuento,
        "precio_final": resultado,
        "mensaje": "¡Guardado en base de datos!"
    })

if __name__ == '__main__':
    app.run(debug=True)