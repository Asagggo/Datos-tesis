import pandas as pd

# Cargar el archivo Excel
file_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Dataframe completo (Indicadores World Data Bank y Numero de patentes por país y año).xlsx'
data = pd.read_excel(file_path)

# Lista de países a mantener
paises_a_mantener = ['ARM', 'BGR', 'BLR', 'BRA', 'CHL', 'CHN', 'COL', 'CRI', 'DZA', 'ECU', 'EGY', 'GTM', 'HRV', 'HUN', 'IDN', 'IND', 'IRN', 'KAZ', 'KEN', 'MAR', 'MDA', 'MEX', 'MKD', 'MNG', 'MYS', 'PAK', 'PER', 'PHL', 'PRT', 'ROU', 'RUS', 'SAU', 'SVK', 'THA', 'TUN', 'TUR', 'UKR', 'ZAF']
  #países a filtrar

# Filtrar el DataFrame
data_filtrada = data[data['country'].isin(paises_a_mantener)]

# Guardar el DataFrame filtrado en un nuevo archivo de Excel
ruta_salida = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Grupo 2\Grupo_2.xlsx'
data_filtrada.to_excel(ruta_salida, index=False)

print(f"Archivo filtrado guardado en: {ruta_salida}")