import random

from .models import Answer, Question

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    contagem_perguntas = Question.objects.count()
    return render(request, 'askapp/index.html', {'contagem_perguntas': contagem_perguntas})


def pergunta(request):
    if request.method == 'POST':
        pergunta = request.POST.get('pergunta', '')
        if not pergunta:
            return HttpResponse('Pergunta não informada', status=400)
        pergunta_existe = Question.objects.filter(text=pergunta).exists()
        if pergunta_existe:
            resposta = "Já respondi essa pergunta!"
        else:
            resposta = random.choice(Answer.objects.all())
            Question.objects.create(text=pergunta, answer=resposta)
        return render(request, 'askapp/pergunta.html', {'resposta': resposta,
                                                        'contagem_perguntas': Question.objects.count()})
    else:
        return HttpResponse('Método não permitido', status=405)
