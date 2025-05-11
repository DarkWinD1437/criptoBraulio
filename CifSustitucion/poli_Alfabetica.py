import time

def cifrado_vigenere(mensaje, clave):
    # Validaciones
    if not isinstance(mensaje, str) or not isinstance(clave, str):
        raise TypeError("El mensaje y la clave deben ser cadenas de texto.")
    if not mensaje:
        raise ValueError("El mensaje no puede estar vacío.")
    if not clave:
        raise ValueError("La clave no puede estar vacía.")

    # Normalización: eliminar espacios y convertir a mayúsculas
    mensaje = mensaje.replace(" ", "").upper()
    clave = clave.replace(" ", "").upper()

    # Repetir la clave para que coincida con la longitud del mensaje
    clave_repetida = (clave * (len(mensaje) // len(clave) + 1))[:len(mensaje)]

    # Cifrado letra por letra
    mensaje_cifrado = []
    for m, k in zip(mensaje, clave_repetida):
        if not m.isalpha():
            continue  # Ignorar caracteres no alfabéticos (opcional)
        # Convertir letras a valores numéricos (A=0, B=1, ..., Z=25)
        num_m = ord(m) - ord('A')
        num_k = ord(k) - ord('A')
        # Aplicar cifrado: (mensaje + clave) mod 26
        num_c = (num_m + num_k) % 26
        # Convertir de vuelta a letra
        letra_c = chr(num_c + ord('A'))
        mensaje_cifrado.append(letra_c)

    return ''.join(mensaje_cifrado)

def descifrado_vigenere(mensaje_cifrado, clave):
    # Validaciones (similares a cifrado)
    if not isinstance(mensaje_cifrado, str) or not isinstance(clave, str):
        raise TypeError("El mensaje cifrado y la clave deben ser cadenas de texto.")
    if not mensaje_cifrado:
        raise ValueError("El mensaje cifrado no puede estar vacío.")
    if not clave:
        raise ValueError("La clave no puede estar vacía.")

    # Normalización
    mensaje_cifrado = mensaje_cifrado.replace(" ", "").upper()
    clave = clave.replace(" ", "").upper()

    # Repetir la clave
    clave_repetida = (clave * (len(mensaje_cifrado) // len(clave) + 1))[:len(mensaje_cifrado)]

    # Descifrado letra por letra
    mensaje_descifrado = []
    for c, k in zip(mensaje_cifrado, clave_repetida):
        if not c.isalpha():
            continue  # Ignorar caracteres no alfabéticos (opcional)
        # Convertir letras a valores numéricos
        num_c = ord(c) - ord('A')
        num_k = ord(k) - ord('A')
        # Aplicar descifrado: (cifrado - clave) mod 26
        num_m = (num_c - num_k) % 26
        # Convertir de vuelta a letra
        letra_m = chr(num_m + ord('A'))
        mensaje_descifrado.append(letra_m)

    return ''.join(mensaje_descifrado)

def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO POLIALFABÉTICO DE VIGENÈRE  ".center(50))
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
                    clave = input("Clave: ").strip()
                    if not clave:
                        raise ValueError("La clave no puede estar vacía.")

                    resultado = cifrado_vigenere(mensaje, clave)
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

                    resultado = descifrado_vigenere(mensaje, clave)
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