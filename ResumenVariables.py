import os
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Cargar datos desde el Excel
# --------------------------------------------------------
ruta_archivo = r"C:\Users\PC\Documents\Documentos Github\Datos-tesis\DataframeEIA_con_grupo.xlsx"

df = pd.read_excel(ruta_archivo)

# --------------------------------------------------------
# 2. Seleccionar variables numéricas de interés
#    (puedes agregar/quitar según tu gusto)
# --------------------------------------------------------
variables_numericas = ["IED", "INF", "CFG", "PL", "TD", "CDP", "EIA"]

# Opcional: incluir el año en la tabla
# variables_numericas = ["AÑO", "IED", "INF", "CFG", "PL", "TD", "CDP", "EIA"]

df_num = df[variables_numericas]

# --------------------------------------------------------
# 3. Crear tabla de estadísticas descriptivas
# --------------------------------------------------------
stats = df_num.describe().T  # Transponer para que cada fila sea una variable

# Nos quedamos con las columnas más usadas
stats = stats[["mean", "std", "min", "25%", "50%", "75%", "max"]]

# Redondeamos para que sea más legible
stats = stats.round(3)

# Renombrar columnas a español (opcional pero recomendable para la tesis)
stats = stats.rename(columns={
    "mean": "Media",
    "std": "Desv.Est.",
    "min": "Mín",
    "25%": "P25",
    "50%": "Mediana",
    "75%": "P75",
    "max": "Máx"
})

stats.index.name = "Variable"

# --------------------------------------------------------
# 4. Crear carpeta de salida (opcional)
# --------------------------------------------------------
carpeta_salida = "salidas_graficas"
os.makedirs(carpeta_salida, exist_ok=True)

# --------------------------------------------------------
# 5. Convertir la tabla en una imagen PNG con matplotlib
# --------------------------------------------------------
# Ajustamos el tamaño de la figura según el número de variables
num_vars = stats.shape[0]
alto_figura = 1.5 + num_vars * 0.4  # puedes ajustar estos factores

fig, ax = plt.subplots(figsize=(10, alto_figura))

# Quitamos ejes
ax.axis('off')

# Creamos la tabla
tabla = ax.table(
    cellText=stats.values,
    rowLabels=stats.index,
    colLabels=stats.columns,
    loc='center'
)

# Estética: tamaño de fuente y escala de la tabla
tabla.auto_set_font_size(False)
tabla.set_fontsize(9)
tabla.scale(1.1, 1.3)  # (ancho, alto) de cada celda

# Título
ax.set_title(
    "Tabla 1. Estadísticas descriptivas de las variables\n",
    fontsize=12,
    fontweight='bold',
    pad=20
)

plt.tight_layout()

# Guardar como PNG
nombre_salida = os.path.join(carpeta_salida, "tabla_estadisticas_resumen.png")
plt.savefig(nombre_salida, dpi=300, bbox_inches='tight')
plt.show()

print("Imagen guardada en:", nombre_salida)
