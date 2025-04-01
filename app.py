import requests

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

especie = "Asterias rubens"  
resultado = pesquisar_especie(especie, -30, 30, -90, -60, 2000, 2020)
print(resultado[:3])  
