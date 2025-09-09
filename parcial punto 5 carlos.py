
productos = []

while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            continue
        productos.append({"nombre": nombre, "precio": precio})
    except ValueError:
        print("Precio inválido. Debe ingresar un número.")


def total_productos(lista):
    return len(lista)

def precio_promedio(lista):
    if not lista:
        return 0
    total = sum(p["precio"] for p in lista)
    return total / len(lista)

def producto_mas_caro(lista):
    return max(lista, key=lambda x: x["precio"])

def producto_mas_barato(lista):
    return min(lista, key=lambda x: x["precio"])


print("\n--- REPORTE FINAL ---")
print(f"Total de productos: {total_productos(productos)}")
print(f"Precio promedio: {precio_promedio(productos):.2f}")

caro = producto_mas_caro(productos)
print(f"Producto más caro: {caro['nombre']} - ${caro['precio']:.2f}")

barato = producto_mas_barato(productos)
print(f"Producto más barato: {barato['nombre']} - ${barato['precio']:.2f}")


productos_ordenados = sorted(productos, key=lambda x: x["precio"], reverse=True)

print("\nProductos ordenados de mayor a menor precio:")
for p in productos_ordenados:
    print(f"{p['nombre']}: ${p['precio']:.2f}")

