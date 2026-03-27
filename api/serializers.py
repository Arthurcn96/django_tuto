from rest_framework import serializers
from polls.models import Question, Choice

# Serializer para criar apenas a Escolha (usado no add/choice)
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']
        extra_kwargs = {'question': {'required': False}}

# Serializer para criar apenas a Pergunta (usado no add/question)
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']

# Serializer para criar Pergunta e Escolhas ao mesmo tempo (nested)
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
