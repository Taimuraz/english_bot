from django.db import models


class GrammarQuestions(models.Model):
    text = models.TextField(max_length=1000)

class Choice(models.Model):
    text = models.CharField(max_length=255)
    is_correct_answer = models.BooleanField()
    question = models.ForeignKey(GrammarQuestions, related_name='questions', on_delete=models.CASCADE)

