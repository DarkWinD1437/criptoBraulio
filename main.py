import os
import time

#los siguientes modulos aquí
from CifDesplazamiento import puroPalabraClave
from CifTransposicion import main as mainTrans
from CifSustitucion import main as mainSus
from CifSustMonoPoli import main as mainMono

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
            puroPalabraClave.main()

        elif opcion == "2":
            mainTrans.main()

        elif opcion == "3":
            mainSus.main()

        elif opcion == "4":
            mainMono.main()

        # Agrega el resto de las opciones aquí
        elif opcion == "5":
            print("\n¡Saliendo del programa!")
            time.sleep(1)
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()