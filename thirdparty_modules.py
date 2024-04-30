# Os módulos de terceiros são pacotes ou bibliotecas criados por outras pessoas e não fazem parte do conjunto padrão do Python.
# Você pode encontrar mais informações sobre pacotes e módulos na documentação oficial do Python e no site do pip.
# terminal: pip install requests   ---  requests-2.31.0

# Importação e uso de um módulo de terceiro

import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTPS para {url} retornou o status {response.status_code}")