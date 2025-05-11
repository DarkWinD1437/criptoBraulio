import time

def cifrado_serie_grupos(mensaje, tam_grupo, permutacion, relleno='X'):
    # Validaciones
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(tam_grupo, int) or tam_grupo <= 0:
        raise ValueError("El tamaño del grupo debe ser un entero positivo.")
    if not isinstance(permutacion, list):
        raise ValueError("La permutación debe ser una lista.")
    if sorted(permutacion) != list(range(len(permutacion))):
        raise ValueError("La permutación debe contener índices únicos desde 0 hasta n-1.")

    # Normalización: eliminar espacios y convertir a mayúsculas
    mensaje = mensaje.replace(" ", "").upper()

    # Relleno si es necesario
    if len(mensaje) % tam_grupo != 0:
        mensaje += relleno * (tam_grupo - (len(mensaje) % tam_grupo))

    # Dividir en grupos
    grupos = [mensaje[i:i + tam_grupo] for i in range(0, len(mensaje), tam_grupo)]

    # Asegurar que la permutación sea válida para el número de grupos
    if len(permutacion) > len(grupos):
        raise ValueError("La permutación no puede ser más larga que la cantidad de grupos.")

    # Reordenar los grupos según la permutación
    grupos_reordenados = [grupos[i] for i in permutacion]

    # Concatenar el resultado
    mensaje_cifrado = "".join(grupos_reordenados)

    return mensaje_cifrado

def descifrado_serie_grupos(mensaje_cifrado, tam_grupo, permutacion, relleno='X'):
    # Validaciones (similares a cifrado)
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(tam_grupo, int) or tam_grupo <= 0:
        raise ValueError("El tamaño del grupo debe ser un entero positivo.")
    if not isinstance(permutacion, list):
        raise ValueError("La permutación debe ser una lista.")
    if sorted(permutacion) != list(range(len(permutacion))):
        raise ValueError("La permutación debe contener índices únicos desde 0 hasta n-1.")

    # Normalización
    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()

    # Dividir en grupos
    grupos = [mensaje_cifrado[i:i + tam_grupo] for i in range(0, len(mensaje_cifrado), tam_grupo)]

    # Generar permutación inversa
    permutacion_inversa = [0] * len(permutacion)
    for i, pos in enumerate(permutacion):
        permutacion_inversa[pos] = i

    # Reordenar grupos según la permutación inversa
    grupos_descifrados = [grupos[i] for i in permutacion_inversa]

    # Concatenar y eliminar relleno
    mensaje_descifrado = "".join(grupos_descifrados).rstrip(relleno)

    return mensaje_descifrado

def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO DE TRANSPOSICIÓN POR SERIE DE GRUPOS  ".center(50))
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

                    tam_grupo = int(input("Tamaño de grupo (ej. 4): "))
                    permutacion = [int(x) for x in input("Permutación (ej. '1 0 2' para 3 grupos): ").split()]

                    resultado = cifrado_serie_grupos(mensaje, tam_grupo, permutacion)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    tam_grupo = int(input("Tamaño de grupo (ej. 4): "))
                    permutacion = [int(x) for x in input("Permutación (ej. '1 0 2' para 3 grupos): ").split()]

                    resultado = descifrado_serie_grupos(mensaje, tam_grupo, permutacion)
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