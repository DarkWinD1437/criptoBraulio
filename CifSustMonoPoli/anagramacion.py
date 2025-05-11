import time


def cifrado_vigenere(mensaje, clave):
    if not isinstance(mensaje, str) or not isinstance(clave, str):
        raise TypeError("El mensaje y la clave deben ser cadenas de texto.")
    if not mensaje:
        raise ValueError("El mensaje no puede estar vacío.")
    if not clave:
        raise ValueError("La clave no puede estar vacía.")

    mensaje = mensaje.replace(" ", "").upper()
    clave = clave.replace(" ", "").upper()

    clave_repetida = (clave * (len(mensaje) // len(clave) + 1))[:len(mensaje)]
    mensaje_cifrado = []

    for m, k in zip(mensaje, clave_repetida):
        if not m.isalpha():
            continue
        num_m = ord(m) - ord('A')
        num_k = ord(k) - ord('A')
        num_c = (num_m + num_k) % 26
        letra_c = chr(num_c + ord('A'))
        mensaje_cifrado.append(letra_c)

    return ''.join(mensaje_cifrado)


def descifrado_vigenere(mensaje_cifrado, clave):
    if not isinstance(mensaje_cifrado, str) or not isinstance(clave, str):
        raise TypeError("El mensaje cifrado y la clave deben ser cadenas de texto.")
    if not mensaje_cifrado:
        raise ValueError("El mensaje cifrado no puede estar vacío.")
    if not clave:
        raise ValueError("La clave no puede estar vacía.")

    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()
    clave = clave.replace(" ", "").upper()

    clave_repetida = (clave * (len(mensaje_cifrado) // len(clave) + 1))[:len(mensaje_cifrado)]
    mensaje_descifrado = []

    for c, k in zip(mensaje_cifrado, clave_repetida):
        if not c.isalpha():
            continue
        num_c = ord(c) - ord('A')
        num_k = ord(k) - ord('A')
        num_m = (num_c - num_k) % 26
        letra_m = chr(num_m + ord('A'))
        mensaje_descifrado.append(letra_m)

    return ''.join(mensaje_descifrado)


def anagramar_por_columnas(texto, clave):
    clave = clave.upper()
    # Ordenar las letras de la clave y obtener índices originales
    clave_ordenada = sorted([(c, i) for i, c in enumerate(clave)], key=lambda x: x[0])
    indices_ordenados = [i for c, i in clave_ordenada]

    num_columnas = len(clave)
    # Rellenar con X si es necesario
    texto = texto.ljust(len(texto) + (num_columnas - len(texto) % num_columnas), 'X')

    # Dividir en filas
    filas = [texto[i:i + num_columnas] for i in range(0, len(texto), num_columnas)]

    # Leer por columnas en el orden determinado
    texto_anagramado = []
    for i in indices_ordenados:
        for fila in filas:
            if i < len(fila):
                texto_anagramado.append(fila[i])

    return ''.join(texto_anagramado)


def desanagramar_por_columnas(texto, clave):
    clave = clave.upper()
    # Recrear el mismo orden usado en cifrado
    clave_ordenada = sorted([(c, i) for i, c in enumerate(clave)], key=lambda x: x[0])
    indices_ordenados = [i for c, i in clave_ordenada]

    num_columnas = len(clave)
    if len(texto) % num_columnas != 0:
        raise ValueError("La longitud del texto no es divisible por el número de columnas")

    num_filas = len(texto) // num_columnas

    # Reconstruir matriz original
    matriz = [[None for _ in range(num_columnas)] for _ in range(num_filas)]

    # Llenar columnas en el orden original
    col_actual = 0
    for i in indices_ordenados:
        for fila in range(num_filas):
            if col_actual * num_filas + fila < len(texto):
                matriz[fila][i] = texto[col_actual * num_filas + fila]
        col_actual += 1

    # Leer por filas
    texto_original = ''.join([''.join(fila) for fila in matriz])
    return texto_original.rstrip('X')

#libreria necesaria para generar una cifra interna la cual usar para encriptar y desencriptar
import random

def anagramar_por_cifras(texto, cifra):
    # Convertir la cifra en una semilla reproducible
    random.seed(cifra)
    # Crear lista de índices
    indices = list(range(len(texto)))
    # Mezclar los índices usando la semilla
    random.shuffle(indices)
    # Reordenar el texto según los índices mezclados
    texto_anagramado = [texto[i] for i in indices]
    return ''.join(texto_anagramado), indices

def desanagramar_por_cifras(texto, cifra, indices_originales):
    # Revertir el proceso usando los índices originales
    texto_original = [None] * len(texto)
    for pos_actual, pos_original in enumerate(indices_originales):
        texto_original[pos_original] = texto[pos_actual]
    return ''.join(texto_original)


def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO VIGENÈRE CON ANAGRAMACIÓN  ".center(50))
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
                    clave_vigenere = input("Clave para Vigenère: ").strip()
                    if not clave_vigenere:
                        raise ValueError("La clave no puede estar vacía.")

                    print("\nMétodo de anagramación:")
                    print("1. Por columnas")
                    print("2. Por cifras")
                    print("3. Sin anagramación")
                    opcion_anagramacion = input("Seleccione (1-3): ").strip()

                    resultado = cifrado_vigenere(mensaje, clave_vigenere)

                    if opcion_anagramacion == "1":
                        clave_anagramacion = input("Clave para anagramación por columnas: ").strip()
                        if not clave_anagramacion:
                            raise ValueError("La clave de anagramación no puede estar vacía.")
                        resultado = anagramar_por_columnas(resultado, clave_anagramacion)
                        print(f"\n[✓] Mensaje cifrado (Vigenère + Columnas): {resultado}")
                    elif opcion_anagramacion == "2":
                        cifra = int(input("Ingrese número para anagramación por cifras: "))
                        resultado, indices = anagramar_por_cifras(resultado, cifra)
                        print(f"\n[✓] Mensaje cifrado (Vigenère + Cifras): {resultado}")
                        print(f"[!] Guarde este número para descifrar: {cifra}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":  # Descifrar

                try:
                    print("\n" + "-" * 50)
                    mensaje_cifrado = input("Mensaje cifrado: ").strip().upper()
                    if not mensaje_cifrado:
                        raise ValueError("El mensaje no puede estar vacío.")
                    # PRIMERO preguntar por anagramación
                    print("\n¿Qué método de anagramación se usó?")
                    print("1. Por columnas")
                    print("2. Por cifras")
                    print("3. No se usó anagramación")
                    opcion_anagramacion = input("Seleccione (1-3): ").strip()
                    # SEGUNDO: Manejar cada caso
                    if opcion_anagramacion == "1":
                        clave_anagramacion = input("Clave para desanagramación por columnas: ").strip().upper()
                        if not clave_anagramacion:
                            raise ValueError("La clave de anagramación no puede estar vacía.")
                        # TERCERO: Pedir clave Vigenère
                        clave_vigenere = input("Clave para Vigenère: ").strip().upper()
                        if not clave_vigenere:
                            raise ValueError("La clave no puede estar vacía.")
                         # Primero desanagramar, luego descifrar
                        mensaje_desanagramado = desanagramar_por_columnas(mensaje_cifrado, clave_anagramacion)
                        mensaje_descifrado = descifrado_vigenere(mensaje_desanagramado, clave_vigenere)
                        print(f"\n[✓] Mensaje descifrado (Columnas + Vigenère): {mensaje_descifrado}")

                    elif opcion_anagramacion == "2":
                        cifra = int(input("Ingrese el número usado en el cifrado: "))
                        clave_vigenere = input("Clave para Vigenère: ").strip().upper()
                        # Primero desanagramar (necesitamos regenerar los índices)
                        random.seed(cifra)
                        indices = list(range(len(mensaje_cifrado)))
                        random.shuffle(indices)
                        mensaje_desanagramado = desanagramar_por_cifras(mensaje_cifrado, cifra, indices)
                        # Luego descifrar Vigenère
                        mensaje_descifrado = descifrado_vigenere(mensaje_desanagramado, clave_vigenere)
                        print(f"\n[✓] Mensaje descifrado (Cifras + Vigenère): {mensaje_descifrado}")

                    else:
                        # Solo descifrar Vigenère
                        clave_vigenere = input("Clave para Vigenère: ").strip().upper()
                        if not clave_vigenere:
                            raise ValueError("La clave no puede estar vacía.")
                        mensaje_descifrado = descifrado_vigenere(mensaje_cifrado, clave_vigenere)
                        print(f"\n[✓] Mensaje descifrado (solo Vigenère): {mensaje_descifrado}")

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