import random

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Answer, Question


def index(request):
    return render(request, 'askapp/index.html')


def pergunta(request):
    if request.method == 'POST':
        pergunta = request.POST.get('pergunta', '')
        resposta = random.choice(Answer.objects.all())
        Question.objects.create(text=pergunta, answer=resposta)
        return render(request, 'askapp/pergunta.html', {'resposta': resposta})
    else:
        return HttpResponse('Método não permitido', status=405)
