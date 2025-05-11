#instalar la libreria numpy (pip install numpy)
import numpy as np
import time


def letra_a_numero(letra):
    """Convierte una letra a su equivalente numérico (A=0, B=1, ..., Z=25)"""
    return ord(letra.upper()) - ord('A')


def numero_a_letra(numero):
    """Convierte un número a su equivalente de letra (0=A, 1=B, ..., 25=Z)"""
    return chr(numero % 26 + ord('A'))


def validar_matriz_clave(matriz, tam_grupo):
    """Valida que la matriz clave sea válida para el cifrado de Hill"""
    if len(matriz) != tam_grupo or any(len(fila) != tam_grupo for fila in matriz):
        raise ValueError("La matriz clave debe ser cuadrada y coincidir con el tamaño de grupo")

    # Convertir a numpy array y verificar si es invertible módulo 26
    matriz_np = np.array(matriz)
    det = int(round(np.linalg.det(matriz_np)))
    if det == 0 or np.gcd(det, 26) != 1:
        raise ValueError("La matriz clave no es invertible módulo 26 (determinante debe ser coprimo con 26)")


def cifrado_hill(mensaje, tam_grupo, matriz_clave, relleno='X'):
    """Cifra un mensaje usando el cifrado de Hill"""
    # Validaciones
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(tam_grupo, int) or tam_grupo <= 0:
        raise ValueError("El tamaño del grupo debe ser un entero positivo.")

    # Validar matriz clave
    validar_matriz_clave(matriz_clave, tam_grupo)
    matriz_np = np.array(matriz_clave)

    # Normalización: eliminar espacios y convertir a mayúsculas
    mensaje = mensaje.replace(" ", "").upper()

    # Relleno si es necesario
    if len(mensaje) % tam_grupo != 0:
        mensaje += relleno * (tam_grupo - (len(mensaje) % tam_grupo))

    # Convertir mensaje a números
    numeros = [letra_a_numero(c) for c in mensaje]

    # Dividir en grupos
    grupos = [numeros[i:i + tam_grupo] for i in range(0, len(numeros), tam_grupo)]

    # Cifrar cada grupo
    cifrado = []
    for grupo in grupos:
        grupo_vector = np.array(grupo).reshape((tam_grupo, 1))
        cifrado_grupo = np.dot(matriz_np, grupo_vector) % 26
        cifrado.extend([numero_a_letra(num[0]) for num in cifrado_grupo])

    return ''.join(cifrado)


def descifrado_hill(mensaje_cifrado, tam_grupo, matriz_clave):
    """Descifra un mensaje cifrado con Hill"""
    # Validaciones
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(tam_grupo, int) or tam_grupo <= 0:
        raise ValueError("El tamaño del grupo debe ser un entero positivo.")

    # Validar matriz clave y calcular inversa módulo 26
    validar_matriz_clave(matriz_clave, tam_grupo)
    matriz_np = np.array(matriz_clave)

    # Calcular matriz inversa módulo 26
    det = int(round(np.linalg.det(matriz_np)))
    det_inv = pow(det, -1, 26)  # Inverso multiplicativo del determinante
    matriz_adj = np.round(det * np.linalg.inv(matriz_np)).astype(int) % 26
    matriz_inv = (det_inv * matriz_adj) % 26

    # Convertir mensaje a números
    numeros = [letra_a_numero(c) for c in mensaje_cifrado]

    # Dividir en grupos
    grupos = [numeros[i:i + tam_grupo] for i in range(0, len(numeros), tam_grupo)]

    # Descifrar cada grupo
    descifrado = []
    for grupo in grupos:
        grupo_vector = np.array(grupo).reshape((tam_grupo, 1))
        descifrado_grupo = np.dot(matriz_inv, grupo_vector) % 26
        descifrado.extend([numero_a_letra(num[0]) for num in descifrado_grupo])

    return ''.join(descifrado)


def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO DE HILL  ".center(50))
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

                    tam_grupo = int(input("Tamaño de grupo (ej. 2 para matriz 2x2): "))

                    print("\nIngrese la matriz clave fila por fila (valores separados por espacios):")
                    matriz_clave = []
                    for i in range(tam_grupo):
                        fila = [int(x) for x in input(f"Fila {i + 1}: ").split()]
                        matriz_clave.append(fila)

                    resultado = cifrado_hill(mensaje, tam_grupo, matriz_clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    tam_grupo = int(input("Tamaño de grupo (ej. 2 para matriz 2x2): "))

                    print("\nIngrese la matriz clave fila por fila (valores separados por espacios):")
                    matriz_clave = []
                    for i in range(tam_grupo):
                        fila = [int(x) for x in input(f"Fila {i + 1}: ").split()]
                        matriz_clave.append(fila)

                    resultado = descifrado_hill(mensaje, tam_grupo, matriz_clave)
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