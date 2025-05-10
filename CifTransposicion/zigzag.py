import time
import logging

logging.basicConfig(filename='transposicion_zigzag_errors.log', level=logging.ERROR)


def cifrado_zigzag(mensaje, rieles, relleno='X'):
    # Validación de argumentos
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(rieles, int) or rieles <= 1:
        raise ValueError("El número de rieles debe ser un entero mayor a 1.")

    mensaje = mensaje.replace(" ", "").upper()
    if not mensaje:
        raise ValueError("El mensaje no puede estar vacío después de eliminar espacios.")

    # Aplicar relleno si es necesario
    ciclo = 2 * (rieles - 1)
    faltante = (ciclo - (len(mensaje) % ciclo)) % ciclo
    mensaje += relleno * faltante

    # Crear una matriz para los rieles
    matriz = [[] for _ in range(rieles)]
    fila = 0
    direccion = 1  # 1 para abajo, -1 para arriba

    for letra in mensaje:
        matriz[fila].append(letra)
        fila += direccion
        if fila == 0 or fila == rieles - 1:
            direccion *= -1

    # Concatenar todos los rieles en orden
    mensaje_cifrado = ''.join([''.join(riil) for riil in matriz])
    return mensaje_cifrado


def descifrado_zigzag(mensaje_cifrado, rieles):
    # Validación de argumentos
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(rieles, int) or rieles <= 1:
        raise ValueError("El número de rieles debe ser un entero mayor a 1.")

    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()
    if not mensaje_cifrado:
        raise ValueError("El mensaje cifrado no puede estar vacío.")

    # Calcular la longitud de cada riel
    ciclo = 2 * (rieles - 1)
    longitud_total = len(mensaje_cifrado)
    q, r = divmod(longitud_total, ciclo)

    longitudes = [0] * rieles
    for i in range(rieles):
        if i == 0 or i == rieles - 1:
            longitudes[i] = q
        else:
            longitudes[i] = 2 * q
    for i in range(r):
        if i < rieles:
            longitudes[i] += 1
        else:
            longitudes[2 * (rieles - 1) - i] += 1

    # Extraer los rieles
    rieles_separados = []
    inicio = 0
    for l in longitudes:
        rieles_separados.append(mensaje_cifrado[inicio:inicio + l])
        inicio += l

    # Reconstruir el mensaje original
    mensaje_descifrado = []
    fila = 0
    direccion = 1
    indices = [0] * rieles

    for _ in range(len(mensaje_cifrado)):
        mensaje_descifrado.append(rieles_separados[fila][indices[fila]])
        indices[fila] += 1
        fila += direccion
        if fila == 0 or fila == rieles - 1:
            direccion *= -1

    return ''.join(mensaje_descifrado)


def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO DE TRANSPOSICIÓN ZIG-ZAG (RAIL FENCE)  ".center(50))
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

                    rieles = int(input("Número de rieles (ej. 3): "))
                    resultado = cifrado_zigzag(mensaje, rieles)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")
                except Exception as e:
                    logging.error(f"Error al cifrar: {str(e)}")
                    print("\n[!] Ocurrió un error inesperado. Verifique los datos.")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    rieles = int(input("Número de rieles original (ej. 3): "))
                    resultado = descifrado_zigzag(mensaje, rieles)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")
                except Exception as e:
                    logging.error(f"Error al descifrar: {str(e)}")
                    print("\n[!] Ocurrió un error inesperado. Verifique los datos.")

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
        except Exception as e:
            logging.critical(f"Error crítico: {str(e)}")
            print("\n[!] Error crítico. Consulte el archivo de logs.")
            break


if __name__ == "__main__":
    main()