import time
from collections import defaultdict, Counter
import math
from itertools import combinations
import re


def preprocesar_texto(texto):
    """Normaliza el texto: solo letras mayúsculas sin espacios ni caracteres especiales"""
    return re.sub(r'[^A-Za-z]', '', texto.upper())


def encontrar_secuencias_repetidas(texto, longitud_minima=2):
    """Encuentra todas las secuencias repetidas y sus posiciones"""
    secuencias = defaultdict(list)
    for i in range(len(texto) - longitud_minima + 1):
        secuencia = texto[i:i + longitud_minima]
        secuencias[secuencia].append(i)
    return {k: v for k, v in secuencias.items() if len(v) > 1}


def calcular_posibles_longitudes(distancias, max_longitud=20):
    """Calcula posibles longitudes de clave basado en factores comunes"""
    factores = Counter()

    for distancia in distancias:
        # Considerar todos los factores posibles
        for i in range(2, min(distancia, max_longitud) + 1):
            if distancia % i == 0:
                factores[i] += 1

    # Ordenar factores por frecuencia y magnitud
    factores_ordenados = sorted(factores.items(), key=lambda x: (-x[1], x[0]))

    # Devolver solo las longitudes más probables
    return [f[0] for f in factores_ordenados[:3]] if factores_ordenados else [3, 4, 5]  # Valores por defecto


def analizar_frecuencias(grupo, frecuencias_esperadas):
    """Analiza frecuencias de letras para encontrar el desplazamiento más probable"""
    frecuencias = Counter(grupo)
    total = len(grupo)
    mejor_desplazamiento = 0
    mejor_puntaje = float('-inf')

    for desplazamiento in range(26):
        puntaje = 0
        for letra, count in frecuencias.items():
            letra_original = chr(((ord(letra) - ord('A') - desplazamiento) % 26 + ord('A')))
            puntaje += count * math.log(frecuencias_esperadas.get(letra_original, 0.0001))

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_desplazamiento = desplazamiento

    return mejor_desplazamiento


def descifrar_grupo(texto, desplazamiento):
    """Descifra un texto aplicando un desplazamiento inverso"""
    return ''.join(
        chr(((ord(c) - ord('A') - desplazamiento) % 26 + ord('A')))
            for c in texto)


def verificar_resultado(texto_descifrado, frecuencias_esperadas, umbral=0.05):
    """Verifica si el texto descifrado tiene frecuencias plausibles"""
    frecuencias = Counter(texto_descifrado)
    total = len(texto_descifrado)
    error = 0

    for letra, freq_esperada in frecuencias_esperadas.items():
        freq_observada = frecuencias.get(letra, 0) / total
        error += abs(freq_observada - freq_esperada)

    return error / len(frecuencias_esperadas) < umbral


def ataque_kasiski_mejorado(texto_cifrado, frecuencias_idioma, longitud_clave=None):
    """Ataque mejorado de Kasiski con manejo de textos cortos"""
    texto = preprocesar_texto(texto_cifrado)
    longitud_texto = len(texto)

    if longitud_texto < 30:
        print("[!] Advertencia: Texto muy corto, los resultados pueden ser menos precisos")

    # Paso 1: Estimar longitud de clave
    if longitud_clave is None:
        secuencias = encontrar_secuencias_repetidas(texto, 2)  # Usar secuencias más cortas para textos pequeños

        if not secuencias:
            # Si no hay secuencias repetidas, probar con longitudes comunes
            posibles_longitudes = [3, 4, 5, 6, 7, 8]
        else:
            distancias = [abs(j - i) for pos in secuencias.values() for i, j in combinations(pos, 2)]
            posibles_longitudes = calcular_posibles_longitudes(distancias)

        print(f"[+] Posibles longitudes de clave: {posibles_longitudes}")
    else:
        posibles_longitudes = [longitud_clave]

    mejores_resultados = []

    for longitud in posibles_longitudes:
        # Paso 2: Dividir en grupos según la longitud de clave
        grupos = [[] for _ in range(longitud)]
        for i, c in enumerate(texto):
            grupos[i % longitud].append(c)

        # Paso 3: Analizar cada grupo para encontrar la clave
        clave = []
        for grupo in grupos:
            desplazamiento = analizar_frecuencias(grupo, frecuencias_idioma)
            clave.append(chr(desplazamiento + ord('A')))

        clave_str = ''.join(clave)

        # Paso 4: Descifrar con la clave encontrada
        texto_descifrado = []
        for i, c in enumerate(texto):
            desplazamiento = ord(clave_str[i % longitud]) - ord('A')
            texto_descifrado.append(
                chr(((ord(c) - ord('A') - desplazamiento) % 26 + ord('A'))))

            texto_descifrado_str = ''.join(texto_descifrado)

            # Paso 5: Verificar la calidad del descifrado
            es_valido = verificar_resultado(texto_descifrado_str, frecuencias_idioma)
            puntaje = sum(frecuencias_idioma.get(c, 0) for c in texto_descifrado_str) / len(texto_descifrado_str)

            mejores_resultados.append((puntaje, longitud, clave_str, texto_descifrado_str))

            # Ordenar resultados por puntaje (mejores primero)
            mejores_resultados.sort(reverse=True, key=lambda x: x[0])

    return mejores_resultados


def main():
    # Frecuencias de letras en español
    FRECUENCIAS_ES = {
        'A': 0.1253, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586,
        'E': 0.1368, 'F': 0.0069, 'G': 0.0101, 'H': 0.0070,
        'I': 0.0625, 'J': 0.0044, 'K': 0.0002, 'L': 0.0497,
        'M': 0.0315, 'N': 0.0671, 'O': 0.0868, 'P': 0.0251,
        'Q': 0.0088, 'R': 0.0687, 'S': 0.0798, 'T': 0.0463,
        'U': 0.0393, 'V': 0.0090, 'W': 0.0001, 'X': 0.0022,
        'Y': 0.0090, 'Z': 0.0052
    }

    print("\n" + "=" * 50)
    print("  ATAQUE METODO DE KASISKI  ".center(50))
    print("=" * 50)

    while True:
        texto_cifrado = input("\nIngrese el texto cifrado (o 'salir' para terminar): ").strip()

        if texto_cifrado.lower() == 'salir':
            break

        if not texto_cifrado:
            print("[!] Por favor ingrese un texto válido")
            continue

        print("\n[+] Analizando texto...")
        start_time = time.time()

        resultados = ataque_kasiski_mejorado(texto_cifrado, FRECUENCIAS_ES)

        print(f"\n[+] Tiempo de análisis: {time.time() - start_time:.2f} segundos")

        if not resultados:
            print("[!] No se encontraron resultados válidos")
            continue

        print("\n[+] Mejores resultados encontrados:")
        for i, (puntaje, longitud, clave, texto_descifrado) in enumerate(resultados[:3], 1):
            print(f"\nOpción {i}:")
            print(f"Longitud clave: {longitud}")
            print(f"Clave probable: {clave}")
            print(f"Texto descifrado: {texto_descifrado[:200]}{'...' if len(texto_descifrado) > 200 else ''}")
            print(f"Puntaje de confianza: {puntaje:.4f}")

        # Opción para probar con una longitud específica
        opcion = input(
            "\n¿Desea probar con una longitud específica? (ingrese el número o Enter para continuar): ").strip()
        if opcion.isdigit():
            longitud = int(opcion)
            resultados_especificos = ataque_kasiski_mejorado(texto_cifrado, FRECUENCIAS_ES, longitud)
            if resultados_especificos:
                print("\n[+] Resultado con longitud especificada:")
                _, _, clave, texto_descifrado = resultados_especificos[0]
                print(f"Clave: {clave}")
                print(f"Texto descifrado: {texto_descifrado[:200]}{'...' if len(texto_descifrado) > 200 else ''}")


if __name__ == "__main__":
    main()