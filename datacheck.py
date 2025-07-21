#PAÍSES DESARROLLADOS GRUPO A
import wbgapi as wb
info= wb.data.DataFrame(['FIN', 'ISR', 'GBR', 'SAU', 'HUN', 'IND', 'IRL', 'PRT', 'ITA', 'NLD',
 'JPN', 'POL', 'KOR', 'OWID_WRL', 'NZL', 'MEX', 'FRA', 'NOR', 'EST', 'CHE',
 'AUS', 'AUT', 'BEL', 'USA', 'BRA', 'CAN', 'TWN', 'ESP', 'CHN', 'SWE',
 'SVK', 'DEU', 'SGP', 'RUS', 'ARE', 'ISL', 'MYS', 'LVA', 'ARG', 'IDN',
 'GRC', 'DNK', 'CZE', 'CYP', 'CHL', 'ZAF', 'LTU', 'KEN', 'THA', 'TUR', 'BGR'], range(1995,2020), skipBlanks=True, columns='series') # most recent 15 years of inflation data for the USA, CHINA E INDIA
print(info)
#Agregar columna de años
# Guardar el dataframe en un archivo Excel
info.to_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\WorldDataBankGrupoA(1995-2020_expense general).xlsx', index=True)
