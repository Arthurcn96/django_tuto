from rest_framework import serializers
from polls.models import Question, Choice

# Serializer para criar apenas a Escolha (usado no add/choice)
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']

# Serializer para criar apenas a Pergunta (usado no add/question)
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']

# Serializer completo (Pergunta + Escolhas juntas - usado no add/poll)
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False) # Agora é opcional aqui

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            # Removemos o question dos dados da choice se ele vier duplicado
            choice_data.pop('question', None)
            Choice.objects.create(question=question, **choice_data)
        return question
