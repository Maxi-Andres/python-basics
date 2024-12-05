import cv2
import numpy as np

# Cargar una imagen en escala de grises
# cv2.imread() carga una imagen desde el archivo especificado.
# cv2.IMREAD_GRAYSCALE lee la imagen directamente en escala de grises.
img = cv2.imread('BORED APE #3152.png', cv2.IMREAD_GRAYSCALE)
print("Imagen cargada en escala de grises")

# Mostrar una imagen
# cv2.imshow() muestra la imagen en una ventana con el título 'Imagen'.
# cv2.waitKey(0) espera a que se presione una tecla para cerrar la ventana.
# cv2.destroyAllWindows() cierra todas las ventanas de OpenCV.
cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar una imagen
# cv2.imwrite() guarda la imagen en el archivo especificado.
cv2.imwrite('imagen_guardada.jpg', img)
print("Imagen guardada como imagen_guardada.jpg")


image = cv2.imread('BORED APE #3152.png')

# Aplicar transformaciones
colored_image1 = cv2.applyColorMap(image, cv2.COLOR_RGB2BGR)
colored_image2 = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
colored_image3 = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)  # algunos ejemplos
colored_image4 = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
colored_image5 = cv2.applyColorMap(image, cv2.COLORMAP_JET)
colored_image6 = cv2.applyColorMap(image, cv2.COLORMAP_HOT)
colored_image7 = cv2.applyColorMap(image, cv2.COLORMAP_WINTER)

# Mostrar las imágenes
cv2.imshow('Imagen Original', image)
cv2.imshow('Imagen RGB a BGR', colored_image1)
cv2.imshow('Imagen RGB a HSV', colored_image2)  #las ventanas tienen que tener distintos nombres sino se sobreescriben
cv2.imshow('Imagen BGR a YUV', colored_image3)
cv2.imshow('Imagen BGR a Lab', colored_image4)
cv2.imshow('Imagen con COLORMAP_JET', colored_image5)
cv2.imshow('Imagen con COLORMAP_HOT', colored_image6)
cv2.imshow('Imagen con COLORMAP_WINTER', colored_image7)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Redimensionar una imagen
# cv2.resize() cambia el tamaño de la imagen a las dimensiones especificadas (200, 200 píxeles).
resized_img = cv2.resize(img, (200, 200))
print("Imagen redimensionada a 200x200 píxeles")
cv2.imshow('Imagen redimensionada', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertir una imagen a escala de grises
# cv2.cvtColor() convierte la imagen a escala de grises, aunque en este caso ya lo está.
gray_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # Si la imagen ya es gris, esta línea es innecesaria.
print("Imagen convertida a escala de grises")
cv2.imshow('Imagen en escala de grises', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicar desenfoque gaussiano
# cv2.GaussianBlur() aplica un filtro de desenfoque gaussiano. 
# El (5, 5) es el tamaño del kernel, y el 0 es la desviación estándar.
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
print("Imagen con desenfoque gaussiano aplicado")
cv2.imshow('Imagen con desenfoque gaussiano', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detectar bordes con Canny
# cv2.Canny() detecta bordes en una imagen usando el algoritmo de Canny.
# Los parámetros 100 y 200 son los umbrales mínimo y máximo para la detección de bordes.
edges = cv2.Canny(img, 100, 200)
print("Bordes detectados en la imagen")
cv2.imshow('Bordes detectados', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Dibujar un rectángulo
# cv2.rectangle() dibuja un rectángulo en la imagen en las coordenadas especificadas.
# Los puntos (50, 50) y (150, 150) representan la esquina superior izquierda e inferior derecha.
# El color (255, 0, 0) es azul en BGR, y el grosor de línea es 2.
rect_img = img.copy()
cv2.rectangle(rect_img, (50, 50), (150, 150), (255, 0, 0), 2)
print("Rectángulo dibujado en la imagen")
cv2.imshow('Rectángulo dibujado', rect_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Dibujar un círculo
# cv2.circle() dibuja un círculo en la imagen en el centro (100, 100) con radio 50.
# El color es verde en BGR, y el grosor de -1 llena el círculo.
circle_img = img.copy()
cv2.circle(circle_img, (100, 100), 50, (0, 255, 0), -1)
print("Círculo dibujado en la imagen")
cv2.imshow('Círculo dibujado', circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Dibujar una línea
# cv2.line() dibuja una línea desde (0, 0) a (200, 200) con un grosor de 3 píxeles.
line_img = img.copy()
cv2.line(line_img, (0, 0), (200, 200), (0, 0, 255), 3)
print("Línea dibujada en la imagen")
cv2.imshow('Línea dibujada', line_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Escribir texto en una imagen
# cv2.putText() escribe el texto 'OpenCV' en las coordenadas (10, 200).
# El tipo de fuente es cv2.FONT_HERSHEY_SIMPLEX, el tamaño de letra es 1, y el color es blanco.
text_img = img.copy()
cv2.putText(text_img, 'OpenCV', (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
print("Texto 'OpenCV' escrito en la imagen")
cv2.imshow('Texto escrito', text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Transformación de perspectiva
# cv2.getPerspectiveTransform() calcula la transformación de perspectiva.
# pts1 y pts2 son puntos de entrada y salida para el cambio de perspectiva.
pts1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
warped_img = cv2.warpPerspective(img, M, (300, 300))
print("Transformación de perspectiva aplicada")
cv2.imshow('Imagen con transformación de perspectiva', warped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detectar contornos
# cv2.findContours() encuentra los contornos en una imagen binaria.
# cv2.RETR_EXTERNAL recupera solo los contornos externos.
# cv2.CHAIN_APPROX_SIMPLE comprime los segmentos horizontales, verticales y diagonales.
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_img = cv2.drawContours(img.copy(), contours, -1, (255, 0, 0), 2)
print("Contornos detectados y dibujados")
cv2.imshow('Contornos detectados', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crear una máscara binaria
# cv2.threshold() convierte la imagen a una máscara binaria con un umbral de 127.
_, mask = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print("Máscara binaria creada")
cv2.imshow('Máscara binaria', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicar una máscara a la imagen
# cv2.bitwise_and() aplica una operación AND entre la imagen y la máscara.
masked_img = cv2.bitwise_and(img, img, mask=mask)
print("Máscara aplicada a la imagen")
cv2.imshow('Imagen con máscara', masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotar una imagen
# cv2.getRotationMatrix2D() crea una matriz de rotación en torno al centro.
# cv2.warpAffine() aplica la rotación de 45 grados.
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))
print("Imagen rotada 45 grados")
cv2.imshow('Imagen rotada', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detección de caras usando un clasificador Haar
# cv2.CascadeClassifier() carga un clasificador Haar para detección de rostros.
# detectMultiScale() detecta rostros en la imagen.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
print("Rostros detectados y marcados en la imagen")
cv2.imshow('Rostros detectados', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
