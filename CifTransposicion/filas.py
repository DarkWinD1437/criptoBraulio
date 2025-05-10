import time

def generar_permutacion_desde_clave(clave):
    clave = clave.upper()
    # Creamos una lista de tuplas: (carácter, índice original) para ordenar
    caracteres_ordenados = sorted((char, idx) for idx, char in enumerate(clave))
    # Extraemos los índices originales en el orden alfabético
    permutacion = [idx for char, idx in caracteres_ordenados]
    return permutacion

def cifrado_transposicion_filas(mensaje, clave, relleno='X'):
    # Validación de argumentos
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(clave, str) or len(clave) == 0:
        raise ValueError("La clave debe ser una cadena no vacía.")

    # Normalización
    mensaje = mensaje.replace(" ", "").upper()
    clave = clave.upper()
    tam_grupo = len(clave)

    # Generar permutación desde la clave
    permutacion = generar_permutacion_desde_clave(clave)

    # Aplicar relleno si es necesario
    if len(mensaje) % tam_grupo != 0:
        mensaje += relleno * (tam_grupo - (len(mensaje) % tam_grupo))

    # Dividir en filas
    filas = [mensaje[i:i + tam_grupo] for i in range(0, len(mensaje), tam_grupo)]

    # Cifrar: leer columnas según la permutación
    mensaje_cifrado = []
    for fila in filas:
        for col_idx in permutacion:
            if col_idx < len(fila):
                mensaje_cifrado.append(fila[col_idx])
    return "".join(mensaje_cifrado)

def descifrado_transposicion_filas(mensaje_cifrado, clave, relleno='X'):
    # Validaciones
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(clave, str) or len(clave) == 0:
        raise ValueError("La clave debe ser una cadena no vacía.")

    # Normalización
    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()
    clave = clave.upper()
    tam_grupo = len(clave)

    # Generar permutación y su inversa
    permutacion = generar_permutacion_desde_clave(clave)
    permutacion_inversa = [permutacion.index(i) for i in range(tam_grupo)]

    # Dividir en grupos del tamaño de la clave
    grupos = [mensaje_cifrado[i:i + tam_grupo] for i in range(0, len(mensaje_cifrado), tam_grupo)]

    # Descifrar cada grupo
    mensaje_descifrado = []
    for grupo in grupos:
        # Reordenar las letras según la permutación inversa
        grupo_descifrado = [''] * tam_grupo
        for pos_original, pos_cifrada in enumerate(permutacion_inversa):
            if pos_cifrada < len(grupo):
                grupo_descifrado[pos_original] = grupo[pos_cifrada]
        mensaje_descifrado.extend(grupo_descifrado)

    # Unir y eliminar relleno
    return "".join(mensaje_descifrado).rstrip(relleno)

def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO DE TRANSPOSICIÓN POR FILAS (CLAVE)  ".center(50))
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
                    if not clave:
                        raise ValueError("La clave no puede estar vacía.")

                    resultado = cifrado_transposicion_filas(mensaje, clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    clave = input("Clave (palabra): ").strip()
                    if not clave:
                        raise ValueError("La clave no puede estar vacía.")

                    resultado = descifrado_transposicion_filas(mensaje, clave)
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