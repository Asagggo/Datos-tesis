# ──────────────────────────────────────────────────────────────
#  Integrar la columna "EIA" al DataFrame principal
#  Autor: ChatGPT · 2025-07-04
# ──────────────────────────────────────────────────────────────
import pandas as pd
from pathlib import Path

# 1) Define la carpeta donde están tus archivos
base_path = Path('.')   # «.» = directorio actual; cámbialo si es necesario

# 2) Nombres de archivo
main_file   = base_path / 'DataframeAbreviada_Con_Grupo_ConID.xlsx'
eia_file    = base_path / 'private-investment-in-artificial-intelligence-cset.xlsx'
output_file = base_path / 'DataframeAbreviada_ConEIA.xlsx'

# 3) Carga los datos
df_main = pd.read_excel(main_file)
df_eia  = pd.read_excel(eia_file)

# 4) Conservar solo las columnas clave en el archivo EIA
#    (PAIS y AÑO son las llaves de unión; EIA es la variable a añadir)
df_eia_subset = df_eia[['PAIS', 'AÑO', 'EIA']]

# 5) Une ambos dataframes (left join para no perder filas del principal)
df_merged = df_main.merge(df_eia_subset, on=['PAIS', 'AÑO'], how='left')

# ── OPCIONAL ── rellena faltantes con 0 si así lo prefieres
# df_merged['EIA'] = df_merged['EIA'].fillna(0)

# 6) Guarda el resultado
df_merged.to_excel(output_file, index=False)
print(f'Archivo combinado guardado en: {output_file}')

# 7) Vista rápida de los primeros registros (opcional)
print('\nVista previa:')
print(df_merged.head())
