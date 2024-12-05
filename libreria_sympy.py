from sympy import *

# Definir una variable simbólica
x = symbols('x')

# Crear una función algebraica simple
f = 2*x + 1
print("Función f(x):", f)
print()

# Graficar la función
plot(f, title="Gráfico de f(x) = 2x + 1", xlabel="x", ylabel="f(x)")

# Derivar la función
f_derivada = diff(f, x)
print("Derivada de f(x):", f_derivada)
print()

# Integrar la función
f_integral = integrate(f, x)
print("Integral de f(x):", f_integral)
print()

# Evaluar la función en un punto
f_evaluado = f.subs(x, 3)
print("f(x) evaluada en x=3:", f_evaluado)
print()

# Resolver una ecuación
ecuacion = Eq(f, 0)
solucion = solve(ecuacion, x)
print("Solución de la ecuación f(x) = 0:", solucion)
print()

# Simplificar una expresión
expresion = (x**2 - 1) / (x - 1)
expresion_simplificada = simplify(expresion)
print("Expresión simplificada:", expresion_simplificada)
print()

# Expandir una expresión
expresion_expandida = expand((x + 1)**2)
print("Expresión expandida:", expresion_expandida)
print()

# Factorizar una expresión
expresion_factorizada = factor(x**2 - 4)
print("Expresión factorizada:", expresion_factorizada)
print()

# Hallar los puntos críticos de la función (donde la derivada es cero)
puntos_criticos = solve(f_derivada, x)
print("Puntos críticos de f(x):", puntos_criticos)
print()

# Sustituir una expresión en otra
g = x**2
nueva_expresion = f.subs(x, g)
print("Sustituyendo x en f(x) por x**2:", nueva_expresion)
print()

# Resolver un sistema de ecuaciones
y = symbols('y')
ecuacion1 = Eq(2*x + y, 1)
ecuacion2 = Eq(x - y, 3)
soluciones = solve((ecuacion1, ecuacion2), (x, y))
print("Soluciones del sistema de ecuaciones:", soluciones)
print()

# Expresión trigonométrica
exp_trig = sin(x)**2 + cos(x)**2
exp_trig_simplificada = simplify(exp_trig)
print("Simplificación trigonométrica de sin(x)**2 + cos(x)**2:", exp_trig_simplificada)
print()

# Hallar el límite de una función
limite = limit(f / x, x, 0)
print("Límite de f(x)/x cuando x tiende a 0:", limite)
print()

# Serie de Taylor
serie_taylor = f.series(x, 0, 5)
print("Serie de Taylor de f(x) en torno a x=0:", serie_taylor)
print()

# Solución de una integral definida
integral_definida = integrate(f, (x, 0, 2))
print("Integral definida de f(x) de 0 a 2:", integral_definida)
print()


# Explicación de los ejemplos:
# 1. **Definición de función**: Se define una función algebraica.
# 2. **Derivada**: Se calcula la derivada de la función.
# 3. **Integral**: Se obtiene la integral indefinida.
# 4. **Evaluación**: Se evalúa la función en un punto específico.
# 5. **Resolución de ecuación**: Se resuelve una ecuación.
# 6. **Simplificación**: Se simplifica una expresión algebraica.
# 7. **Expansión**: Se expande un binomio.
# 8. **Factorización**: Se factoriza una expresión.
# 9. **Puntos críticos**: Se encuentran los puntos críticos de la función.
# 10. **Sustitución**: Se sustituye una variable por una expresión.
# 11. **Sistema de ecuaciones**: Se resuelve un sistema de ecuaciones lineales.
# 12. **Trigonometría**: Se simplifica una expresión trigonométrica.
# 13. **Límite**: Se halla el límite de una función.
# 14. **Serie de Taylor**: Se calcula la serie de Taylor de la función.
# 15. **Integral definida**: Se calcula la integral definida de la función en un intervalo dado.