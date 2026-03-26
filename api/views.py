from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from polls.models import Question, Choice
from .serializers import QuestionSerializer, PollSerializer, ChoiceSerializer


@api_view(['GET'])
def getData(request):
    question = Question.objects.all()
    # Usamos o serializer completo no GET para ver as escolhas juntas
    serialize = PollSerializer(question, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def addPoll(request):
    # Cria TUDO junto: Pergunta + Escolhas
    serializer = PollSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addQuestion(request):
    # Cria apenas a Pergunta
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addChoice(request):
    # Cria apenas uma Escolha (precisa enviar o 'question' id no JSON)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
