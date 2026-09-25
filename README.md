def evaluar_triaje(temp: float, fc: float, sat: float) -> str:
    # D1: ¿sat < 90 O fc > 120?
    if sat < 90 or fc > 120:
        nivel = "ROJO"
    # D2: ¿temp >= 39.0?
    elif temp >= 39.0:
        nivel = "AMARILLO"
    else:
        nivel = "VERDE"

    return nivel


# Entrada de datos
try:
    temp = float(input("Ingrese temperatura: "))
    fc = float(input("Ingrese frecuencia cardíaca: "))
    sat = float(input("Ingrese saturación de oxígeno: "))

    # Evaluación y Salida (usando la variable 'nivel')
    resultado = evaluar_triaje(temp, fc, sat)
    print(f"\nNivel assigned: {resultado}")

except ValueError:
    print("Error: Ingrese únicamente números válidos.")
