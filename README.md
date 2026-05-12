# hotel-cancellation-prediction
📌 Descripción del Proyecto
Este proyecto desarrolla un modelo de Machine Learning capaz de predecir con alta fiabilidad si una reserva hotelera será cancelada antes de la fecha de llegada.

El problema: Las cancelaciones inesperadas impactan directamente en la rentabilidad y la planificación de recursos del hotel.
La solución: Un sistema predictivo basado en XGBoost que permite al hotel identificar reservas de alto riesgo para activar estrategias de mitigación (overbooking táctico, políticas de prepago o campañas de reconfirmación).

📊 Resultados Clave
Para este problema de negocio, se priorizó la capacidad de detección (Recall) sobre la precisión global, asegurando que el hotel capture la gran mayoría de las posibles bajas.

Recall (Sensibilidad): 87% (Detectamos 9 de cada 10 cancelaciones reales).

Accuracy: 80%

F1-Score: 0.71

Estabilidad: Validación Cruzada (K-fold) con desviación estándar de solo 0.0082.

🛠️ Estructura del Repositorio
src/
├── data/
│   └── hotel_bookings_cleaned.csv       # Dataset procesado tras Feature Engineering
├── notebooks/
│   ├── 01_EDA_Feature_Engineering.ipynb # Análisis exploratorio y transformación de datos
│   └── 02_Modelos_Machine_Learning.ipynb # Entrenamiento, evaluación y tuning de modelos
├── models/
│   ├── modelo_final_hotel.pkl           # Pesos del modelo XGBoost entrenado
│   ├── escalador_hotel.pkl              # StandardScaler para normalización de inputs
│   └── columnas_modelo_final_hotel.pkl  # Listado de variables para asegurar consistencia
├── Memoria_proyecto_ML.pdf              # Documentación técnica y conclusiones de negocio
└── requirements.txt                     # Librerías necesarias para ejecutar el proyecto

🚀 Metodología Detallada
1. Feature Engineering (Ingeniería de Variables)
Se procesaron variables críticas para el comportamiento del cliente.

2. Selección del Modelo
Se probaron varios algoritmos, descartando opciones basándose en el valor de negocio.

💻 Instalación y Uso
Clona el repositorio:

Bash
git clone https://github.com/tu-usuario/hotel-cancellation-prediction-xgboost.git
Instala las dependencias:

Bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
Carga el modelo para predicciones:

Python
import pickle
# Cargar modelo y escalador
model = pickle.load(open('models/modelo_final_hotel.pkl', 'rb'))
scaler = pickle.load(open('models/escalador_hotel.pkl', 'rb'))

✒️ Autora
Nassirdine El Mourif Fatima
