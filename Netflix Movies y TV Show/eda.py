import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

def get_unique_values(column):
    unique_values = set() 
    for value in column.dropna():  
        values = value.split(", ")  
        unique_values.update(values)  
    return unique_values

def replace_country_substrings(value):
    countries = value.split(", ")
    corrected_countries = [country.replace('Soviet Union', 'Russia').replace('West Germany', 'Germany').replace('East Germany', 'Germany') for country in countries]
    return ", ".join(corrected_countries)

wr.filterwarnings('ignore')

# cargando y leyendo el dataset
df = pd.read_csv("netflix_titles.csv")
print(df.head(7))

columns = df.columns
print(columns)
print(df.isnull().sum())

#valores unicos de la columna duration
print(df['duration'].unique())

# llenando los valores nulos
df['director'].fillna('Data Unavailable', inplace=True)
df['cast'].fillna('Data Unavailable', inplace=True)
df['country'].fillna('Data Unavailable', inplace=True)
df['date_added'].fillna('Date Unavailable', inplace=True)
df['rating'].fillna('Date Unavailable', inplace=True)


# dividiendo la columna date_added en dos columnas year_added y month_added
df['year_added'] = df['date_added'].apply(lambda x: x.split(" ")[-1])
df['month_added'] = df['date_added'].apply(lambda x: x.split(" ")[0])
df.drop(['date_added'], axis=1, inplace=True)


#pasando valores de la columna rating a la columna duration y type_unit_duration a filas especificas
shows_id = ['s5542', 's5795', 's5814']
filas_id = df[df['show_id'].isin(shows_id)].index
df.loc[filas_id, 'duration'] = df.loc[filas_id, 'rating']
df.loc[filas_id, 'rating'] = 'NR'

# Usar una expresión regular para separar la columna 'duration' en dos partes
df[['duration_value', 'type_unit_duration']] = df['duration'].str.extract(r'(\d+) (\w+)')

# Reemplazar valores nulos en 'duration_value' y 'type_unit_duration'
df['duration_value'].fillna('0', inplace=True)
df['type_unit_duration'].fillna('Unknown', inplace=True)
df.drop(['duration'], axis=1, inplace=True)


#remplazando valores de la columna rating, cambiando UR a NR
df['rating'] = df['rating'].apply(lambda x: 'NR' if x == 'UR' else x)

# listando valores unicos de la columna country y separando por comas
unique_countries = get_unique_values(df['country'])
print(unique_countries)
unique_listed_in = get_unique_values(df['listed_in'])
print(unique_listed_in)

# Reemplazando inconsistencia en la columna country
df['country'] = df['country'].apply(replace_country_substrings)

 #Verificando los cambios
unique_countries = get_unique_values(df['country'])
print(unique_countries.__contains__('Russia'))
print(unique_countries.__contains__('Soviet Union'))
print(unique_countries.__contains__('West Germany'))





# Guardando el dataset limpio
df.to_csv("netflix_titles_cleaned.csv", index=False)



