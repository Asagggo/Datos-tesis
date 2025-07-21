import wbgapi as wb
import pandas as pd

# Lista de países con datos EIA en al menos 8 años (ISO-3)
countries = ['FIN', 'ISR', 'GBR', 'SAU', 'HUN', 'IND', 'IRL', 'PRT', 'ITA', 'NLD',
             'JPN', 'POL', 'KOR', 'NZL', 'MEX', 'FRA', 'NOR', 'EST', 'CHE',
             'AUS', 'AUT', 'BEL', 'USA', 'BRA', 'CAN', 'TWN', 'ESP', 'CHN', 'SWE',
             'SVK', 'DEU', 'SGP', 'RUS', 'ARE', 'ISL', 'MYS', 'LVA', 'ARG', 'IDN',
             'GRC', 'DNK', 'CZE', 'CYP', 'CHL', 'ZAF', 'LTU', 'KEN', 'THA', 'TUR', 'BGR']

# Indicadores del World Bank según tus variables del modelo
indicators = {
    'SL.UEM.TOTL.ZS': 'TD',            # Tasa de desempleo (% población activa)
    'FP.CPI.TOTL.ZG': 'INF',           # Inflación (% IPC)
    'NE.CON.GOVT.ZS': 'CFG',           # Consumo final del gobierno (% PIB)
    'SP.POP.GROW': 'CDP',              # Crecimiento de la población (% anual)
    'BX.KLT.DINV.WD.GD.ZS': 'IED',     # IED neta (% PIB)
    'SL.GDP.PCAP.EM.KD': 'PL'          # PIB por persona empleada (USD constantes)
}

# Años del análisis
years = range(2014, 2024)  # 2014 a 2023

# Descargar los datos desde WDI
df = wb.data.DataFrame(indicators.keys(), countries, years, labels=True, columns='series', skipBlanks=True)

# Renombrar variables a nombres de tu modelo
df.rename(columns=indicators, inplace=True)

# Acomodar los índices como columnas: 'PAIS' y 'AÑO'
df.reset_index(inplace=True)
df.rename(columns={'economy': 'PAIS', 'time': 'AÑO'}, inplace=True)

# Guardar en archivo Excel
output_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\WorldDataBank_GrupoA(2014-2023).xlsx'
df.to_excel(output_path, index=False)

print(f"✅ Datos descargados correctamente.\n📁 Guardados en: {output_path}")
