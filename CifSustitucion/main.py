import time
#Funciones
from CifSustitucion import mono_Alfabetica
from CifSustitucion import poli_Alfabetica

def main():

    while True:
        try:
            print("\nBienvenido al Cifrado por Sustitucion: ")
            print("\nOpciones:")
            print("1. Mono Alfabetica (Transformacion Afin)")
            print("2. Poli Alfabetica")
            print("3. Salir")

            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                mono_Alfabetica.main()
                time.sleep(0.5)

            elif opcion == "2":
                poli_Alfabetica.main()
                time.sleep(0.5)

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

if __name__ == "__main__":
    main()