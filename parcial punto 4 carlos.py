try:
    saldo = int(input("Ingrese el saldo inicial: "))
    monto = int(input("Ingrese el monto a retirar: "))

    if monto < 0:
        print("Error: No se permiten valores negativos.")
    elif monto > saldo:
        print("Error: Fondos insuficientes.")
    elif monto < 10000 or monto % 1000 != 0:
        print("Error: Esta cifra no es válida. Solo se permiten montos de 10000 en adelante y múltiplos de 1000.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Saldo restante: {saldo}")

except ValueError:
    print("Error: Debe ingresar un número válido.")

