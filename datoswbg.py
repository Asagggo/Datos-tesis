import wbgapi as wb
import pandas as pd
import openpyxl as op

# Obtener el dataframe
inflation = wb.data.DataFrame('SP.POP.SCIE.RD.P6', 'USA')

print (inflation)

# Guardar el dataframe en un archivo Excel
inflation.to_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\USA\USATECH.xlsx', index=False)
