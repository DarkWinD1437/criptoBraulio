import time

def cifrado_afin(mensaje, a, b):
    # Validaciones
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Las claves a y b deben ser enteros.")
    if a <= 0 or b < 0:
        raise ValueError("Las claves deben ser positivas.")
    if mcd(a, 26) != 1:
        raise ValueError("La clave 'a' debe ser coprima con 26 (mcd(a,26)=1).")

    # Normalización: eliminar espacios y convertir a mayúsculas
    mensaje = mensaje.replace(" ", "").upper()
    mensaje_cifrado = ""

    for letra in mensaje:
        if letra.isalpha():
            x = ord(letra) - ord('A')
            y = (a * x + b) % 26
            mensaje_cifrado += chr(y + ord('A'))
        else:
            mensaje_cifrado += letra  # Conserva caracteres no alfabéticos

    return mensaje_cifrado

def descifrado_afin(mensaje_cifrado, a, b):
    # Validaciones
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Las claves a y b deben ser enteros.")
    if a <= 0 or b < 0:
        raise ValueError("Las claves deben ser positivas.")
    if mcd(a, 26) != 1:
        raise ValueError("La clave 'a' debe ser coprima con 26 (mcd(a,26)=1).")

    # Calcular inverso multiplicativo de 'a' módulo 26
    a_inv = inverso_modular(a, 26)
    mensaje_descifrado = ""

    for letra in mensaje_cifrado:
        if letra.isalpha():
            y = ord(letra) - ord('A')
            x = (a_inv * (y - b)) % 26
            mensaje_descifrado += chr(x + ord('A'))
        else:
            mensaje_descifrado += letra  # Conserva caracteres no alfabéticos

    return mensaje_descifrado

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverso_modular(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No existe inverso modular para {a} módulo {m}")

def main():
    while True:
        try:
            print("\n" + "=" * 50)
            print("  CIFRADO AFÍN POR SUSTITUCIÓN  ".center(50))
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

                    a = int(input("Clave 'a' (debe ser coprima con 26): "))
                    b = int(input("Clave 'b': "))

                    resultado = cifrado_afin(mensaje, a, b)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except ValueError as ve:
                    print(f"\n[!] Error: {ve}")

            elif opcion == "2":
                try:
                    print("\n" + "-" * 50)
                    mensaje = input("Mensaje cifrado: ").strip()
                    if not mensaje:
                        raise ValueError("El mensaje no puede estar vacío.")

                    a = int(input("Clave 'a' (debe ser coprima con 26): "))
                    b = int(input("Clave 'b': "))

                    resultado = descifrado_afin(mensaje, a, b)
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