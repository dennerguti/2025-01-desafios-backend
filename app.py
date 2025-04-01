import requests

def pesquisar_especie(nome, limite=10):
    url = "https://api.gbif.org/v1/occurrence/search"
    params = {
        "scientificName": nome,
        "hasCoordinate": "true",
        "limit": limite
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    
    else:
        print(f"Erro na requisição: {response.status_code}")
        return []

# Exemplo de uso
test_species = "Chelonia mydas" 
results = pesquisar_especie(test_species)
print(results[:3])  