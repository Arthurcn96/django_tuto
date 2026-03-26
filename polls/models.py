import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
            return self.question_text

    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
    )

    # Método para verificar se a pergunta foi publicada recentemente (último dia)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # TODO: AINDA
    # Adicionamos o related_name='choices'
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
            return self.choice_text
