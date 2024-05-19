import wbdata
import pandas as pd
from datetime import datetime

# Definir el rango de fechas
start_date = datetime(2005, 1, 1)
end_date = datetime(2023, 12, 31)

# Obtener los datos de inflación mensual para Estados Unidos
data = wbdata.get_dataframe(indicators={'FP.CPI.TOTL': 'CPI'},
                            country='USA',
                            data_date=(start_date, end_date),
                            convert_date=True,
                            freq='M')  # freq='M' para datos mensuales

# Mostrar los datos
print(data)
