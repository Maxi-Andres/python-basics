# Importamos las librerías necesarias
from tqdm import tqdm
import time
import random
import pandas as pd
import concurrent.futures

# 1. Barra de progreso en un bucle simple
print("Ejemplo 1: Barra de progreso en un bucle simple")
for i in tqdm(range(10), desc="Procesando items", unit="item"):
    time.sleep(0.5)  # Simulamos un proceso con un tiempo de espera
print("\n")

# 2. Uso de tqdm con listas o iterables
print("Ejemplo 2: Barra de progreso con listas o iterables")
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for item in tqdm(items, desc="Procesando frutas"):
    time.sleep(1)  # Simula algún trabajo que toma tiempo
print("\n")

# 3. Uso de tqdm con un generador
print("Ejemplo 3: Barra de progreso con un generador")
def generate_data():
    for _ in range(10):
        yield random.randint(1, 100)
        time.sleep(0.5)

for data in tqdm(generate_data(), desc="Generando datos"):
    pass
print("\n")

# 4. Barra de progreso con pandas para procesamiento de DataFrames
print("Ejemplo 4: Barra de progreso con pandas")
df = pd.DataFrame({
    'col1': range(1, 101),
    'col2': range(101, 201)
})

for idx, row in tqdm(df.iterrows(), total=df.shape[0], desc="Procesando filas"):
    time.sleep(0.1)  # Simula procesamiento de cada fila
print("\n")

# 5. Barra de progreso con procesamiento de archivos grandes
print("Ejemplo 5: Barra de progreso con procesamiento de archivos grandes")
with open('grande_archivo.txt', 'w') as f:
    for i in range(1000):
        f.write(f"linea {i}\n")

with open('grande_archivo.txt', 'r') as file:
    lines = file.readlines()

for line in tqdm(lines, desc="Leyendo archivo", unit="línea"):
    pass  # Aquí iría el código para procesar cada línea
print("\n")

# 6. Barra de progreso con procesamiento paralelo usando concurrent.futures
print("Ejemplo 6: Barra de progreso con procesamiento paralelo")
def process_item(item):
    time.sleep(1)
    return item

items = range(10)

with concurrent.futures.ThreadPoolExecutor() as executor:
    list(tqdm(executor.map(process_item, items), total=len(items), desc="Procesando en paralelo"))
print("\n")

# 7. Barra de progreso con actualización manual
print("Ejemplo 7: Barra de progreso con actualización manual")
progress = tqdm(total=100, desc="Progreso manual", unit="steps")

for i in range(100):
    time.sleep(0.1)
    progress.update(1)  # Actualiza la barra de progreso manualmente

progress.close()  # Cerramos la barra cuando termina
print("\n")


# Bucle simple: Una barra de progreso que muestra el avance mientras iteras en un bucle.
# Listas o iterables: Muestra cómo utilizar tqdm en listas u otros iterables.
# Generadores: Usa tqdm en generadores para mostrar el progreso mientras los elementos son generados.
# Pandas: Muestra cómo usar tqdm al iterar sobre las filas de un DataFrame de pandas.
# Archivos grandes: Simula el procesamiento de un archivo de texto con una barra de progreso.
# Procesamiento paralelo: Usa concurrent.futures para realizar un trabajo en paralelo y mostrar el progreso.
# Actualización manual: Muestra cómo actualizar la barra manualmente usando update().

# NOTA
# El archivo de texto (grande_archivo.txt) en el ejemplo 5 debe ser creado o puedes eliminar esa parte si no quieres generar el archivo.
# En el ejemplo de procesamiento paralelo (Ejemplo 6), tqdm se utiliza con ThreadPoolExecutor para mapear el procesamiento de los elementos de la lista items.