# Importaciones
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split 

# Crear datos simulados
np.random.seed(42)
entrada = 2 * np.random.rand(100, 1)
salida = 4 + 3 * entrada + np.random.randn(100, 1)

# Separar los datos
entrada_entreno, entrada_prueba, salida_entreno, salida_prueba = train_test_split(
    entrada, salida, test_size=0.2, random_state=42)

# Inicializar modelo
modelo_lineal = LinearRegression()
modelo_lineal.fit(entrada_entreno, salida_entreno)

# Predecir
predicciones = modelo_lineal.predict(entrada_prueba)

# Evaluar
error_medio = mean_squared_error(salida_prueba, predicciones)
print(f"Error Medio Cuadrático (MSE) = {error_medio}")

# Calificación del modelo
if error_medio < 1.0:
    print("Desempeño Aceptable del Modelo (MSE Bajo).")
else:
    print("Desempeño Deficiente del Modelo (MSE Alto).")

# Visualización
plt.scatter(entrada_prueba, salida_prueba, color = 'blue', label = 'Valores Observados')
plt.plot(entrada_prueba, predicciones, color = 'red', label = 'Valores Estimados')
plt.xlabel('Entrada')
plt.ylabel('Salida')
plt.title('Modelo de Regresión Lineal')
plt.legend()
plt.show()