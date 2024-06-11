from pytrends.request import TrendReq as UTrendReq
import pandas as pd
import time

# Encabezados HTTP y cookies personalizados obtenidos de cURL
cookies = {
    '__utma': '10102256.19699981.1718135400.1718135466.1718135466.1',
    '__utmc': '10102256',
    '__utmz': '10102256.1718135466.1.1.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmt': '1',
    '__utmb': '10102256.8.9.1718135500126',
    'SID': 'g.a000kQgUExEBzmNEAoDdguRg24YfcPrEqICe_dOibj9xgTB40pwkkr0-F7X1lJ1ozjalnwgHvwACgYKAeASARASFQHGX2MitDfRbigKzhi_jIJni-W2qxoVAUF8yKo8EOfAiP-aAMcJSNuz_GCw0076',
    '__Secure-1PSID': 'g.a000kQgUExEBzmNEAoDdguRg24YfcPrEqICe_dOibj9xgTB40pwkGycjcHh0LakQ-kahtiiGWQACgYKAS0SARASFQHGX2MixQR28G33cSHrJT0WUe1HHxoVAUF8yKp9D-2p0DzcGOURk6IltmkH0076',
    '__Secure-3PSID': 'g.a000kQgUExEBzmNEAoDdguRg24YfcPrEqICe_dOibj9xgTB40pwkC0jgIVLItH30aU04WnOJhgACgYKAQcSARASFQHGX2MiOjTL3EwWC7_JwXWe1FauFBoVAUF8yKq3vR3fWyevISWnBm1FyPWh0076',
    'HSID': 'AqVov6cMRWfEtjEVY',
    'SSID': 'AM6byV6tYzvbKm50s',
    'APISID': 'oNhKfb2fOnq0_ufi/AHunDEoAsiIQey6QC',
    'SAPISID': 'IBCn9UMWuT-Uuidj/AmdkGSj5I7xc1t2t8',
    '__Secure-1PAPISID': 'IBCn9UMWuT-Uuidj/AmdkGSj5I7xc1t2t8',
    '__Secure-3PAPISID': 'IBCn9UMWuT-Uuidj/AmdkGSj5I7xc1t2t8',
    'SEARCH_SAMESITE': 'CgQIq5sB',
    'AEC': 'AQTF6Hxhrl43DYlaRgDGRdKO__Nr0TQClDEpVw9h968sz5drJvSiLGTk7g',
    '__Secure-1PSIDTS': 'sidts-CjIB3EgAEqVc4Btg6AW-5SIkqpLJp8LHN3GI08km6U9JOdPFFNma7DLQOAKE3B8Fa1ScOhAA',
    '__Secure-3PSIDTS': 'sidts-CjIB3EgAEqVc4Btg6AW-5SIkqpLJp8LHN3GI08km6U9JOdPFFNma7DLQOAKE3B8Fa1ScOhAA',
    '1P_JAR': '2024-06-11-19',
    'NID': '514=Hr45ZUgVKQUAvBBpVvScnYKxqXPVzWLDoPFbnBEnMEMVZGqFc-lE9GCtDFUknuZ5bUuaVgkszLZzJuxsN-YKJeaXupmFLqkGjx0Do16BqX_NNaVA9hKhRZZinMf7itW332W8n01fFxppLHrt6qCCTy8iZxPcE8__m4n2ujZ5MruTXmmkfAsLq0E8qBwRtNdnWfQGc0Lzx3ACstXGSrsPQJdohl8wC_ToHfmC0pe2B67NSo2LT16j7TgMsFg1mMdb_gmrIkcc5H0-g56VHG8GqO1ZTcPeysEN6tWh4BNCkdanAUwgHmg0H_Reo7Ai1vPu6Gu0-ch3Ap-QkvhB0cI0_xPKIfeeCA4bn1M8CyGXY0J0thhaoaXLvQHiykV5u2vp4a7ElntFZ4mk6hbZJEQef8IUroCtfI6j_ZHMFfa5',
    '_gid': 'GA1.3.282072054.1718135400',
    'OTZ': '7597190_80_80_134400_76_436740',
    '_gat_gtag_UA_4401283': '1',
    '_ga': 'GA1.3.19699981.1718135400',
    '_ga_VWZPXDNJJB': 'GS1.1.1718135399.1.1.1718135500.0.0.0',
    'SIDCC': 'AKEyXzWbf-UA1sz3JSjAZ5N-KMAnKprK9_-4EIBRcYxaOWoQjStr6FEdG_LsNhDnYmJR73UxJ8o',
    '__Secure-1PSIDCC': 'AKEyXzVJCwxrezRk5V2xv_83SjRtBtZBZgdnfETfV0D77CWDzQyQrbzQBV7KRoslwgkRUDEHRg',
    '__Secure-3PSIDCC': 'AKEyXzWrf1dJtbckzvrI4ZQktZnRm5-6KS6za5a5Rw8yvaMJgps2RCPbH8Ue4gdnmxBFEMEYyQ',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    # 'cookie': '__utma=10102256.19699981.1718135400.1718135466.1718135466.1; __utmc=10102256; __utmz=10102256.1718135466.1.1.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=10102256.8.9.1718135500126; SID=g.a000kQgUExEBzmNEAoDdguRg24YfcPrEqICe_dOibj9xgTB40pwkkr0-F7X1lJ1ozjalnwgHvwACgYKAeASARASFQHGX2MitDfRbigKzhi_jIJni-W2qxoVAUF8yKo8EOfAiP-aAMcJSNuz_GCw0076; __Secure-1PSID=g.a000kQgUExEBzmNEAoDdguRg24YfcPrEqICe_dOibj9xgTB40pwkGycjcHh0LakQ-kahtiiGWQACgYKAS0SARASFQHGX2MixQR28G33cSHrJT0WUe1HHxoVAUF8yKp9D-2p0DzcGOURk6IltmkH0076; __Secure-3PSID=g.a000kQgUExEBzmNEAoDdguRg24YfcPrEqICe_dOibj9xgTB40pwkC0jgIVLItH30aU04WnOJhgACgYKAQcSARASFQHGX2MiOjTL3EwWC7_JwXWe1FauFBoVAUF8yKq3vR3fWyevISWnBm1FyPWh0076; HSID=AqVov6cMRWfEtjEVY; SSID=AM6byV6tYzvbKm50s; APISID=oNhKfb2fOnq0_ufi/AHunDEoAsiIQey6QC; SAPISID=IBCn9UMWuT-Uuidj/AmdkGSj5I7xc1t2t8; __Secure-1PAPISID=IBCn9UMWuT-Uuidj/AmdkGSj5I7xc1t2t8; __Secure-3PAPISID=IBCn9UMWuT-Uuidj/AmdkGSj5I7xc1t2t8; SEARCH_SAMESITE=CgQIq5sB; AEC=AQTF6Hxhrl43DYlaRgDGRdKO__Nr0TQClDEpVw9h968sz5drJvSiLGTk7g; __Secure-1PSIDTS=sidts-CjIB3EgAEqVc4Btg6AW-5SIkqpLJp8LHN3GI08km6U9JOdPFFNma7DLQOAKE3B8Fa1ScOhAA; __Secure-3PSIDTS=sidts-CjIB3EgAEqVc4Btg6AW-5SIkqpLJp8LHN3GI08km6U9JOdPFFNma7DLQOAKE3B8Fa1ScOhAA; 1P_JAR=2024-06-11-19; NID=514=Hr45ZUgVKQUAvBBpVvScnYKxqXPVzWLDoPFbnBEnMEMVZGqFc-lE9GCtDFUknuZ5bUuaVgkszLZzJuxsN-YKJeaXupmFLqkGjx0Do16BqX_NNaVA9hKhRZZinMf7itW332W8n01fFxppLHrt6qCCTy8iZxPcE8__m4n2ujZ5MruTXmmkfAsLq0E8qBwRtNdnWfQGc0Lzx3ACstXGSrsPQJdohl8wC_ToHfmC0pe2B67NSo2LT16j7TgMsFg1mMdb_gmrIkcc5H0-g56VHG8GqO1ZTcPeysEN6tWh4BNCkdanAUwgHmg0H_Reo7Ai1vPu6Gu0-ch3Ap-QkvhB0cI0_xPKIfeeCA4bn1M8CyGXY0J0thhaoaXLvQHiykV5u2vp4a7ElntFZ4mk6hbZJEQef8IUroCtfI6j_ZHMFfa5; _gid=GA1.3.282072054.1718135400; OTZ=7597190_80_80_134400_76_436740; _gat_gtag_UA_4401283=1; _ga=GA1.3.19699981.1718135400; _ga_VWZPXDNJJB=GS1.1.1718135399.1.1.1718135500.0.0.0; SIDCC=AKEyXzWbf-UA1sz3JSjAZ5N-KMAnKprK9_-4EIBRcYxaOWoQjStr6FEdG_LsNhDnYmJR73UxJ8o; __Secure-1PSIDCC=AKEyXzVJCwxrezRk5V2xv_83SjRtBtZBZgdnfETfV0D77CWDzQyQrbzQBV7KRoslwgkRUDEHRg; __Secure-3PSIDCC=AKEyXzWrf1dJtbckzvrI4ZQktZnRm5-6KS6za5a5Rw8yvaMJgps2RCPbH8Ue4gdnmxBFEMEYyQ',
    'priority': 'u=1, i',
    'referer': 'https://trends.google.com/trends/explore?date=now%201-d&geo=US&q=ChatGP&hl=en',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"125.0.6422.142"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="125.0.6422.142", "Chromium";v="125.0.6422.142", "Not.A/Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-client-data': 'CIe2yQEIorbJAQipncoBCJnhygEIlaHLAQj/mM0BCIWgzQEI4ZPOAQjok84BCNSYzgEI75vOAQiRnc4BGNfrzQE=',
}

# Subclase de TrendReq para usar encabezados y cookies personalizados
class TrendReq(UTrendReq):
    def _get_data(self, url, method='get', trim_chars=0, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = headers
        if 'cookies' not in kwargs:
            kwargs['cookies'] = cookies
        return super()._get_data(url, method=method, trim_chars=trim_chars, **kwargs)

# Inicializar pytrends con la subclase personalizada
pytrends = TrendReq(hl='en-US', tz=360)

# Palabra clave a buscar
kw_list = ["ChatGPT"]

# Lista de países
countries = ["US"]

# Crear una lista para almacenar los DataFrames
data_frames = []

# Iterar sobre cada país y extraer los datos
for country in countries:
    try:
        # Configurar las opciones de búsqueda
        pytrends.build_payload(kw_list, timeframe='2000-01-01 2022-12-31', geo=country)
        
        # Obtener los datos de interés a lo largo del tiempo
        interest_over_time = pytrends.interest_over_time()
        
        # Verificar si la respuesta contiene datos
        if not interest_over_time.empty:
            # Agregar una columna para el país
            interest_over_time['Country'] = country
            # Agregar los datos a la lista de DataFrames
            data_frames.append(interest_over_time)
        
        # Esperar para evitar exceder el límite de tasa
        time.sleep(10)  # Espera de 10 segundos entre solicitudes
        
    except Exception as e:
        print(f"Error con el país {country}: {e}")
        time.sleep(60)  # Espera de 1 minuto en caso de error para intentar nuevamente

# Concatenar todos los DataFrames en uno solo
if data_frames:
    all_data = pd.concat(data_frames)

    # Eliminar la columna 'isPartial' si existe
    if 'isPartial' in all_data.columns:
        all_data = all_data.drop(columns=['isPartial'])

    # Guardar los datos en un archivo CSV
    all_data.to_csv('chatgpt_trends_2000_2022.csv', index=False)

    print("Datos guardados en 'chatgpt_trends_2000_2022.csv'")
else:
    print("No se obtuvieron datos.")
