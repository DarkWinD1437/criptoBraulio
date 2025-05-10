import time

def obtener_orden_columnas(clave):
    # Creamos lista de tuplas (carácter, posición original, índice) para manejar repeticiones
    caracteres = [(char, i) for i, char in enumerate(clave)]
    # Ordenamos primero por carácter, luego por posición original
    caracteres_ordenados = sorted(caracteres, key=lambda x: (x[0], x[1]))
    # Extraemos las posiciones originales en el nuevo orden
    return [i for (char, i) in caracteres_ordenados]


def cifrado_transposicion_columnas(mensaje, clave, relleno='X'):
    # Validaciones
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(clave, str) or not clave.isalpha():
        raise ValueError("La clave debe ser una palabra alfabética.")

    # Normalización
    mensaje = mensaje.replace(" ", "").upper()
    clave = clave.upper()

    # Obtener orden de columnas
    orden_columnas = obtener_orden_columnas(clave)
    num_columnas = len(orden_columnas)

    # Calcular relleno necesario
    len_mensaje = len(mensaje)
    faltante = (num_columnas - (len_mensaje % num_columnas)) % num_columnas
    mensaje_relleno = mensaje + relleno * faltante if faltante > 0 else mensaje

    # Crear matriz de columnas
    matriz = []
    for i in range(0, len(mensaje_relleno), num_columnas):
        fila = mensaje_relleno[i:i + num_columnas]
        matriz.append(fila)

    # Reordenar columnas según la clave
    matriz_ordenada = []
    for fila in matriz:
        fila_ordenada = [fila[i] for i in orden_columnas]
        matriz_ordenada.append(fila_ordenada)

    # Leer por columnas para obtener el texto cifrado
    texto_cifrado = []
    for i in range(num_columnas):
        for fila in matriz_ordenada:
            if i < len(fila):
                texto_cifrado.append(fila[i])

    return ''.join(texto_cifrado)


def descifrado_transposicion_columnas(mensaje_cifrado, clave, relleno='X'):
    # Validaciones
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(clave, str) or not clave.isalpha():
        raise ValueError("La clave debe ser una palabra alfabética.")

    # Normalización
    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()
    clave = clave.upper()

    # Obtener orden de columnas
    orden_columnas = obtener_orden_columnas(clave)
    num_columnas = len(orden_columnas)

    # Calcular número de filas
    len_cifrado = len(mensaje_cifrado)
    num_filas = len_cifrado // num_columnas
    if len_cifrado % num_columnas != 0:
        num_filas += 1

    # Reconstruir matriz cifrada
    matriz_cifrada = []
    for i in range(0, len_cifrado, num_filas):
        columna = mensaje_cifrado[i:i + num_filas]
        matriz_cifrada.append(columna)

    # Reordenar columnas a posición original
    matriz_original = [None] * num_columnas
    for pos_original, pos_cifrada in enumerate(orden_columnas):
        matriz_original[pos_cifrada] = matriz_cifrada[pos_original]

    # Reconstruir mensaje original
    mensaje_descifrado = []
    for i in range(num_filas):
        for j in range(num_columnas):
            if i < len(matriz_original[j]):
                mensaje_descifrado.append(matriz_original[j][i])

    # Eliminar relleno
    texto_descifrado = ''.join(mensaje_descifrado)
    if relleno:
        texto_descifrado = texto_descifrado.rstrip(relleno)

    return texto_descifrado


def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO DE TRANSPOSICIÓN POR COLUMNAS  ".center(50))
            print("=" * 50)
            print("\nOpciones:")
            print("1. Cifrar mensaje")
            print("2. Descifrar mensaje")
            print("3. Salir")

            opcion = input("\nSeleccione una opción (1-3): ").strip()

            if opcion == "1":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje a cifrar: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    clave = input("Clave (palabra): ").strip()
                    if not clave or not clave.isalpha():
                        raise ValueError("La clave debe ser una palabra alfabética.")

                    resultado = cifrado_transposicion_columnas(mensaje, clave)
                    len_mensaje = len(mensaje.replace(" ", ""))
                    num_columnas = len(clave)
                    faltante = (num_columnas - (len_mensaje % num_columnas)) % num_columnas

                    print(f"\n[✓] Mensaje cifrado: {resultado}")
                    if faltante > 0:
                        print(f"[i] Se añadieron {faltante} caracteres de relleno ('X')")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    clave = input("Clave original: ").strip()
                    if not clave or not clave.isalpha():
                        raise ValueError("La clave debe ser una palabra alfabética.")

                    resultado = descifrado_transposicion_columnas(mensaje, clave)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "3":
                print("\nSaliendo del programa...")
                time.sleep(1)
                break

            else:
                print("\n[!] Opción no válida. Intente nuevamente.")
                time.sleep(1)

        except KeyboardInterrupt:
            print("\n\n[!] Programa interrumpido por el usuario.")
            break

if __name__ == "__main__":
    main()