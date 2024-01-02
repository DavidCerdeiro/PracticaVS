import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar datos desde CSV
df = pd.read_csv('SensorData.csv')

plt.plot(df['timestamp'], df['temperatureSHT31'], label='Temperatura')
plt.plot(df['timestamp'], df['humiditySHT31'], label='Humedad')

plt.title('Datos del Sensor')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Obtener la ruta al directorio del script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Guardar la gráfica en el directorio superior
plt.savefig(os.path.join(script_directory, '..', 'grafica_sensor.png'))