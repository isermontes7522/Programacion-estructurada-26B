def cajero_automatico():
    # -------------------------------------------------------------
    # CONSTANTES (Umbrales y valores fijos)
    # -------------------------------------------------------------
    PIN_CORRECTO = 1234
    MULTIPLO_MONTO = 50
    LIMITE_DIARIO_MAX = 6000.0
    MAX_INTENTOS_PIN = 3

    # Estado inicial de la cuenta y cliente
    saldo_cuenta = 5000.0
    retirado_hoy = 2000.0  # Acumulado retirado en el día

    print("=== BIENVENIDO AL CAJERO AUTOMÁTICO ===")

    # -------------------------------------------------------------
    # 1. INICIALIZACIÓN Y CICLO DE PIN
    # -------------------------------------------------------------
    intentos = 1
    pin_valido = False

    while not pin_valido and intentos <= MAX_INTENTOS_PIN:
        try:
            pin_tecleado = int(input(f"\n[Intento {intentos}/{MAX_INTENTOS_PIN}] Ingrese su PIN: "))
        except ValueError:
            print(">> Entrada no válida. Debe ser un número.")
            continue

        if pin_tecleado == PIN_CORRECTO:
            pin_valido = True
        else:
            intentos += 1

    # -------------------------------------------------------------
    # 2. PROCESAMIENTO DE RETIRO Y VALIDACIONES
    # -------------------------------------------------------------
    # Variable de salida única
    mensaje_salida = ""

    if not pin_valido:
        mensaje_salida = "DENEGADO"
    else:
        print(f"\n¡ACCESO CONCEDIDO!")
        print(f"Saldo disponible actual: ${saldo_cuenta:.2f}")

        try:
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            monto = 0.0

        # Comprobación estricta en una sola cadena if / elif / else
        if monto % MULTIPLO_MONTO != 0 or monto <= 0:
            mensaje_salida = "MONTO NO VÁLIDO"
        elif monto > saldo_cuenta:
            mensaje_salida = "SALDO INSUFICIENTE"
        elif (retirado_hoy + monto) > LIMITE_DIARIO_MAX:
            mensaje_salida = "LÍMITE DIARIO EXCEDIDO"
        else:
            saldo_cuenta -= monto
            mensaje_salida = f"ENTREGADO\nSaldo restante: ${saldo_cuenta:.2f}"

    # -------------------------------------------------------------
    # 3. SALIDA ÚNICA
    # -------------------------------------------------------------
    print("\n-------------------------------------------------------------")
    print(mensaje_salida)
    print("-------------------------------------------------------------")


# Ejecutar programa
if __name__ == "__main__":
    cajero_automatico()
