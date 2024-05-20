import wbgapi as wb
info= wb.data.DataFrame(['SL.UEM.TOTL.ZS', 'FP.CPI.TOTL.ZG', 'SP.POP.GROW', 'GC.XPN.TOTL.GD.ZS', 'BX.KLT.DINV.WD.GD.ZS'], 'USA', mrv=10) # most recent 5 years of inflation data for the USA
print(info)