import requests


URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos/'
URL_BASE_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes/'

headers = {'Authorization': 'Token bbf1f99ff5732f657fcbcd3e993cefa48992653e'}

result = requests.get(url=URL_BASE_CURSOS, headers=headers)
print(result.json())

"""
 Um possível teste para as requisições seria testar o status_code
 da requisição. Nesse caso, se não devolver 200 o endpoint estará
 errado.
"""
assert result.status_code == 200

# Testando a quantidade de registros da requisição
assert result.json()['count'] == 4

# Testando se o primeiro titulo do curso está correto
assert result.json()['results'][0]['title'] == 'Novo curso de Ruby'