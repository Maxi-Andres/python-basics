
# Ejemplos de funciones comunes en SciPy

import numpy as np
from scipy import stats, optimize, integrate, linalg, interpolate

# ===============================
# Estadísticas (scipy.stats)
# ===============================

# Generar una distribución normal y calcular estadísticas
data = np.random.normal(0, 1, 1000)  # Media=0, std=1
print("Media:", np.mean(data), "Desvío estándar:", np.std(data))

# Prueba t de una muestra: si la media de los datos difiere de cero
t_stat, p_valor = stats.ttest_1samp(data, 0)
print("Estadístico t:", t_stat, "Valor p:", p_valor)

# ===============================
# Optimización (scipy.optimize)
# ===============================

# Mínimo de una función (ejemplo: x^2 + 10*sin(x))
def funcion(x):
    return x**2 + 10 * np.sin(x)

resultado = optimize.minimize(funcion, x0=2)
print("Mínimo de la función:", resultado.x[0], "f(x):", resultado.fun)

# Ajuste de curva: ajusta datos a una función sinusoide
x_data = np.linspace(0, 4, 50)
y_data = 3 * np.sin(2 * x_data) + np.random.normal(size=x_data.size)
def modelo(x, a, b): return a * np.sin(b * x)
params, _ = optimize.curve_fit(modelo, x_data, y_data)
print("Parámetros ajustados:", params)

# ===============================
# Integración numérica (scipy.integrate)
# ===============================

# Integración de x^2 en [0, 1]
resultado, error = integrate.quad(lambda x: x**2, 0, 1)
print("Integral de x^2 en [0, 1]:", resultado, "Error:", error)

# ===============================
# Álgebra lineal (scipy.linalg)
# ===============================

# Resolver un sistema lineal Ax = b
A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6])
x = linalg.solve(A, b)
print("Solución de Ax = b:", x)

# ===============================
# Interpolación (scipy.interpolate)
# ===============================

# Interpolación lineal a partir de puntos de datos
x = np.linspace(0, 10, 10)
y = np.sin(x)
f_lineal = interpolate.interp1d(x, y)
x_nuevo = np.linspace(0, 10, 50)
y_nuevo = f_lineal(x_nuevo)
print("Valores interpolados:", y_nuevo)
