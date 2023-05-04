import requests

# Faz uma requisição GET para a API do GitHub
response = requests.get('https://api.github.com/')

# Imprime o status da resposta
print(response.status_code)

# Imprime o conteúdo da resposta
print(response.content)