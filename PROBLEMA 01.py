#CASO 01
# Ejercicio - Busqueda de Alojamiento en Airbnb.

#Supongamos que somos un agente de [Airbnb](http://www.airbnb.com) localizado en Lisboa, y tenemos que atender peticiones de varios clientes. Tenemos un archivo llamado `airbnb.csv` (en la carpeta data) donde tenemos información de todos los alojamientos de Airbnb en Lisboa.
import pandas as pd
df_airbnb = pd.read_csv("./airbnb.csv")
df_airbnb.head()
# Paso 1: Filtrar habitaciones con más de 10 críticas y puntuación mayor de 4
habitaciones_filtradas = df_airbnb[(df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4)]

# Paso 2: Ordenar habitaciones por puntuación y número de críticas
habitaciones_ordenadas = habitaciones_filtradas.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

# Paso 3: Seleccionar las tres mejores alternativas
tres_mejores_alternativas = habitaciones_ordenadas.head(3)

# Mostrar las tres mejores alternativas
print(tres_mejores_alternativas)

#CASO 02
# Paso 1: Filtrar las propiedades de Roberto y Clara
propiedades_roberto = df_airbnb[df_airbnb['host_id'] == 97503]
propiedades_clara = df_airbnb[df_airbnb['host_id'] == 90387]

# Paso 2: Crear un nuevo DataFrame con las propiedades de ambos
propiedades_roberto_clara = pd.concat([propiedades_roberto, propiedades_clara])

# Paso 3: Guardar el DataFrame como un archivo Excel
propiedades_roberto_clara.to_excel("roberto.xls", index=False)


#CASO 03
# Paso 1: Filtrar propiedades con precio igual o inferior a 50€
propiedades_baratas = df_airbnb[df_airbnb['price'] <= 50]

# Paso 2: Filtrar las habitaciones compartidas
habitaciones_compartidas = propiedades_baratas[propiedades_baratas['room_type'] == 'Shared room']

# Paso 3: Ordenar las habitaciones compartidas por puntuación de mayor a menor
habitaciones_compartidas_ordenadas = habitaciones_compartidas.sort_values(by='overall_satisfaction', ascending=False)

# Paso 4: Seleccionar las 10 propiedades más baratas
diez_propiedades_baratas = habitaciones_compartidas_ordenadas.head(10)

# Mostrar las 10 propiedades más baratas
print(diez_propiedades_baratas)