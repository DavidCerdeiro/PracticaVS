import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde CSV
df = pd.read_csv('SensorData.csv')

plt.plot(df['Timestamp'], df['Temperature'], label='Temperatura')
plt.plot(df['Timestamp'], df['Humidity'], label='Humedad')

plt.title('Datos del Sensor')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Guardar grafica
plt.savefig('grafica_sensor.png')