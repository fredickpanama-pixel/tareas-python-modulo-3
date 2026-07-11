


def cliente (**detalles_cliente):
    print("Cliente:")
    """ordena datos del cliente
           se analizan datos
           se ordenan"""
    for clave, valor in detalles_cliente.items():
        print(f"{clave.replace('_', ' ').title()} : {valor}")

def calcular_total(*args):
    """Calcula el total
           recibe cifras
           regresa un total sumando"""
    return sum(args)

def principal():
    detalles_cliente = {
        'nombre': 'Juan Pérez',
        'ciudad': 'La Paz',
        'metodo_de_pago': 'Tarjeta'
    }


    productos = [
        {'nombre': 'Laptop Lenovo', 'precio': 5200},
        {'nombre': 'Mouse Logitech', 'precio': 120},
        {'nombre': 'Monitor Samsung', 'precio': 1800},
        {'nombre': 'Teclado Mecánico', 'precio': 850},
        {'nombre': 'Webcam HD', 'precio': 300}
    ]



    precios = list(map(lambda p: p['precio'], productos))
    total_general = calcular_total(*precios)


   #filtra y eligeblos productos mayores a mil bol
    productos_mayores_mil = list(filter(lambda p: p['precio'] > 1000, productos))


    productos_clasificados = sorted(productos, key=lambda x: x['precio'])


    producto_mas_caro = max(productos, key=lambda x: x['precio'])
    producto_mas_barato = min(productos, key=lambda x: x['precio'])


    precio_promedio = total_general / len(productos) if productos else 0


    print("\n==============================")
    print("        RESUMEN DE COMPRA")
    print("==============================\n")

    cliente(**detalles_cliente)

    print("\nProductos adquiridos:")
    for p in productos:
        print(f"{p['nombre']}      Bs {p['precio']}")

    print(f"\nTotal: Bs {total_general}")
    print(f"\nPromedio: Bs {precio_promedio:.2f}")

    print("\nProducto más caro:")
    print(producto_mas_caro['nombre'])

    print("\nProducto más barato: ")
    print(producto_mas_barato['nombre'])

    print("\nProductos mayores a Bs1000")
    print("--------------------------")
    for p in productos_mayores_mil:
        print(p['nombre'])

    print("\nProductos ordenados")
    print("-------------------")
    for p in productos_clasificados:
        print(p['nombre'])


principal()