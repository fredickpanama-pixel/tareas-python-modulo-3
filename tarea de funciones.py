
ventas = [
    ("Laptop",5200),
    ("Mouse",120),
    ("Monitor",1800),
    ("Teclado",250),
    ("Tablet",2200)
]
def calcular_total(*precios):
  total = sum(precios)
  return total

def registrar_compra(**datos):
  print("Información de compra:")
  for clave, valor in datos.items():
    print(f" {clave.capitalize()}: {valor}")



precios_productos = map(lambda item: item[1], ventas)
total_venta = calcular_total(*precios_productos)
print(f"El total de la venta es: {total_venta}")


registrar_compra(
    nombre="Ana Pérez",
    ciudad="Madrid",
    metodo_pago="Tarjeta de Crédito",
    productos=["Laptop", "Monitor"],
    descuento=0.1
)
