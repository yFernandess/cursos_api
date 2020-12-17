import requests


URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos/'
URL_BASE_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes/'

headers = {'Authorization': 'Token bbf1f99ff5732f657fcbcd3e993cefa48992653e'}

curso_atualizado = {
    "title": "Novo Curso de Scrum 3",
    "url": "http://www.novocursodescrum.com.br"
}

result = requests.put(url=f'{URL_BASE_CURSOS}3/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert result.status_code == 200

# Testando o título
assert result.json()['title'] == curso_atualizado['title']

