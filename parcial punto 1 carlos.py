# ejercicio 1
n = int(input("Ingresa un número entero positivo: "))

max_largo = 0
tabla_mas_larga = 0

for i in range(1, n + 1):
    print(f"\nTabla del {i}")
    largo = 0
    for j in range(1, i + 1):  # ahora cada tabla llega hasta i
        print(f"{i} x {j} = {i * j}")
        largo += 1
    if largo > max_largo:
        max_largo = largo
        tabla_mas_larga = i

print(f"\nLa tabla más larga generada fue la del {tabla_mas_larga} con {max_largo} elementos.")