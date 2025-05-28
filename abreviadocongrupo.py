import pandas as pd
import os

# Ruta al archivo de entrada
input_file_path = r'C:\Users\adria\OneDrive\Documentos\Tesis docs\Data modelo tesis\DataframeAbreviada.xlsx'

# Verifica si el archivo de entrada existe
if not os.path.exists(input_file_path):
    raise FileNotFoundError(f"❌ El archivo de entrada no existe: {input_file_path}")

# Cargar el archivo Excel
dataframe = pd.read_excel(input_file_path)

# Diccionario de grupos por país
group_map = {
    "ARM": 2, "AUS": 1, "AUT": 1, "BEL": 1, "BGR": 2, "BLR": 2, "BRA": 2, "CAN": 1, "CHE": 1, "CHL": 1,
    "CHN": 2, "COL": 2, "CRI": 2, "CYP": 1, "CZE": 1, "DEU": 1, "DNK": 1, "DZA": 2, "ECU": 2, "EGY": 2,
    "ESP": 1, "EST": 1, "FIN": 1, "FRA": 1, "GBR": 1, "GRC": 1, "GTM": 2, "HKG": 1, "HRV": 1, "HUN": 1,
    "IDN": 2, "IND": 2, "IRL": 1, "IRN": 2, "ISL": 1, "ISR": 1, "ITA": 1, "JPN": 1, "KAZ": 2, "KEN": 2,
    "KOR": 1, "LTU": 1, "LVA": 1, "MAR": 2, "MDA": 2, "MEX": 2, "MKD": 2, "MLT": 1, "MNG": 2, "MYS": 2,
    "NLD": 1, "NOR": 1, "NZL": 1, "PAK": 2, "PER": 2, "PHL": 2, "POL": 1, "PRT": 1, "ROU": 2, "RUS": 2,
    "SAU": 1, "SGP": 1, "SVK": 1, "SVN": 1, "SWE": 1, "THA": 2, "TUN": 2, "TUR": 2, "UKR": 2, "USA": 1,
    "ZAF": 2
}

# Crear columna con grupo según país
dataframe['Grupo'] = dataframe['PAÍS'].map(group_map)

# NUEVA RUTA SEGURA: guardar en Escritorio
output_folder = r'C:\Users\adria\OneDrive\Escritorio'
os.makedirs(output_folder, exist_ok=True)

output_file_path = os.path.join(output_folder, 'DataframeAbreviada_Con_Grupo.xlsx')
dataframe.to_excel(output_file_path, index=False)

print(f"✅ Archivo guardado exitosamente en:\n{output_file_path}")
