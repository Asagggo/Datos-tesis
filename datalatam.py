import wbgapi as wb
info= wb.data.DataFrame(['SL.UEM.TOTL.ZS', 'FP.CPI.TOTL.ZG', 'SP.POP.GROW', 'NE.CON.GOVT.ZS', 'BX.KLT.DINV.WD.GD.ZS'], ['BOL', 'BRA', 'CHL', 'COL', 'CRI', 'DOM', 'ECU', 'SLV', 'GTM', 'HND', 'MEX', 'NIC', 'PRY', 'PER'], range(2000,2023), skipBlanks=True, columns='series') # most recent 15 years of inflation data for the USA, CHINA E INDIA
print(info)
#Agregar columna de años
# Guardar el dataframe en un archivo Excel
info.to_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\WorldDataBankLatam14(expense general).xlsx', index=True)
