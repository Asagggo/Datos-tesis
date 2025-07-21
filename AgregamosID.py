import pandas as pd
import wbgapi as wb
import os

# 1. Cargar el Excel de entrada (mismo directorio que el .py)
input_file  = 'DataframeAbreviada_Con_Grupo.xlsx'
df          = pd.read_excel(input_file)
print("Columnas de entrada:", df.columns.tolist())

# 2. Confirmar que existen PAIS y AÑO
assert 'PAIS' in df.columns and 'AÑO' in df.columns, "Debe haber columnas 'PAIS' y 'AÑO'"

# 3. Preparar listas para descarga
paises = df['PAIS'].astype(str).unique().tolist()
anios  = sorted(df['AÑO'].astype(int).unique().tolist())

# 4. Descargar I+D del World Bank
wb_ser = 'GB.XPD.RSDV.GD.ZS'
datos_id = wb.data.DataFrame(
    wb_ser,
    paises,
    anios,
    skipBlanks=True,
    columns='series'
)

# 5. Aplanar para merge
df_id = datos_id[wb_ser].reset_index()
df_id.rename(columns={'economy':'PAIS', 'time':'AÑO', wb_ser:'I+D'}, inplace=True)

# 6. Limpiar el prefijo "YR" y convertir año a entero
print("Años crudos:", df_id['AÑO'].unique()[:5])
df_id['AÑO'] = df_id['AÑO'].str.replace(r'^YR', '', regex=True)
df_id['AÑO'] = df_id['AÑO'].astype(int)

# 7. Hacer merge por PAIS y AÑO
df_merged = pd.merge(
    df,
    df_id[['PAIS','AÑO','I+D']],
    on=['PAIS','AÑO'],
    how='left'
)

# 8. Insertar columna I+D antes de GRUPO
cols = df_merged.columns.tolist()
if 'I+D' in cols and 'GRUPO' in cols:
    idx = cols.index('GRUPO')
    cols.insert(idx, cols.pop(cols.index('I+D')))
df_merged = df_merged[cols]

# 9. Guardar resultado en el mismo directorio
output_file = 'DataframeAbreviada_Con_Grupo_ConID.xlsx'
df_merged.to_excel(output_file, index=False)
print("✅ Archivo generado en:", os.path.abspath(output_file))
