#Importar las librearias necesarias
import pandas as pd
import numpy as np
import sklearn

# Cargar los datos (ejemplo: dataset de productos)
data = pd.read_csv('productos.csv')


# procesamiento de datos
features = data.drop('producto_id', axis=1)  # Eliminar la columna de ID del producto
labels = data['producto_id']  # Etiquetas de los productos

#Dividir los datos en conjuntos de entrenamiento y prueba
train_test_split = sklearn.model_selection.train_test_split(features, labels, test_size=0.2, random_state=42)

# Crear y entrenar un modelo KNeighborsClassifier con 5 vecinos
model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
model.fit(train_test_split[0], train_test_split[2])

# Realizar predicciones con los datos de prueba.
predictions = model.predict(train_test_split[1])

# Evaluar la precisión del modelo (accuracy) e imprimir el resultado
accuracy = sklearn.metrics.accuracy_score(train_test_split[3], predictions)
print(f'Precisión del modelo: {accuracy}')

# Función de recomendación que reciba las características de un producto y retorne la predicción
def recommend_product(features):
    return model.predict([features])[0]

# Ejemplo de uso de la función de recomendación con un producto nuevo
new_product_features = [0.5, 1.2, 3.4]  # Características del nuevo producto
recommended_product_id = recommend_product(new_product_features)
print(f'Producto recomendado: {recommended_product_id}')