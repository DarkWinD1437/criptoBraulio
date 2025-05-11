import time
#Funciones
from CifTransposicion import grupos
from CifTransposicion import filas
from CifTransposicion import series
from CifTransposicion import zigzag
from CifTransposicion import columnas

def main():

    while True:
        try:
            print("\n" + "=" * 50)
            print("Bienvenido al Cifrado por Transposicion por: ".center(50))
            print("=" * 50)
            print("\nOpciones:")
            print("1. Grupos")
            print("2. Series")
            print("3. Filas")
            print("4. Zig-Zag")
            print("5. Columnas")
            print("6. Salir")

            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                grupos.main()
                time.sleep(0.5)

            elif opcion == "2":
                series.main()
                time.sleep(0.5)

            elif opcion == "3":
                filas.main()
                time.sleep(0.5)

            elif opcion == "4":
                zigzag.main()
                time.sleep(0.5)

            elif opcion == "5":
                columnas.main()
                time.sleep(0.5)

            elif opcion == "6":
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