import requests
import csv 

def pesquisar_especie(nome_cientifico, lat_min, lat_max, lon_min, lon_max, ano_inicio, ano_fim, limite=10):
    url = "https://api.gbif.org/v1/occurrence/search"
    params = {
        "scientificName": nome_cientifico,
        "hasCoordinate": "true",
        "limit": limite,
        "decimalLatitude": f"{lat_min},{lat_max}",
        "decimalLongitude": f"{lon_min},{lon_max}",
        "year": f"{ano_inicio},{ano_fim}"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    
    else:
        print(f"Erro na requisição: {response.status_code}")
        return []
    
def salvar_em_csv(ocorrencias, nome_arquivo="ocorrencias.csv"):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["decimalLongitude", "decimalLatitude", "year", "day", "month"])  # Cabeçalho do CSV
        
        for ocorrencia in ocorrencias:
            try:
                longitude = ocorrencia["decimalLongitude"]
                latitude = ocorrencia["decimalLatitude"]
                data = ocorrencia["eventDate"].split("-")  # Split da data no formato 'YYYY-MM-DD'
                year = data[0]
                month = data[1]
                day = data[2] if len(data) > 2 else "01"  # Pegar o dia ou definir como 01
                writer.writerow([longitude, latitude, year, day, month])
            except KeyError:
                continue  # Caso a ocorrência não tenha os dados necessários, ignorar


especie = "Asterias rubens"  
resultado = pesquisar_especie(especie, -30, 30, -90, -60, 2000, 2020)
salvar_em_csv(resultado) 
