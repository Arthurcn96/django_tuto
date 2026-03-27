from rest_framework.test import APITestCase
from rest_framework import status
from polls.models import Question, Choice

class PollApiTests(APITestCase):

    def setUp(self) -> None:
        # Prepara oq for necessário pra rodar os testes
       pass

    def test__get_question_list(self) -> None:
        #Verificar se requisição get é 200 e tamanho da resp > 0
        pass

    def test_create_nested_poll(self) -> None:
        # defina Json faça um POST verifique 201 e vê se tá no banco.
        pass

    def test_delete_cascading(self) -> None:
        # Deleta, verifica o 2004, tenta achar ele no banco.
        pass
