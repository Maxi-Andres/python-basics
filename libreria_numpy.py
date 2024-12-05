import numpy as np

# Crear un array 2D de ejemplo
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Obtener la forma (shape) del array
print("Forma del array:")
print(array.shape)
print()

# Obtener el número total de elementos
print("Número total de elementos:")
print(array.size)
print()

# Acceder a un elemento específico (fila 1, columna 2)
print("Elemento en fila 1, columna 2:")
print(array[0, 1])
print()

# Acceder a una fila específica (fila 2)
print("Fila 2 completa:")
print(array[1, :])
print()

# Acceder a una columna específica (columna 3)
print("Columna 3 completa:")
print(array[:, 2])
print()

# Sumar todos los elementos del array
print("Suma de todos los elementos:")
print(array.sum())
print()

# Calcular la media de todos los elementos
print("Media de todos los elementos:")
print(array.mean())
print()

# Encontrar el valor máximo en el array
print("Valor máximo:")
print(array.max())
print()

# Encontrar el valor mínimo en el array
print("Valor mínimo:")
print(array.min())
print()

# Transponer el array (intercambiar filas por columnas)
print("Array transpuesto:")
print(array.T)
print()

# Aplanar el array (convertirlo en 1D)
print("Array aplanado:")
print(array.flatten())
print()

# Ordenar los elementos de cada fila
print("Elementos de cada fila ordenados:")
print(np.sort(array, axis=1))
print()

# Ordenar los elementos de cada columna
print("Elementos de cada columna ordenados:")
print(np.sort(array, axis=0))
print()

# Filtrar elementos mayores que 5
print("Elementos mayores que 5:")
print(array[array > 5])
print()

# Crear un array de ceros con la misma forma
print("Array de ceros:")
print(np.zeros_like(array))
print()

# Crear un array de unos con la misma forma
print("Array de unos:")
print(np.ones_like(array))
print()

# Multiplicar todos los elementos por 2
print("Array multiplicado por 2:")
print(array * 2)
print()

# Calcular el producto punto de dos arrays
array2 = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

print("Producto punto de los dos arrays:")
print(np.dot(array, array2))
print()

# Calcular la suma acumulada
print("Suma acumulada:")
print(np.cumsum(array))
print()

# Reshape: cambiar la forma del array
print("Array reshaped a (1, 9):")
print(array.reshape(1, 9))
print()

# Crear un array con valores equidistantes entre 0 y 1
print("Array con valores equidistantes entre 0 y 1:")
print(np.linspace(0, 1, 5))
print()

# Calcular la raíz cuadrada de cada elemento
print("Raíz cuadrada de cada elemento:")
print(np.sqrt(array))
print()

# Calcular la exponencial de cada elemento
print("Exponencial de cada elemento:")
print(np.exp(array))
print()

# Concatenar arrays
print("Concatenar dos arrays horizontalmente:")
print(np.hstack((array, array2)))
print()

# Concatenar arrays verticalmente
print("Concatenar dos arrays verticalmente:")
print(np.vstack((array, array2)))
print()

# Dividir el array en sub-arrays
print("Dividir array en 3 sub-arrays:")
print(np.array_split(array, 3))
print()

# Obtener el índice del valor máximo
print("Índice del valor máximo:")
print(np.argmax(array))
print()

# Obtener el índice del valor mínimo
print("Índice del valor mínimo:")
print(np.argmin(array))
print()

# Crear dos arrays de ejemplo
array1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

array2 = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

# Producto punto de dos arrays usando np.dot
print("Producto punto usando np.dot:")
print(np.dot(array1, array2))
print()

# Producto punto de dos arrays usando @
print("Producto punto usando @:")
print(array1 @ array2)
print()

# Sumar arrays usando np.add
print("Suma de arrays usando np.add:")
print(np.add(array1, array2))
print()

# Sumar arrays usando operador +
print("Suma de arrays usando operador +:")
print(array1 + array2)
print()

# Multiplicar arrays elemento a elemento usando np.multiply
print("Multiplicación elemento a elemento usando np.multiply:")
print(np.multiply(array1, array2))
print()

# Multiplicar arrays elemento a elemento usando operador *
print("Multiplicación elemento a elemento usando operador *:")
print(array1 * array2)
print()

# Resta de arrays usando np.subtract
print("Resta de arrays usando np.subtract:")
print(np.subtract(array1, array2))
print()

# Resta de arrays usando operador -
print("Resta de arrays usando operador -:")
print(array1 - array2)
print()

# División elemento a elemento usando np.divide
print("División elemento a elemento usando np.divide:")
print(np.divide(array1, array2))
print()

# División elemento a elemento usando operador /
print("División elemento a elemento usando operador /:")
print(array1 / array2)
print()

# Potencia elemento a elemento usando np.power
print("Potencia elemento a elemento usando np.power:")
print(np.power(array1, 2))
print()

# Potencia elemento a elemento usando operador **
print("Potencia elemento a elemento usando operador **:")
print(array1 ** 2)
print()

# Concatenar arrays horizontalmente usando np.hstack
print("Concatenación horizontal usando np.hstack:")
print(np.hstack((array1, array2)))
print()

# Concatenar arrays horizontalmente usando np.concatenate
print("Concatenación horizontal usando np.concatenate (axis=1):")
print(np.concatenate((array1, array2), axis=1))
print()

# Concatenar arrays verticalmente usando np.vstack
print("Concatenación vertical usando np.vstack:")
print(np.vstack((array1, array2)))
print()

# Concatenar arrays verticalmente usando np.concatenate
print("Concatenación vertical usando np.concatenate (axis=0):")
print(np.concatenate((array1, array2), axis=0))
print()

# Transponer un array usando .T
print("Transponer array usando .T:")
print(array1.T)
print()

# Transponer un array usando np.transpose
print("Transponer array usando np.transpose:")
print(np.transpose(array1))
print()

# Aplanar un array usando .ravel()
print("Aplanar array usando .ravel():")
print(array1.ravel())
print()

# Aplanar un array usando .flatten()
print("Aplanar array usando .flatten():")
print(array1.flatten())
print()
