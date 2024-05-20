import wbgapi as wb
info= wb.data.DataFrame(['SL.UEM.TOTL.ZS', 'FP.CPI.TOTL.ZG', 'SP.POP.GROW', 'GC.XPN.TOTL.GD.ZS', 'BX.KLT.DINV.WD.GD.ZS'], 'IND', mrv=14, skipBlanks=True, columns='series') # most recent 15 years of inflation data for the USA, CHINA E INDIA
print(info)
# Guardar el dataframe en un archivo Excel
info.to_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Estados Unidos\IND.xlsx', index=False)
# Guardar el dataframe en un archivo Excel