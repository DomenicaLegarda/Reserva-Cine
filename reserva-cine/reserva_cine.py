# Crear la matriz de asientos: 3 filas y 4 columnas, todos inicializados en 0 (libres)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Mensaje de bienvenida al sistema
print("---- Sistema de Reserva de Cine ----")

# Solicitar al usuario los datos del asiento que desea reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Validar que los valores ingresados estén dentro del rango permitido
if 0 <= fila <= 2 and 0 <= columna <= 3:
    # Marcar el asiento como reservado (asignar valor 1)
    asientos[fila][columna] = 1
    # Confirmar al usuario que la reserva fue exitosa
    print(f"\nAsiento [{fila}][{columna}] reservado con éxito.")
else:
    # Informar al usuario si ingresó una posición incorrecta
    print("\nError: Posición de asiento no válida.")

# Mostrar el encabezado antes de imprimir la tabla de asientos
print("\nEstado de la sala:")

# Recorrer la matriz con bucles anidados para mostrarla en formato de tabla
# Bucle exterior: recorre cada fila
for i in range(3):
    # Bucle interior: recorre cada columna de la fila actual
    for j in range(4):
        # Imprimir el valor sin salto de línea (separado por espacios)
        print(asientos[i][j], end=" ")
    # Salto de línea al terminar de imprimir una fila completa
    print()