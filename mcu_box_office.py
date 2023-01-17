#Importar Pandas
import pandas as pd

#Leer CSV con pandas y settear la columna 'movie_title' como índice del df
df_1 = pd.read_csv('mcu_box_office.csv')
df_1 = df_1.set_index('movie_title')
# print(df_1)

print('---'*50)

# Exploración de df_1
print('\nMuestra de datos')
print(df_1.head())
print('\nFormato del dataframe')
print(df_1.shape)
print('\nNombres de las columnas')
print(df_1.columns)
print('\nBúsqueda de valores nulls por columna')
print(df_1.isnull().sum())
print('\nBúsqueda de valores faltantes por columna')
print(df_1.isna().any())
print('\nFormato de los datos por columna')
print(df_1.dtypes)

print('---'*50)

#Convertir las recaudaciones de 'object' a 'float'
df_1['production_budget'] = df_1['production_budget'].str.split(',').str.join("").astype(float)
df_1['opening_weekend'] = df_1['opening_weekend'].str.split(',').str.join("").astype(float)
df_1['domestic_box_office'] = df_1['domestic_box_office'].str.split(',').str.join("").astype(float)
df_1['worldwide_box_office'] = df_1['worldwide_box_office'].str.split(',').str.join("").astype(float)

#Convertir fecha de estreno de 'object' a 'datetime'
df_1.release_date = pd.to_datetime(df_1.release_date)

print('\nFormato de los datos por columna convertidos')
print(df_1.dtypes)

print('---'*50)

#Estadísticos descriptivos
pd.options.display.float_format= '{:,.2f}'.format
print('\nEstadísticos descriptivos')
print(df_1.describe())

print('---'*50)

#Exploración
print('\nTop 5 películas que más recaudaron')
df_2 = df_1.sort_values('worldwide_box_office', ascending=False)
print(df_2[['worldwide_box_office']].head())

print('\nTop 5 películas que menos recaudaron')
df_2 = df_1.sort_values('worldwide_box_office', ascending=True)
print(df_2[['worldwide_box_office']].head())