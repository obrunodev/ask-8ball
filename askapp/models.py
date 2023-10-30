from django.db import models


class Answer(models.Model):
    """Answer model"""
    text = models.CharField(max_length=255, verbose_name='Resposta')

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return self.text


class Question(models.Model):
    """Question model"""
    text = models.CharField(max_length=255, verbose_name='Pergunta')
    answer = models.CharField(max_length=255, verbose_name='Resposta')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.text
