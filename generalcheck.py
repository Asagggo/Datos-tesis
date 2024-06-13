#Chequeo de datos de países total
import wbgapi as wb
#Se hace prueba con nueva variable para medir productividad SL.GDP.PCAP.EM.KD
info= wb.data.DataFrame(['SL.UEM.TOTL.ZS', 'FP.CPI.TOTL.ZG', 'SP.POP.GROW', 'NE.CON.GOVT.ZS', 'BX.KLT.DINV.WD.GD.ZS','SL.GDP.PCAP.EM.KD'], ['AUS', 'AUT', 'BEL', 'CAN', 'CHL', 'COL', 'CRI', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ISR', 'ITA', 'JPN', 'KOR', 'LVA', 'LTU', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 'USA', 'DZA', 'AND', 'ARG', 'ARM', 'BLR', 'BMU', 'BIH', 'BRA', 'BGR', 'CYM', 'CHN', 'HRV', 'CUB', 'CYP', 'PRK', 'DJI', 'ECU', 'EGY', 'SLV', 'GEO', 'GTM', 'HKG', 'IND', 'IDN', 'IRN', 'JAM', 'JOR', 'KAZ', 'KEN', 'KWT', 'LBN', 'LIE', 'MYS', 'MLT', 'MDA', 'MCO', 'MNG', 'MAR', 'NGA', 'MKD', 'PAK', 'PAN', 'PER', 'PHL', 'PRI', 'ROU', 'RUS', 'SAU', 'SYC', 'SGP', 'ZAF', 'LKA', 'TWN', 'THA', 'TTO', 'TUN', 'UKR', 'ARE', 'URY', 'UZB', 'VEN', 'ZWE'], range(1980,2021), skipBlanks=True, columns='series') # most recent 15 years of inflation data for the USA, CHINA E INDIA
print(info)
#Agregar columna de años
# Guardar el dataframe en un archivo Excel
info.to_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\DataCheckAllCountries.xlsx', index=True)
