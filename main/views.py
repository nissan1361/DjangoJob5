from django.shortcuts import render
from .models import *
from .forms import AddForm


def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Форма была не верной!')

    qst = Question.objects.all() # Модель вопросов с вариантами ответов
    ans = Answer.objects.all() # Варианты ответов
    qt = QuestionText.objects.all() # Вопросы с текстовым ответом
    tex = Text.objects.all() # Текст ответа

    form = AddForm

    return render(request, 'main/index.html', {
        'title': 'Опросы пользователей',
        'qst': qst,
        'ans': ans,
        'qt': qt,
        'tex': tex,
        'form': form,
    })

