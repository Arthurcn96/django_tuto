from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from polls.models import Question, Choice
from django.urls import reverse

class PollApiTests(APITestCase):

    def setUp(self) -> None:
        # Prepara oq for necessário pra rodar os testes
        self.question = Question.objects.create(
            question_text="Qual a melhor linguagem?",
            pub_date=timezone.now()
        )
        self.choice1 = Choice.objects.create(
            question=self.question,
            choice_text="Python",
            votes=10
        )
        self.choice2 = Choice.objects.create(
            question=self.question,
            choice_text="Java",
            votes=0
        )

    def test__get_question_list(self) -> None:
        # Verificar se requisição get é 200 e tamanho da resp > 0
        url = reverse('question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_nested_poll(self) -> None:
        # defina Json faça um POST verifique 201 e vê se tá no banco.
        url = reverse('question-list')
        data = {
            "question_text": "Time do coração?",
            "pub_date": timezone.now().isoformat(),
            "choices": [
                {"choice_text": "Vasco", "votes": 100},
                {"choice_text": "Outro", "votes": 0}
            ]
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Question.objects.filter(question_text="Time do coração?").exists())
        question = Question.objects.get(question_text="Time do coração?")
        self.assertEqual(question.choices.count(), 2)

    def test_delete_cascading(self) -> None:
        # Deleta, verifica o 204, tenta achar ele no banco.
        url = reverse('question-detail', kwargs={'pk': self.question.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Question.objects.filter(id=self.question.id).exists())
        # Verifica cascade nas choices
        self.assertFalse(Choice.objects.filter(question_id=self.question.id).exists())
