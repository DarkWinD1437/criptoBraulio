import time

def cifrado_transposicion_series(mensaje, tam_serie, permutacion, relleno='X'):
    # Validación exhaustiva de argumentos
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(tam_serie, int) or tam_serie <= 0:
        raise ValueError("El tamaño de serie debe ser un entero positivo.")
    if not isinstance(permutacion, list) or len(permutacion) != tam_serie:
        raise ValueError("La permutación debe ser una lista con tamaño igual a tam_serie.")
    if sorted(permutacion) != list(range(tam_serie)):
        raise ValueError("La permutación debe contener todos los índices de 0 a tam_serie-1 sin repeticiones.")

    # Normalización: eliminar espacios y convertir a mayúsculas
    mensaje = mensaje.replace(" ", "").upper()

    # Aplicar relleno si es necesario
    faltante = (tam_serie - (len(mensaje) % tam_serie)) % tam_serie
    if faltante > 0:
        mensaje += relleno * faltante

    # Cifrado por series
    mensaje_cifrado = []
    for i in range(0, len(mensaje), tam_serie):
        serie = mensaje[i:i + tam_serie]
        serie_cifrada = [serie[j] for j in permutacion]
        mensaje_cifrado.extend(serie_cifrada)

    return ''.join(mensaje_cifrado)


def generar_permutacion_inversa(permutacion):
    """Genera la permutación inversa para descifrar"""
    return [permutacion.index(i) for i in range(len(permutacion))]


def descifrado_transposicion_series(mensaje_cifrado, tam_serie, permutacion, relleno='X'):
    # Validaciones
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(tam_serie, int) or tam_serie <= 0:
        raise ValueError("El tamaño de serie debe ser un entero positivo.")
    if not isinstance(permutacion, list) or len(permutacion) != tam_serie:
        raise ValueError("La permutación debe ser una lista con tamaño igual a tam_serie.")
    if sorted(permutacion) != list(range(tam_serie)):
        raise ValueError("La permutación debe contener todos los índices de 0 a tam_serie-1 sin repeticiones.")

    # Normalización del mensaje
    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()

    # Generar permutación inversa
    permutacion_inversa = generar_permutacion_inversa(permutacion)

    # Descifrar cada serie
    mensaje_descifrado = []
    for i in range(0, len(mensaje_cifrado), tam_serie):
        serie = mensaje_cifrado[i:i + tam_serie]
        serie_descifrada = [serie[permutacion_inversa[j]] for j in range(tam_serie)]
        mensaje_descifrado.extend(serie_descifrada)

    # Eliminar caracteres de relleno
    mensaje_descifrado = ''.join(mensaje_descifrado)
    if relleno:
        mensaje_descifrado = mensaje_descifrado.rstrip(relleno)

    return mensaje_descifrado


def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO DE TRANSPOSICIÓN POR SERIES  ".center(50))
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

                    tam_serie = int(input("Tamaño de serie (ej. 3): "))
                    permutacion = [int(x) for x in input("Permutación (ej. '2 0 1' para tamaño 3): ").split()]

                    resultado = cifrado_transposicion_series(mensaje, tam_serie, permutacion)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    tam_serie = int(input("Tamaño de serie original (ej. 3): "))
                    permutacion = [int(x) for x in input("Permutación original (ej. '2 0 1'): ").split()]

                    resultado = descifrado_transposicion_series(mensaje, tam_serie, permutacion)
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