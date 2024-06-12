import requests
import pandas as pd
import xml.etree.ElementTree as ET

# URL de la consulta generada con el SDMX flavor "Flat"
url = "https://sdmx.oecd.org/public/rest/data/OECD.STI.PIE,DSD_PATENTS@DF_PATENTS_OECDSPECIFIC,1.0/9P50_1.A.AP.PATN.PRIORITY.AUT+BEL+CAN+CHL+COL+CRI+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EU27_2020+OECD+WXOECD+DZA+AND+ARG+ARM+BLR+BMU+BIH+BRA+BGR+CYM+CHN+HRV+CUB+CYP+PRK+DJI+ECU+EGY+SLV+GEO+GTM+HKG+IND+IDN+IRN+JAM+JOR+KAZ+KEN+KWT+LBN+LIE+MYS+MLT+MDA+MCO+MNG+MAR+NGA+MKD+PAK+PAN+PER+PHL+PRI+ROU+RUS+SAU+SYC+SGP+ZAF+LKA+TWN+THA+TTO+TUN+UKR+ARE+URY+UZB+VEN+ZWE+W+AUS+MEX..INVENTOR...NANOTECH?startPeriod=1980&endPeriod=2020&dimensionAtObservation=AllDimensions"

try:
    # Realizar la solicitud GET a la URL
    response = requests.get(url)

    # Comprobar que la solicitud fue exitosa
    if response.status_code == 200:
        # Imprimir el contenido de la respuesta para verificar
        print("Contenido de la respuesta:")
        print(response.text)
        
        try:
            # Parsear el contenido XML
            root = ET.fromstring(response.content)

            # Extraer las observaciones
            data = []
            for obs in root.findall('.//generic:Obs', namespaces={'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}):
                obs_data = {}
                for value in obs.findall('.//generic:Value', namespaces={'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}):
                    obs_data[value.get('id')] = value.get('value')
                obs_data['OBS_VALUE'] = obs.find('.//generic:ObsValue', namespaces={'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}).get('value')
                data.append(obs_data)
            
            # Convertir la lista de diccionarios en un DataFrame de pandas
            df = pd.DataFrame(data)
            
            # Guardar el DataFrame en un archivo Excel
            df.to_excel('oecd_data.xlsx', index=False)
            print("Datos guardados exitosamente en 'oecd_data.xlsx'")
        except ET.ParseError as e:
            print("Error al parsear el XML:", e)
    else:
        print(f"Error al acceder a la API: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
