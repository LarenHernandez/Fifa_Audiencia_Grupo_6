"""Pipeline de analisis: audiencia y economia del futbol (FIFA) - Grupo 6.

Flujo: 1. Carga y validacion -> 2. Limpieza -> 3. Analisis -> 4. Visualizacion
"""

from cargador import CargarCSV

def main():
    try:
        # 1. Carga y validacion
        datos = CargarCSV("data/grupo06_futbol_audiencia_fifa.csv").cargar()
        print(f"Cargadas {len(datos)} filas.")

    except (FileNotFoundError) as e:
        print(f"No se han podido cargar los datos: {e}")

if __name__ == "__main__":
    main()