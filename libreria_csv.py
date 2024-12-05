import csv

with open("datos.csv") as archivito:
    reader = csv.reader(archivito)
    for row in reader:
        print(row)

# Crear y escribir en un archivo CSV
with open('archivo.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Apellido', 'Edad'])
    writer.writerow(['Maxi', 'Andres', 99])
    writer.writerow(['Adolfo', 'Demencial', 23])
    writer.writerow(['Pepe', 'Obispo', 34])
print("Archivo CSV creado y datos escritos.")
print()

# Leer un archivo CSV
with open('archivo.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print()

# Leer un archivo CSV como diccionario
with open('archivo.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
print()

# Escribir en un archivo CSV usando DictWriter
with open('archivo2.csv', mode='w', newline='') as file:
    fieldnames = ['Nombre', 'Apellido', 'Edad']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Nombre': 'Ana', 'Apellido': 'Smith', 'Edad': 28})
    writer.writerow({'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 45})
print("Archivo CSV creado con DictWriter y datos escritos.")
print()

# Leer y filtrar datos de un archivo CSV
with open('archivo.csv', mode='r') as file:
    reader = csv.DictReader(file)
    mayores_que_30 = [row for row in reader if int(row['Edad']) > 30]
    for row in mayores_que_30:
        print(row)
print()

# Añadir nuevas filas a un archivo CSV existente
with open('archivo.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Luis', 'Garcia', 50])
    writer.writerow(['Maria', 'Lopez', 19])
print("Nuevas filas añadidas al archivo CSV.")
print()

# Contar el número de filas en un archivo CSV
with open('archivo.csv', mode='r') as file:
    reader = csv.reader(file)
    filas = sum(1 for row in reader)
print(f"El archivo CSV tiene {filas} filas.")
print()

# Leer y transformar datos en un archivo CSV
with open('archivo.csv', mode='r') as file:
    reader = csv.reader(file)
    datos_transformados = [[col.upper() for col in row] for row in reader]
    for row in datos_transformados:
        print(row)
print()

# Escribir datos a un archivo CSV delimitado por tabulaciones
with open('archivo_tab.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['Nombre', 'Apellido', 'Edad'])
    writer.writerow(['Pedro', 'Gomez', 36])
    writer.writerow(['Laura', 'Martinez', 42])
print("Archivo CSV delimitado por tabulaciones creado y datos escritos.")
print()

# Explicación de los ejemplos:
# 1. **Escribir en un archivo CSV**: Crea un archivo y escribe filas en él.
# 2. **Leer un archivo CSV**: Lee y muestra cada fila de un archivo CSV.
# 3. **Leer como diccionario**: Lee un CSV y convierte cada fila en un diccionario.
# 4. **Escribir con DictWriter**: Crea un archivo CSV usando un diccionario para las filas.
# 5. **Filtrar datos**: Lee y filtra filas en función de un criterio (edad > 30).
# 6. **Añadir filas**: Añade nuevas filas a un archivo CSV existente.
# 7. **Contar filas**: Cuenta el número total de filas en un archivo CSV.
# 8. **Transformar datos**: Lee y transforma los datos, como convertir texto a mayúsculas.
# 9. **Archivo delimitado por tabulaciones**: Crea un archivo CSV donde las columnas están separadas por tabulaciones en lugar de comas.