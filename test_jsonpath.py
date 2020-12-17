import requests
import jsonpath


URL_BASE_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes/'
URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos/'

avaliacoes = requests.get(URL_BASE_AVALIACOES)

# results = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(results)

first = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(first)

name = jsonpath.jsonpath(avaliacoes.json(), 'results[0].name')[0]
print(name)

nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
print(nota)

print('********************************************')

# Todos os nomes das pessoas que avaliaram o curso
names = jsonpath.jsonpath(avaliacoes.json(), 'results[*].name')
print('NAMES: ' + str(names))

# Todos os nomes das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print('AVALIAÇÕES: ' + str(notas))

