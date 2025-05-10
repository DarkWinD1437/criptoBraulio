import time
#Funciones
from CifSustMonoPoli import anagramacion
from CifSustMonoPoli import ataque_kasiski
from CifSustMonoPoli import hill
from CifSustMonoPoli import playfair

def main():

    while True:
        try:
            print("\nBienvenido al Cifrado por Sustitucion Monogramica Polialfabeto: ")
            print("\nOpciones:")
            print("Polialfabeticos Periodicos")
            print("1. Anagramacion en cifras o columnas")
            print("2. Playfair")
            print("3. Ataque de Kasiski")
            print("4. Cifrado de Hill")
            print("6. Salir")

            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                anagramacion.main()
                time.sleep(0.5)

            elif opcion == "2":
                playfair.main()
                time.sleep(0.5)

            elif opcion == "3":
                ataque_kasiski.main()
                time.sleep(0.5)

            elif opcion == "4":
                hill.main()
                time.sleep(0.5)

            elif opcion == "5":
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