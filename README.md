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
01_EDA_Feature_Engineering.ipynb: Limpieza de datos, análisis exploratorio y creación de nuevas variables (como total_guests, total_stays, room_changed).

02_Modelos_Machine_Learning.ipynb: Comparativa de modelos (Regresión Logística, Random Forest y XGBoost) y optimización final.

Memoria_proyecto_ML.pdf: Documentación detallada del proceso, métricas y conclusiones de negocio.

models/: Contiene los archivos serializados en formato .pkl:

modelo_final_hotel.pkl: El cerebro del modelo.

escalador_hotel.pkl: Transformador para normalizar datos nuevos.

columnas_modelo_final_hotel.pkl: Estructura técnica necesaria para la consistencia de datos.

🚀 Metodología Detallada
1. Feature Engineering (Ingeniería de Variables)
Se procesaron variables críticas para el comportamiento del cliente:

Lead Time: Antelación de la reserva (factor determinante).

Special Requests: El número de peticiones especiales reduce drásticamente la probabilidad de cancelación.

Tipo de Depósito: Identificado como uno de los predictores más fuertes.

2. Selección del Modelo
Se probaron varios algoritmos, descartando opciones basándose en el valor de negocio:

Random Forest: Descartado a pesar de su buen Accuracy, debido a un bajo Recall (45%), lo que lo hacía inútil para prevenir cancelaciones de forma masiva.

XGBoost (Elegido): Configurado con scale_pos_weight para corregir el desbalanceo de clases y maximizar la detección de cancelaciones.

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
