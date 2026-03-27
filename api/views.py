from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.models import Question, Choice
from .serializers import QuestionSerializer, PollSerializer, ChoiceSerializer

# Utilizando VIEWSET

# Viewset (GET,POST,DELETE,PUT)
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = PollSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
