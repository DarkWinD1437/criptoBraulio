import os
import time

#los siguientes modulos aquí
import CifDesplazamiento.puroPalabraClave
import CifTransposicion

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
# Función principal
def main():
    while True:
        limpiar_pantalla()
        print("\nBienvenido al programa de cifrado")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifrado por Desplazamiento")
        print("2. Cifrado por Transposicion por: ")
        print("3. Cifrado por Sustitucion")
        print("4. Cifrado por Sustitucion Monogramica Polialfabeto")
        print("5. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            CifDesplazamiento.puroPalabraClave.main()

        elif opcion == "2":
            CifTransposicion.main.main()

        elif opcion == "3":
            cifrado_monogramico_polialfabeto.main()

        elif opcion == "4":
            cifrado_poligramica_monoalfabeto.main()

        # Agrega el resto de las opciones aquí
        elif opcion == "5":
            print("\n¡Saliendo del programa!")
            time.sleep(1)
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
