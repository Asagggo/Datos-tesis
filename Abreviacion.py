import pandas as pd

# Cargar el archivo Excel original y el de abreviaciones
file_path_data = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Dataframe completo (Indicadores World Data Bank y Numero de patentes por país y año).xlsx'
file_path_abreviaciones = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Lista de codigos y abreviaciones.xlsx'
data = pd.read_excel(file_path_data)
abreviaciones = pd.read_excel(file_path_abreviaciones)

# Crear un diccionario de mapeo de los códigos a sus abreviaciones
mapeo_abreviaciones = dict(zip(abreviaciones['Código de la Variable'], abreviaciones['Abreviación']))

# Renombrar las columnas del DataFrame original
data_renombrada = data.rename(columns=mapeo_abreviaciones)

# Guardar el DataFrame con los nombres de columnas actualizados en un nuevo archivo de Excel
ruta_salida = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\DataframeAbreviada.xlsx'
data_renombrada.to_excel(ruta_salida, index=False)

print(f"Archivo renombrado guardado en: {ruta_salida}")
