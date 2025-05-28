import pandas as pd

# Cargar el archivo Excel
file_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\DataframeAbreviada.xlsx'
data = pd.read_excel(file_path)

# Lista de países a mantener
paises_a_mantener = ['AUS', 'AUT', 'BEL', 'CAN', 'CHE', 'CYP', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HKG', 'IRL', 'ISL', 'ISR', 'ITA', 'JPN', 'KOR', 'LTU', 'LVA', 'MLT', 'NLD', 'NOR', 'NZL', 'POL', 'SGP', 'SVN', 'SWE', 'USA']

  #países a filtrar

# Filtrar el DataFrame
data_filtrada = data[data['PAÍS'].isin(paises_a_mantener)]

# Guardar el DataFrame filtrado en un nuevo archivo de Excel
ruta_salida = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Grupo 1\Grupo_1_Abrv.xlsx'
data_filtrada.to_excel(ruta_salida, index=False)

print(f"Archivo filtrado guardado en: {ruta_salida}")