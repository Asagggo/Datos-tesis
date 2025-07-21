import wbgapi as wb
import pandas as pd
from pathlib import Path

# Lista de países con datos EIA consistentes
countries = ['FIN', 'ISR', 'GBR', 'SAU', 'HUN', 'IND', 'IRL', 'PRT', 'ITA', 'NLD',
             'JPN', 'POL', 'KOR', 'NZL', 'MEX', 'FRA', 'NOR', 'EST', 'CHE',
             'AUS', 'AUT', 'BEL', 'USA', 'BRA', 'CAN', 'TWN', 'ESP', 'CHN', 'SWE',
             'SVK', 'DEU', 'SGP', 'RUS', 'ARE', 'ISL', 'MYS', 'LVA', 'ARG', 'IDN',
             'GRC', 'DNK', 'CZE', 'CYP', 'CHL', 'ZAF', 'LTU', 'KEN', 'THA', 'TUR', 'BGR']

# Indicadores del modelo (World Bank codes)
indicators = {
    'SL.UEM.TOTL.ZS': 'TD',            # Tasa de desempleo
    'FP.CPI.TOTL.ZG': 'INF',           # Inflación
    'NE.CON.GOVT.ZS': 'CFG',           # Gasto público
    'SP.POP.GROW': 'CDP',              # Crecimiento población
    'BX.KLT.DINV.WD.GD.ZS': 'IED',     # IED
    'SL.GDP.PCAP.EM.KD': 'PL'          # PIB por persona empleada
}

# Rango de años
years = range(2014, 2024)

# Descargar datos desde el World Bank
df = wb.data.DataFrame(indicators.keys(), countries, years, labels=True, columns='series', skipBlanks=True)

# Renombrar las columnas
df.rename(columns=indicators, inplace=True)

# Reindexar y renombrar columnas de clave
df.reset_index(inplace=True)
df.rename(columns={'economy': 'PAIS', 'time': 'AÑO'}, inplace=True)

# Crear ruta para guardar el archivo en la misma carpeta de trabajo
output_path = Path().resolve() / "WorldDataBank_GrupoA(2014-2023).xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Datos guardados correctamente en:\n{output_path}")
