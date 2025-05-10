import time
import logging

# Configuración básica de logging
logging.basicConfig(filename='cifrado_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validar_entradas(texto, clave, alfabeto_mixto):
    #Válida que las entradas sean correctas antes de procesarlas
    if not texto:
        raise ValueError("El texto no puede estar vacío.")
    if not clave:
        raise ValueError("La clave no puede estar vacía.")
    for char in clave:
        if char not in alfabeto_mixto:
            raise ValueError(f"La clave contiene el carácter '{char}' que no está en el alfabeto.")


def cifrado_cesar_clave(texto, clave, alfabeto_mixto):
    #Cifra el texto usando una palabra clave como desplazamiento variable.
    try:
        validar_entradas(texto, clave, alfabeto_mixto)

        texto_cifrado = ""
        clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]

        for i in range(len(texto)):
            caracter = texto[i]
            if caracter in alfabeto_mixto:
                desplazamiento = alfabeto_mixto.index(clave_repetida[i])
                indice_original = alfabeto_mixto.index(caracter)
                indice_cifrado = (indice_original + desplazamiento) % len(alfabeto_mixto)
                texto_cifrado += alfabeto_mixto[indice_cifrado]
            else:
                texto_cifrado += caracter
                logging.warning(f"Carácter '{caracter}' no encontrado en el alfabeto y se mantuvo igual.")

        return texto_cifrado

    except Exception as e:
        logging.error(f"Error en cifrado: {str(e)}")
        raise


def descifrado_cesar_clave(texto_cifrado, clave, alfabeto_mixto):
    #Descifra el texto usando una palabra clave como desplazamiento variable.
    try:
        validar_entradas(texto_cifrado, clave, alfabeto_mixto)

        texto_descifrado = ""
        clave_repetida = (clave * (len(texto_cifrado) // len(clave) + 1))[:len(texto_cifrado)]

        for i in range(len(texto_cifrado)):
            caracter_cifrado = texto_cifrado[i]
            if caracter_cifrado in alfabeto_mixto:
                desplazamiento = alfabeto_mixto.index(clave_repetida[i])
                indice_cifrado = alfabeto_mixto.index(caracter_cifrado)
                indice_original = (indice_cifrado - desplazamiento) % len(alfabeto_mixto)
                texto_descifrado += alfabeto_mixto[indice_original]
            else:
                texto_descifrado += caracter_cifrado
                logging.warning(f"Carácter '{caracter_cifrado}' no encontrado en el alfabeto y se mantuvo igual.")

        return texto_descifrado

    except Exception as e:
        logging.error(f"Error en descifrado: {str(e)}")
        raise


def main():
    alfabeto_mixto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+={}[]|;:<>,.?/"

    while True:
        try:
            print("\nBienvenido al Cifrado por Desplazamiento con Palabra Clave")
            print("\nOpciones:")
            print("1. Cifrar mensaje")
            print("2. Descifrar mensaje")
            print("3. Salir")

            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                try:
                    mensaje = input("Ingrese el mensaje a cifrar: ").strip()
                    if not mensaje:
                        print("Error: El mensaje no puede estar vacío.")
                        time.sleep(1)
                        continue

                    clave = input("Ingrese la palabra clave: ").strip()
                    mensaje_cifrado = cifrado_cesar_clave(mensaje, clave, alfabeto_mixto)
                    print("\nMensaje cifrado:", mensaje_cifrado)

                except ValueError as ve:
                    print(f"\nError de validación: {ve}")
                except Exception as e:
                    print(f"\nError inesperado al cifrar: {e}")

            elif opcion == "2":
                try:
                    mensaje_cifrado = input("Ingrese el mensaje cifrado: ").strip()
                    if not mensaje_cifrado:
                        print("Error: El mensaje cifrado no puede estar vacío.")
                        time.sleep(1)
                        continue

                    clave = input("Ingrese la palabra clave: ").strip()
                    mensaje_descifrado = descifrado_cesar_clave(mensaje_cifrado, clave, alfabeto_mixto)
                    print("\nMensaje descifrado:", mensaje_descifrado)

                except ValueError as ve:
                    print(f"\nError de validación: {ve}")
                except Exception as e:
                    print(f"\nError inesperado al descifrar: {e}")

            elif opcion == "3":
                print("\nSaliendo del programa...")
                time.sleep(1)
                break

            else:
                print("\nOpción no válida. Intente nuevamente.")
                time.sleep(1)

        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario. Saliendo...")
            time.sleep(1)
            break
        except Exception as e:
            print(f"\nError crítico: {e}")
            logging.critical(f"Error crítico en main: {str(e)}")
            break


if __name__ == "__main__":
    main()