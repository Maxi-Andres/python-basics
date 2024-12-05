import pandas as pd

# Leer el archivo CSV
arch = pd.read_csv("datos.csv")
arch2 = pd.read_csv("datos.csv")

# Obtener los datos de la columna 'nombre'
print("Columna 'nombre':")
print(arch["nombre"])
print()

# Ordenar el DataFrame por 'edad' de mayor a menor
print("DataFrame ordenado por 'edad' (descendente):")
arch_ordenado = arch.sort_values("edad", ascending=False)
print(arch_ordenado)
print()

# Concatenar dos DataFrames
print("DataFrames concatenados:")
arch_concatenados = pd.concat([arch, arch2])
print(arch_concatenados)
print()

# Obtener la primera fila del DataFrame
print("Primera fila del DataFrame:")
fila_particular = arch.head(1)
print(fila_particular)
print()

# Acceder al número total de filas y columnas
print("Número total de columnas:")
filas_totales, columnas_totales = arch.shape
print(columnas_totales)
print()

# Obtener estadísticas descriptivas del DataFrame
print("Estadísticas descriptivas:")
archivo_info = arch.describe()
print(archivo_info)
print()

# Acceder a un elemento específico con .loc
print("Elemento en la fila 2, columna 'edad' con .loc:")
elemento_especifico_loc = arch.loc[2, "edad"]
print(elemento_especifico_loc)
print()

# Acceder a un elemento específico con .iloc
print("Elemento en la fila 2, columna 2 con .iloc:")
elemento_especifico_iloc = arch.iloc[2, 2]
print(elemento_especifico_iloc)
print()

# Acceder a toda la columna 'apellido' con .loc
print("Columna 'apellido' con .loc:")
apellidos = arch.loc[:, "apellido"]
print(apellidos)
print()

# Acceder a toda la columna 'apellido' con .iloc
print("Columna 'apellido' con .iloc:")
apellidos_iloc = arch.iloc[:, 1]
print(apellidos_iloc)
print()

# Acceder a la fila 3 con .loc
print("Fila 3 con .loc:")
fila_3 = arch.loc[2, :]
print(fila_3)
print()

# Acceder a la fila 3 con .iloc
print("Fila 3 con .iloc:")
fila_3_iloc = arch.iloc[2, :]
print(fila_3_iloc)
print()

# Filtrar filas donde 'edad' es mayor a 30
print("Filas donde 'edad' > 30:")
mayor_que_30 = arch.loc[arch["edad"] > 30, :]
print(mayor_que_30)
print()

# Agrupar datos por una columna y calcular la media(promedio)
print("Media de 'edad' agrupada por 'apellido':")
media_por_apellido = arch.groupby("apellido")["edad"].mean()
print(media_por_apellido)
print()

# Agrupar datos por una columna y encontrar la mediana(el valor del medio)
print("Mediana de 'edad' agrupada por 'apellido':")
mediana_por_apellido = arch.groupby("apellido")["edad"].median()
print(mediana_por_apellido)
print()

# te devuelve la desviacion estandar es para otro ejemplo pero bueno lo pongo aca
#YearsExperience_desviacion_estandar = arch['YearsExperience'].std()


# Obtener valores únicos en la columna 'apellido'
print("Valores únicos en la columna 'apellido':")
valores_unicos_apellido = arch["apellido"].unique()
print(valores_unicos_apellido)
print()

# Aplicar una función a una columna
print("Edad incrementada en 1 año:")
edad_incrementada = arch["edad"].apply(lambda x: x + 1)
print(edad_incrementada)
print()

# Eliminar una columna del DataFrame
print("DataFrame sin la columna 'apellido':")
arch_sin_apellido = arch.drop(columns=["apellido"])
print(arch_sin_apellido)
print()

# Reemplazar valores en una columna
print("Reemplazar 'maxi' por 'Maximiliano' en la columna 'nombre':")
arch_reemplazado = arch.replace({"nombre": {"maxi": "Maximiliano"}})
print(arch_reemplazado)
print()

# Renombrar columnas
print("Columnas renombradas:")
arch_renombrado = arch.rename(columns={"nombre": "Nombre", "edad": "Edad"}) #inplace=True hace que no tengas que crear arch_renombrado
print(arch_renombrado)
print()

# Añadir una nueva columna calculada
print("Nueva columna 'año_nacimiento':")
arch["año_nacimiento"] = 2024 - arch["edad"]
print(arch)
print()

# Ordenar columnas de forma personalizada
print("DataFrame con columnas reordenadas:")
arch_reordenado = arch[["nombre", "año_nacimiento", "edad"]]
print(arch_reordenado)
print()

# Filtrar filas con múltiples condiciones
print("Filas donde 'edad' > 30 y 'apellido' es 'andres':")
filtro_multiple = arch.loc[(arch["edad"] > 30) & (arch["apellido"] == "andres"), :]
print(filtro_multiple)
print()

# Eliminar filas duplicadas
print("DataFrame sin filas duplicadas:")
arch_sin_duplicados = arch.drop_duplicates()
print(arch_sin_duplicados)
print()

# Restablecer el índice del DataFrame
print("Índice restablecido:")
arch_reset_index = arch.reset_index(drop=True)
print(arch_reset_index)
print()

# Transponer el DataFrame
print("DataFrame transpuesto:")
arch_transpuesto = arch.T
print(arch_transpuesto)
print()

# Crear un DataFrame desde un diccionario
print("DataFrame creado desde un diccionario:")
data = {"nombre": ["Ana", "Luis"], "edad": [22, 34], "apellido": ["Pérez", "López"]}
nuevo_df = pd.DataFrame(data)
print(nuevo_df)
print()

# Aplicar filtros condicionales con .query()
print("Filas donde 'edad' > 30 usando .query():")
filtro_query = arch.query("edad > 30")
print(filtro_query)
print()
