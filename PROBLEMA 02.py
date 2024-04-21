import pandas as pd
data = pd.read_csv("./winemag-data-130k-v2.csv")
data.head()
data.dtypes
# Mostrar las primeras filas del DataFrame
print(data.head())
# Obtener información sobre el DataFrame
print(data.info())
# Obtener estadísticas descriptivas del DataFrame
print(data.describe())
# Renombrar columnas
data.rename(columns={'country': 'pais', 'points': 'puntuacion', 'variety': 'variedad', 'winery': 'bodega'}, inplace=True)

# Crear nuevas columnas
data['precio_usd'] = data['price'] * tipo_de_cambio_dolar 
 # Suponiendo que ya tenemos el tipo de cambio del dólar
data['rango_puntuacion'] = pd.cut(data['puntuacion'], bins=[0, 85, 90, 95, 100], labels=['bajo', 'medio', 'alto', 'máximo'])
data['longitud_descripcion'] = data['description'].apply(lambda x: len(x))
# Reporte 1: Promedio de puntuación por país
reporte1 = data.groupby('pais')['puntuacion'].mean()

# Reporte 2: Máximo precio por variedad de vino
reporte2 = data.groupby('variedad')['price'].max()

# Reporte 3: Cantidad de vinos por rango de puntuación
reporte3 = data.groupby('rango_puntuacion').size()

# Reporte 4: Suma de precios por provincia
reporte4 = data.groupby('province')['price'].sum()

# Almacenar el Reporte 1 en un archivo Excel
reporte1.to_excel('promedio_puntuacion_por_pais.xlsx')