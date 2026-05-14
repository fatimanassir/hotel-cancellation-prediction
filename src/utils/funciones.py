# Función check missings en mi dataset
def check_missings(data):
    """
    Calcula nulos totales y porcentaje de cada columna que presente missings.
    Siguiendo el punto 11 de la guía de ML.
    """
     # 1. Calculamos nulos totales por columna
    # data.isnull() → devuelve True/False (True si es nulo)
    # .sum() → cuenta los True (porque True = 1)
    # 1. Calculamos nulos totales
    missings = data.isnull().sum()
    
    
    # 2. Filtramos solo las que tienen nulos > 0
     # missings > 0 → condición
    # nos quedamos solo con esas columnas
    missings = missings[missings > 0]
    
    # Si no hay columnas con nulos
    if missings.empty:
        
        return "No se encontraron valores nulos."
    
    # 3. Creamos un DataFrame para visualizar los resultados
    reporte_nulos = pd.DataFrame({
         # Número total de nulos por columna
        'Nulos': missings,
        # Porcentaje de nulos:
        # missings / len(data) → divide por número de filas
        # * 100 → lo convierte en %
        # .round(2) → redondea a 2 decimales
        'Porcentaje (%)': (missings / len(data) * 100).round(2)
        
    # Ordenamos de mayor a menor número de nulos    
    }).sort_values(by='Nulos', ascending=False)
    
    return reporte_nulos


# Definimos funcion eliminar columnas

def borrar_columnas(data, lista_columnas):
    """
    Elimina columnas específicas de un DataFrame.

    Parámetros:
    -----------
    data : pandas.DataFrame
        DataFrame del que se desean eliminar columnas.

    lista_columnas : list
        Lista con los nombres de las columnas que se quieren borrar.

    Retorna:
    --------
    pandas.DataFrame
        DataFrame sin las columnas indicadas.
    """
    # errors='ignore' hace que si la columna no existe, simplemente la salte
    return data.drop(columns=lista_columnas, errors='ignore')

# --- Ejemplo de uso ---
columnas_a_eliminar = ['company']


