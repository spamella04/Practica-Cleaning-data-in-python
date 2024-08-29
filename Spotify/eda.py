import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

wr.filterwarnings('ignore')

# cargando y leyendo el dataset
df = pd.read_csv("Most Streamed Spotify Songs 2024.csv", encoding='ISO-8859-1') #codificacion utilizada en el archivo
print(df.info())
print(df.describe())
print(df.isnull().sum())

#Convirtiendo a string
columnas_string = ['Artist', 'Track', 'Album Name']

for col in columnas_string:
    df[col] = df[col].astype(str)

# Reemplazando caracteres de este tipo ��������������������� por unkonwn
    df[col] = df[col].str.replace(r'[^a-zA-Z0-9\s]', ' ', regex=True)
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True).str.strip()
    df[col] = df[col].replace('', 'Unknown')
    
# llenando valores nulos con 'Unknown'
    df[col] = df[col].fillna('Unknown')

# Convirtiendo a formato numerico entero

columnas_enteras = ['All Time Rank', 'All Time Rank', 'Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'YouTube Views', 'YouTube Likes', 'TikTok Posts','TikTok Likes',
                        'TikTok Views', 'YouTube Playlist Reach', 'AirPlay Spins', 'SiriusXM Spins', 'Deezer Playlist Reach', 'Pandora Streams', 'Pandora Track Stations', 'Shazam Counts', 'Explicit Track']

for col in columnas_enteras:
    df[col] = df[col].astype(str) #convirtiendo a cadena
    df[col] = df[col].str.replace(',', '')  #eliminando comas
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)  # convirtiendo a entero y llenando valores nulos con 0

# Convirtiendo a formato numerico flotante

columnas_float = ['Track Score', 'Apple Music Playlist Count', 'Deezer Playlist Count', 'Deezer Playlist Count', 'Amazon Playlist Count']

for col in columnas_float:
    df[col] = df[col].astype(str) 
    df[col] = df[col].str.replace(',', '')  
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)  

# llenado valores nulos
df['Spotify Streams'] = df['Spotify Streams'].fillna(0)
df['Spotify Playlist Count'] = df['Spotify Playlist Count'].fillna(0)
df['Spotify Playlist Reach'] = df['Spotify Playlist Reach'].fillna(0)
df['Spotify Popularity'] = df['Spotify Popularity'].fillna(0)
df['YouTube Views'] = df['YouTube Views'].fillna(0)
df['YouTube Likes'] = df['YouTube Likes'].fillna(0)
df['TikTok Posts'] = df['TikTok Posts'].fillna(0)
df['TikTok Likes'] = df['TikTok Likes'].fillna(0)        
df['TikTok Views'] = df['TikTok Views'].fillna(0)        
df['YouTube Playlist Reach'] = df['YouTube Playlist Reach'].fillna(0)
df['Apple Music Playlist Count'] = df['Apple Music Playlist Count'].fillna(0)
df['AirPlay Spins'] = df['AirPlay Spins'].fillna(0)
df['SiriusXM Spins'] = df['SiriusXM Spins'].fillna(0)          
df['Deezer Playlist Count'] = df['Deezer Playlist Count'].fillna(0)
df['Deezer Playlist Reach'] = df['Deezer Playlist Reach'].fillna(0)        
df['Amazon Playlist Count'] = df['Amazon Playlist Count'].fillna(0)        
df['Pandora Streams'] = df['Pandora Streams'].fillna(0)
df['Pandora Track Stations'] = df['Pandora Track Stations'].fillna(0)
df['Soundcloud Streams'] = df['Soundcloud Streams'].fillna(0)
df['Shazam Counts'] = df['Shazam Counts'].fillna(0)

# eliminando columna TIDAL Popularity
df.drop(columns=['TIDAL Popularity'], inplace=True) # casi todos los registro tiene null esta columna

# Remplazando valores 0 y 1 en Explicit Track
df['Explicit Track'] = df['Explicit Track'].replace(1, True).replace(0, False)

print(df.isnull().sum())

# Convirtiendo a formato Fecha
df['Release Date'] = pd.to_datetime(df['Release Date'], format='%m/%d/%Y')

# Separando la columna fecha en año, mes y dia
df['Year'] = df['Release Date'].dt.year
df['Month'] = df['Release Date'].dt.strftime('%B')

# Eliminando la columna Release Date
df.drop(columns=['Release Date'], inplace=True)

# Comprobando si hay duplicados.
duplicated_rows = df[df.duplicated(keep=False)]
print(duplicated_rows)
# Borrando los duplicados.
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

#guardando el dataset limpio
df.to_csv('Most Streamed Spotify Songs 2024_clean.csv', index=False)