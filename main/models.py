from django.db import models
import datetime


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class QuestionText(models.Model):
    title = models.CharField(max_length=200, verbose_name="Вопрос с текстовым ответом")
    date_published = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос (ответ текст)'
        verbose_name_plural = 'Вопросы (ответ текст)'


class AnswerText(models.Model):
    question_id = models.ForeignKey(QuestionText, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name='Текст ответа')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class QuestionCheck(models.Model):
    title = models.CharField(max_length=200, verbose_name="Вопрос с чек боксами")
    date_published = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос (чек бокс)'
        verbose_name_plural = 'Вопросы (чек бокс)'


class AnswerCheck(models.Model):
    question_id = models.ForeignKey(QuestionCheck, on_delete=models.CASCADE)

    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

