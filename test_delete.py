import requests


URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos/'
URL_BASE_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes/'

headers = {'Authorization': 'Token bbf1f99ff5732f657fcbcd3e993cefa48992653e'}

result = requests.delete(url=f'{URL_BASE_CURSOS}3/', headers=headers)

# Testando o código HTTP
assert result.status_code == 204

# Testando se o tamanho do conteúdo do retorno é 0
assert len(result.text) == 0