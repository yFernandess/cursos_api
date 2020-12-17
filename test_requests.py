import requests


URL_BASE_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes'
URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos'
# GET Avaliações

avaliacoes = requests.get(URL_BASE_AVALIACOES)

# Acessando o código de status HTTP
print(avaliacoes.status_code)

# Acessando os dados da resposta
print(avaliacoes.json())
print(type(avaliacoes.json()))

# Acessando a quantidade de registros
print('Quantidade de avaliações: ' + str(avaliacoes.json()['count']))

# Acessando a próxima página de resultados
print('Próxima página de resultados: ' + str(avaliacoes.json()['next']))


# Acessando os resultados da página
print('Resultados da página: ' + str(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
print('Primeiro resultado: ' + str(avaliacoes.json()['results'][0]))

# Acessando o último elemento da lista de resultados
print('Último resultado: ' + str(avaliacoes.json()['results'][-1]))

# Acessando o nome da pessoa que fez a última avaliação
print('Nome da pessoa que fez a última avaliação: ' + str(avaliacoes.json()['results'][-1]['name']))


# GET Avaliação
avaliacao = requests.get(URL_BASE_AVALIACOES + '/5')
print('Avaliação de número 5: ' + str(avaliacao.json()))

print('*********************************************************************')

# GET Cursos
headers = {'Authorization': 'Token bbf1f99ff5732f657fcbcd3e993cefa48992653e'}

cursos = requests.get(url=URL_BASE_CURSOS, headers=headers)
print('Cursos: ' + str(cursos.json()))