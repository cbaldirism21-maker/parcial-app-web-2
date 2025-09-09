def analizar_numeros(*args, **kwargs):
    pares = []
    impares = []

    for num in args:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    if kwargs.get('mostrar_pares', True):
        print("Pares:", pares)
        print("Cantidad de pares:", len(pares))

    if kwargs.get('mostrar_impares', True):
        print("Impares:", impares)
        print("Cantidad de impares:", len(impares))

# Ejemplo de uso:
analizar_numeros(1, 2, 3, 4, 5, 6, mostrar_pares=True, mostrar_impares=True)

