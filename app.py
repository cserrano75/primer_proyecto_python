def calcular_precio_final(precio, descuento):
    """Calcula el precio aplicando un porcentaje de descuento."""
    if descuento > 100 or descuento < 0:
        return "Error: Descuento no válido"
    
    ahorro = precio * (descuento / 100)
    return precio - ahorro

if __name__ == "__main__":
    print("--- Sistema de Descuentos ---")
    p = float(input("Precio del producto: "))
    d = float(input("Porcentaje de descuento: "))
    
    resultado = calcular_precio_final(p, d)
    print(f"El precio final es: ${resultado}")