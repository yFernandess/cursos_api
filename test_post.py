import requests


URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos/'
URL_BASE_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes/'

headers = {'Authorization': 'Token bbf1f99ff5732f657fcbcd3e993cefa48992653e'}

novo_curso = {
    "title": "Gerência Ágil de Projetos com Scrum 2",
    "url": "http://www.gerenciaagil.com.br/scrum2"
}

result = requests.post(url=URL_BASE_CURSOS, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201 - Created
assert result.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert result.json()['title'] == novo_curso['title']