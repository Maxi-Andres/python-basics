import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Crear datos para gráficos
x = np.linspace(0, 10, 100)
y = 2 * x + 1

# Gráfico de línea simple
plt.plot(x, y, label='y = 2x + 1')
plt.title('Gráfico de Línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.show()

print()

# Gráfico de dispersión (scatter plot)
y2 = y + np.random.normal(0, 1, size=x.size)  # Agregar ruido a los datos
plt.scatter(x, y2, color='red', label='Datos dispersos')
plt.title('Gráfico de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()

print()

# Gráfico de barras
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 9]
plt.bar(categories, values, color='green')
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.show()

print()

# Gráfico de barras horizontales
plt.barh(categories, values, color='orange')
plt.title('Gráfico de Barras Horizontales')
plt.xlabel('Valores')
plt.ylabel('Categorías')
plt.show()

print()

# Gráfico de histograma
data = np.random.randn(1000)  # Datos aleatorios con distribución normal
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

print()

# Gráfico de pastel
sizes = [25, 35, 20, 20]
plt.pie(sizes, labels=categories, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'orange'])
plt.title('Gráfico de Pastel')
plt.show()

print()

# Gráfico de múltiples líneas
y3 = np.sin(x)
y4 = np.cos(x)
plt.plot(x, y, label='y = 2x + 1')
plt.plot(x, y3, label='y = sin(x)')
plt.plot(x, y4, label='y = cos(x)')
plt.title('Gráfico de Múltiples Líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.show()

print()

# Subgráficos (subplots)
plt.subplot(2, 1, 1)
plt.plot(x, y, label='y = 2x + 1', color='blue')
plt.title('Subgráfico 1')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x, y3, label='y = sin(x)', color='red')
plt.title('Subgráfico 2')
plt.grid(True)

plt.tight_layout()
plt.show()

print()

# Gráfico con anotaciones
plt.plot(x, y, label='y = 2x + 1')
plt.title('Gráfico con Anotaciones')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.annotate('Punto clave', xy=(5, 11), xytext=(7, 20), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

print()

# Gráfico con estilo personalizado
plt.style.use('ggplot')
plt.plot(x, y, label='y = 2x + 1')
plt.plot(x, y3, label='y = sin(x)')
plt.title('Gráfico con Estilo Personalizado')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.show()

print()

# Gráfico de área
plt.fill_between(x, y3, color='yellow', alpha=0.5, label='Área bajo sin(x)')
plt.plot(x, y3, label='y = sin(x)', color='blue')
plt.title('Gráfico de Área')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()

# Gráfico de campana gaussiana (distribución normal)
mu, sigma = 64.43, 5  # Media y desviación estándar
pesos = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
pdf = norm.pdf(pesos, mu, sigma)
plt.plot(pesos, pdf, label=f'$\mu={mu},\ \sigma={sigma}$')
plt.title('Distribución Normal - Pesos de Golden Retriever')
plt.xlabel('Peso (lb)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()


# Generar una muestra de pesos de golden retrievers (en libras)
np.random.seed(0)  # Para reproducibilidad
pesos = np.random.normal(loc=64.43, scale=5, size=50)  # Media = 64.43 lb, Desviación estándar = 5 lb
# Crear el rango de valores para la gráfica
x = np.linspace(pesos.min() - 10, pesos.max() + 10, 1000)
pdf = norm.pdf(x, np.mean(pesos), np.std(pesos))
# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label='Distribución Normal Ajustada', color='blue')
plt.hist(pesos, bins=10, density=True, alpha=0.6, color='gray', edgecolor='black', label='Datos de Muestra')
plt.title('Distribución Normal de Pesos de Golden Retrievers')
plt.xlabel('Peso (lb)')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()

# Explicación de los ejemplos:
# 1. **Gráfico de línea**: Muestra una relación lineal simple.
# 2. **Gráfico de dispersión**: Visualiza datos dispersos con ruido aleatorio.
# 3. **Gráfico de barras**: Muestra datos categóricos en barras verticales.
# 4. **Gráfico de barras horizontales**: Similar al anterior, pero con barras horizontales.
# 5. **Histograma**: Representa la distribución de un conjunto de datos.
# 6. **Gráfico de pastel**: Muestra la proporción de categorías en un pastel.
# 7. **Múltiples líneas**: Compara varias funciones en el mismo gráfico.
# 8. **Subgráficos**: Muestra múltiples gráficos en una sola figura.
# 9. **Anotaciones**: Agrega anotaciones y flechas para resaltar puntos clave.
# 10. **Estilo personalizado**: Aplica un estilo visual específico a los gráficos.
# 11. **Gráfico de área**: Rellena el área bajo una curva para destacar la región.
# 12. **Campana gaussiana**: Grafica una distribución normal con parámetros específicos.
# 12. **Campana gaussiana y histograma**: Grafica una distribución normal con parámetros específicos.

# x: Los datos que se quieren graficar.
# bins: Número de barras en el histograma. Si es mayor, hay más barras, mostrando más detalles. (cantidad de columnas)
# range: Establece los límites inferior y superior para los datos en el histograma.
# density: Si es True, el área total del histograma se normaliza a 1.
# weights: Un array de pesos que ajusta la altura de cada barra en función del peso asociado.
# bottom: Posición base de las barras.
# histtype: Tipo de histograma. Ejemplo: bar (barras llenas), step (líneas).
# align: Alineación de las barras (left, mid, right).
# rwidth: Ancho relativo de las barras. Mayor valor = barras más anchas.
# log: Si es True, usa una escala logarítmica en el eje.
# color: Color de las barras.
# label: Etiqueta del dataset para la leyenda.
# normed: Ahora se usa density; ajusta la altura de las barras para que sumen 1.