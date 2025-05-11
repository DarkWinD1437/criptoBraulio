import time


def crear_matriz_playfair(clave):
    """
    Crea la matriz 5x5 para el cifrado Playfair.
    - Elimina letras duplicadas en la clave.
    - Combina I y J en la misma celda.
    - Rellena con el resto del alfabeto (sin J).
    """
    clave = clave.upper().replace(" ", "").replace("J", "I")
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Eliminar duplicados manteniendo el orden
    letras_unicas = []
    for letra in clave + alfabeto:
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    # Crear matriz 5x5
    matriz = [letras_unicas[i * 5:(i + 1) * 5] for i in range(5)]
    return matriz


def preparar_texto(texto):
    """
    Prepara el texto para el cifrado Playfair:
    - Elimina espacios y convierte a mayúsculas
    - Reemplaza J por I
    - Añade X entre letras duplicadas
    - Añade X si la longitud es impar
    """
    texto = texto.upper().replace(" ", "").replace("J", "I")
    texto_preparado = []

    i = 0
    while i < len(texto):
        # Si quedan dos letras o más
        if i == len(texto) - 1:
            texto_preparado.append(texto[i] + "X")
            break
        elif texto[i] == texto[i + 1]:
            texto_preparado.append(texto[i] + "X")
            i += 1
        else:
            texto_preparado.append(texto[i] + texto[i + 1])
            i += 2

    return texto_preparado


def encontrar_posicion(matriz, letra):
    """
    Encuentra la posición (fila, columna) de una letra en la matriz.
    """
    for fila in range(5):
        for col in range(5):
            if matriz[fila][col] == letra:
                return (fila, col)
    raise ValueError(f"Letra {letra} no encontrada en la matriz")


def cifrar_digrama(matriz, digrama):
    """
    Cifra un digrama usando las reglas de Playfair.
    """
    a, b = digrama[0], digrama[1]
    fila_a, col_a = encontrar_posicion(matriz, a)
    fila_b, col_b = encontrar_posicion(matriz, b)

    # Misma fila
    if fila_a == fila_b:
        return matriz[fila_a][(col_a + 1) % 5] + matriz[fila_b][(col_b + 1) % 5]

    # Misma columna
    elif col_a == col_b:
        return matriz[(fila_a + 1) % 5][col_a] + matriz[(fila_b + 1) % 5][col_b]

    # Rectángulo
    else:
        return matriz[fila_a][col_b] + matriz[fila_b][col_a]


def descifrar_digrama(matriz, digrama):
    """
    Descifra un digrama usando las reglas de Playfair.
    """
    a, b = digrama[0], digrama[1]
    fila_a, col_a = encontrar_posicion(matriz, a)
    fila_b, col_b = encontrar_posicion(matriz, b)

    # Misma fila
    if fila_a == fila_b:
        return matriz[fila_a][(col_a - 1) % 5] + matriz[fila_b][(col_b - 1) % 5]

    # Misma columna
    elif col_a == col_b:
        return matriz[(fila_a - 1) % 5][col_a] + matriz[(fila_b - 1) % 5][col_b]

    # Rectángulo
    else:
        return matriz[fila_a][col_b] + matriz[fila_b][col_a]


def cifrar_playfair(texto, clave):
    """
    Cifra un texto usando el cifrado Playfair.
    """
    matriz = crear_matriz_playfair(clave)
    digramas = preparar_texto(texto)
    texto_cifrado = []

    for digrama in digramas:
        texto_cifrado.append(cifrar_digrama(matriz, digrama))

    return " ".join(texto_cifrado)


def descifrar_playfair(texto_cifrado, clave):
    """
    Descifra un texto cifrado con Playfair.
    """
    matriz = crear_matriz_playfair(clave)
    texto_cifrado = texto_cifrado.replace(" ", "")
    digramas = [texto_cifrado[i:i + 2] for i in range(0, len(texto_cifrado), 2)]
    texto_descifrado = []

    for digrama in digramas:
        texto_descifrado.append(descifrar_digrama(matriz, digrama))

    # Eliminar X de relleno (excepto si es parte del mensaje original)
    resultado = "".join(texto_descifrado)
    if resultado[-1] == "X":
        resultado = resultado[:-1]
    resultado = resultado.replace("XX", "X")  # Para casos donde X era parte del mensaje

    return resultado


def mostrar_matriz(matriz):
    """
    Muestra la matriz Playfair de forma legible.
    """
    print("\nMatriz Playfair:")
    print("+" + "-" * 11 + "+")
    for fila in matriz:
        print("| " + " ".join(fila) + " |")
    print("+" + "-" * 11 + "+")


def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO PLAYFAIR  ".center(50))
            print("=" * 50)
            print("\nOpciones:")
            print("1. Cifrar mensaje")
            print("2. Descifrar mensaje")
            print("3. Mostrar matriz con una clave")
            print("4. Salir")

            opcion = input("\nSeleccione una opción (1-4): ").strip()

            if opcion == "1":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje a cifrar: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    clave = input("Clave: ").strip()
                    if not clave:
                        raise ValueError("La clave no puede estar vacía.")

                    resultado = cifrar_playfair(mensaje, clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    clave = input("Clave: ").strip()
                    if not clave:
                        raise ValueError("La clave no puede estar vacía.")

                    resultado = descifrar_playfair(mensaje, clave)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "3":
                try:
                    print("\n" + "-" * 50)
                    clave = input("Clave para generar matriz: ").strip()
                    if not clave:
                        raise ValueError("La clave no puede estar vacía.")

                    matriz = crear_matriz_playfair(clave)
                    mostrar_matriz(matriz)

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "4":
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