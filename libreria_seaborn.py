# Importamos las librerías necesarias
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Gráfico de dispersión (scatter plot)
print("Ejemplo 1: Gráfico de dispersión")
# Generar datos de ejemplo
x = np.random.rand(100)
y = np.random.rand(100)

# Crear un gráfico de dispersión con Seaborn
sns.scatterplot(x=x, y=y)
plt.title("Gráfico de dispersión")
plt.show()

# 2. Gráfico de barras (bar plot)
print("Ejemplo 2: Gráfico de barras")
# Datos de ejemplo
data = {'Categoría': ['A', 'B', 'C', 'D'], 'Valor': [10, 20, 15, 30]}
df = pd.DataFrame(data)

# Crear un gráfico de barras
sns.barplot(x='Categoría', y='Valor', data=df)
plt.title("Gráfico de barras")
plt.show()

# 3. Gráfico de cajas (box plot)
print("Ejemplo 3: Gráfico de cajas")
# Generar datos de ejemplo
data = np.random.normal(size=(20, 5))  # 5 grupos con 20 datos cada uno

# Crear un gráfico de cajas
sns.boxplot(data=data)
plt.title("Gráfico de cajas")
plt.show()

# 4. Gráfico de violín (violin plot)
print("Ejemplo 4: Gráfico de violín")
# Generar datos de ejemplo
data = np.random.normal(size=(100, 3))  # 3 grupos con 100 datos cada uno

# Crear un gráfico de violín
sns.violinplot(data=data)
plt.title("Gráfico de violín")
plt.show()

# 5. Mapa de calor (heatmap)
print("Ejemplo 5: Mapa de calor")
# Crear una matriz de correlación aleatoria
corr_matrix = np.random.rand(5, 5)

# Crear un mapa de calor
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Mapa de calor")
plt.show()

# 6. Gráfico de distribución (distplot)
print("Ejemplo 6: Gráfico de distribución")
# Generar datos de ejemplo
data = np.random.randn(1000)

# Crear un gráfico de distribución
sns.histplot(data, kde=True)
plt.title("Gráfico de distribución")
plt.show()

# 7. Pairplot (gráfico de pares)
print("Ejemplo 7: Pairplot")
# Generar datos de ejemplo
df = sns.load_dataset('iris')  # Dataset Iris de Seaborn

# Crear un pairplot (gráfico de pares)
sns.pairplot(df, hue='species')
plt.title("Pairplot")
plt.show()

# 8. Gráfico de regresión (regplot)
print("Ejemplo 8: Gráfico de regresión")
# Generar datos de ejemplo
x = np.random.rand(100)
y = 2 * x + np.random.randn(100) * 0.1

# Crear un gráfico de regresión
sns.regplot(x=x, y=y)
plt.title("Gráfico de regresión")
plt.show()

# 9. Gráfico de barras con múltiples variables
print("Ejemplo 9: Gráfico de barras con múltiples variables")
# Datos de ejemplo
tips = sns.load_dataset("tips")

# Crear un gráfico de barras con hue (para diferenciación)
sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
plt.title("Gráfico de barras con hue")
plt.show()

# 10. Heatmap con anotaciones personalizadas
print("Ejemplo 10: Heatmap con anotaciones personalizadas")
# Crear una matriz de correlación aleatoria
corr_matrix = np.random.rand(5, 5)

# Crear un mapa de calor con anotaciones personalizadas
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='YlGnBu')
plt.title("Mapa de calor con anotaciones personalizadas")
plt.show()

# Gráfico de dispersión: Utiliza sns.scatterplot() para crear un gráfico de dispersión simple.
# Gráfico de barras: Usa sns.barplot() para crear gráficos de barras con los datos proporcionados.
# Gráfico de cajas: Usa sns.boxplot() para crear un gráfico de cajas que muestra la distribución de los datos.
# Gráfico de violín: Utiliza sns.violinplot() para crear un gráfico de violín, que combina aspectos de un gráfico de cajas con una distribución de densidad.
# Mapa de calor: Usa sns.heatmap() para mostrar una matriz de correlación en forma de mapa de calor.
# Gráfico de distribución: Usa sns.histplot() para mostrar una distribución de los datos con un histograma y una línea de densidad.
# Pairplot: Usa sns.pairplot() para crear una matriz de gráficos de dispersión entre diferentes características de un conjunto de datos.
# Gráfico de regresión: Utiliza sns.regplot() para crear un gráfico de regresión lineal entre dos variables.
# Gráfico de barras con múltiples variables: Muestra cómo usar hue para crear un gráfico de barras categóricas diferenciadas por una variable adicional (como el sexo en el dataset tips).
# Mapa de calor con anotaciones personalizadas: Muestra cómo personalizar los mapas de calor añadiendo anotaciones con formato.
# Nota:
# El archivo tips y iris son datasets de ejemplo que vienen con Seaborn, lo que te permite probar rápidamente los gráficos sin necesidad de datos externos.
# Asegúrate de tener instalada la librería seaborn antes de ejecutar este archivo.