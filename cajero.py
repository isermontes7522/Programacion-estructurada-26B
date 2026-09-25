# Constantes de configuración
MULTIPLO_MONTO = 50
LIMITE_DIARIO_MAX = 6000

# Datos de la cuenta (puedes cambiar estos valores iniciales)
saldo = 10000.00
retirado_hoy = 0.00

# Captura de datos del usuario
try:
    monto = float(input("Ingrese el monto a retirar: "))

    # Validación de condiciones en orden secuencial
    if monto % MULTIPLO_MONTO != 0:
        resultado = "MONTO NO VÁLIDO"
    elif monto > saldo:
        resultado = "SALDO INSUFICIENTE"
    elif retirado_hoy + monto > LIMITE_DIARIO_MAX:
        resultado = "LÍMITE DIARIO EXCEDIDO"
    else:
        saldo -= monto
        resultado = f"ENTREGADO. Nuevo saldo: ${saldo:.2f}"

except ValueError:
    resultado = "MONTO NO VÁLIDO"

# Salida única en pantalla
print(resultado)
