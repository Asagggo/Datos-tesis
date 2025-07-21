import pandas as pd
from pathlib import Path

# Definir carpeta de trabajo actual
base_path = Path().resolve()

# 1. Cargar archivos
df_macro = pd.read_excel(base_path / "WorldDataBank_GrupoA(2014-2023).xlsx")
df_eia = pd.read_excel(base_path / "private-investment-in-artificial-intelligence-cset.xlsx")

# 2. Limpiar columna 'AÑO' en archivo macro (quitar prefijo 'YR' si existe)
df_macro['AÑO'] = df_macro['AÑO'].astype(str).str.extract(r'(\d{4})').astype(int)
df_macro['PAIS'] = df_macro['PAIS'].astype(str)

# 3. Asegurar tipos consistentes en archivo EIA
df_eia['AÑO'] = df_eia['AÑO'].astype(int)
df_eia['PAIS'] = df_eia['PAIS'].astype(str)

# 4. Eliminar duplicados en EIA por seguridad
df_eia = df_eia.drop_duplicates(subset=['PAIS', 'AÑO'])

# 5. Realizar la fusión por 'PAIS' y 'AÑO'
df_merged = df_macro.merge(df_eia[['PAIS', 'AÑO', 'EIA']], on=['PAIS', 'AÑO'], how='left')

# 6. Guardar el resultado
output_path = base_path / "WorldDataBank_GrupoA_ConEIA(2014-2023).xlsx"
df_merged.to_excel(output_path, index=False)

# Confirmación
print(f"✅ Archivo fusionado guardado exitosamente en:\n{output_path}")
