def calcular_impuesto(valor, impuesto=19):
    return valor + (valor * impuesto / 100)

total = 0

for i in range(3):
    precio = float(input(f"Ingrese el precio del producto {i+1}: "))
    total += calcular_impuesto(precio)

print(f"\nTotal a pagar con impuesto: {total:.2f}")