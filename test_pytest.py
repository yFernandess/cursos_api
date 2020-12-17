import requests

class TestCursos:
    headers = {'Authorization': 'Token bbf1f99ff5732f657fcbcd3e993cefa48992653e'}
    URL_BASE_CURSOS = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        response = requests.get(url=self.URL_BASE_CURSOS, headers=self.headers)
        assert response.status_code == 200

    def test_get_curso(self):
        response = requests.get(url=f'{self.URL_BASE_CURSOS}6/', headers=self.headers)
        assert response.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "title": "Gerência Ágil de Projetos com Scrum 345",
            "url": "http://www.gerenciaagil.com.br/scrum345"
        }

        response = requests.post(url=self.URL_BASE_CURSOS, headers=self.headers, data=novo_curso)

        # Testando o código de status HTTP 201 - Created
        assert response.status_code == 201

        # Testando se o título do curso retornado é o mesmo do informado
        assert response.json()['title'] == novo_curso['title']

    def test_put_curso(self):
        updated = {
            "title": "Novo curso de Ruby 34",
            "url": "http://cursoderuby34.com.br"
        }

        response = requests.put(url=f'{self.URL_BASE_CURSOS}6/', headers=self.headers, data=updated)

        # Testando o código de status HTTP
        assert response.status_code == 200

    def test_put_title_curso(self):
        updated = {
            "title": "Novo curso de Ruby 226",
            "url": "http://cursoderuby226.com.br"
        }

        response = requests.put(url=f'{self.URL_BASE_CURSOS}6/', headers=self.headers, data=updated)

        # Testando o título
        assert response.json()['title'] == updated['title']

    def test_delete_curso(self):
        response =  requests.delete(url=f'{self.URL_BASE_CURSOS}6/', headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0

